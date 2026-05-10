#!/usr/bin/env python3
"""
Wifther.AI - Bug Scanner
AST-based analysis engine (Python polyglot fallback for SIC architecture)

Single-file stdin mode:
  echo '{"file": "foo.py", "source": "..."}' | python wifther.py

Directory stdin mode:
  echo '{"directory": "C:/project"}' | python wifther.py

Corresponds to architecture spec in main.sic / scanner.sic.
Replace with native SIC binary when sic-codegen completes function-body lowering.
"""

import ast
import difflib
import json
import sys
from pathlib import Path

_SKIP_DIRS = frozenset({
    "__pycache__", ".git", ".venv", "venv", "env",
    "node_modules", ".tox", "dist", "build",
})


def _unified_diff(orig: str, sugg: str, lineno: int) -> str | None:
    lines = list(difflib.unified_diff(
        [orig + "\n"],
        [sugg + "\n"],
        fromfile=f"line {lineno}",
        tofile=f"line {lineno} (suggested)",
        lineterm="",
    ))
    return "\n".join(lines) if lines else None


class _BugVisitor(ast.NodeVisitor):
    def __init__(self, lines: list[str]):
        self.findings: list[dict] = []
        self._lines = lines

    def _src(self, lineno: int) -> str:
        i = lineno - 1
        return self._lines[i] if 0 <= i < len(self._lines) else ""

    def _visit_funcdef(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        args = node.args
        n_args = len(args.args)
        n_def = len(args.defaults)
        for i, default in enumerate(args.defaults):
            if not isinstance(default, (ast.List, ast.Dict, ast.Set)):
                continue
            arg_name = args.args[n_args - n_def + i].arg
            repr_ = "[]" if isinstance(default, ast.List) else ("{}" if isinstance(default, ast.Dict) else "set()")
            orig = self._src(default.lineno)
            sugg = orig.replace(f"={repr_}", "=None", 1)
            self.findings.append({
                "type": "MutableDefaultArg",
                "line": default.lineno,
                "severity": 2,
                "message": f"Mutable default argument {repr_} for '{arg_name}' — shared across all calls",
                "fix": f"Use None sentinel: `def {node.name}(..., {arg_name}=None)`, then `if {arg_name} is None: {arg_name} = {repr_}`",
                "diff": _unified_diff(orig, sugg, default.lineno),
            })
        self.generic_visit(node)

    visit_FunctionDef = _visit_funcdef
    visit_AsyncFunctionDef = _visit_funcdef

    def visit_ExceptHandler(self, node: ast.ExceptHandler) -> None:
        if node.type is None:
            orig = self._src(node.lineno)
            sugg = orig.replace("except:", "except Exception:")
            self.findings.append({
                "type": "BareExceptPass",
                "line": node.lineno,
                "severity": 2,
                "message": "Bare except: catches SystemExit and KeyboardInterrupt",
                "fix": "Replace with `except Exception:` or a specific exception type",
                "diff": _unified_diff(orig, sugg, node.lineno),
            })
        self.generic_visit(node)

    _SECRET_NAMES = frozenset({
        "password", "passwd", "api_key", "api_secret",
        "secret", "secret_key", "token", "auth_token", "access_token",
    })

    def visit_Assign(self, node: ast.Assign) -> None:
        if not (isinstance(node.value, ast.Constant) and isinstance(node.value.value, str) and node.value.value):
            self.generic_visit(node)
            return
        for target in node.targets:
            if isinstance(target, ast.Name):
                name = target.id
            elif isinstance(target, ast.Attribute):
                name = target.attr
            else:
                continue
            if name.lower() in self._SECRET_NAMES:
                self.findings.append({
                    "type": "HardcodedSecret",
                    "line": node.lineno,
                    "severity": 3,
                    "message": f"Hardcoded {name} literal in source",
                    "fix": f"Use `os.environ['{name.upper()}']` or a secrets manager (python-dotenv, AWS Secrets Manager)",
                    "diff": None,
                })
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        func = node.func
        name = None
        if isinstance(func, ast.Name):
            name = func.id
        elif isinstance(func, ast.Attribute):
            name = func.attr
        if name in ("eval", "exec"):
            self.findings.append({
                "type": "DangerousFunction",
                "line": node.lineno,
                "severity": 3,
                "message": f"Use of {name}() enables arbitrary code execution",
                "fix": "Use `json.loads()`, `ast.literal_eval()`, or a sandboxed alternative",
                "diff": None,
            })
        self.generic_visit(node)


def scan_code_patterns(source: str, filename: str = "<string>") -> list[dict]:
    try:
        tree = ast.parse(source, filename=filename)
    except SyntaxError as e:
        return [{
            "type": "SyntaxError",
            "line": e.lineno or 0,
            "severity": 3,
            "message": f"Syntax error: {e.msg}",
            "fix": None,
            "diff": None,
        }]
    visitor = _BugVisitor(source.splitlines())
    visitor.visit(tree)
    visitor.findings.sort(key=lambda f: f["line"])
    return visitor.findings


def scan_file(filepath: str | Path) -> dict:
    path = Path(filepath)
    try:
        source = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return {"file": str(path), "error": str(e), "findings": [], "bug_count": 0}
    findings = scan_code_patterns(source, filename=path.name)
    return {"file": str(path), "findings": findings, "bug_count": len(findings)}


def scan_directory(directory: str | Path, extensions: list[str] | None = None) -> dict:
    if extensions is None:
        extensions = [".py"]
    root = Path(directory)
    if not root.exists():
        return {"status": "error", "message": f"Directory not found: {directory}"}

    results = []
    files_scanned = 0
    total_bugs = 0

    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix not in extensions:
            continue
        if any(part in _SKIP_DIRS for part in path.parts):
            continue
        result = scan_file(path)
        files_scanned += 1
        total_bugs += result["bug_count"]
        if result["bug_count"] > 0 or "error" in result:
            results.append(result)

    return {
        "status": "completed",
        "directory": str(root.resolve()),
        "files_scanned": files_scanned,
        "total_bugs": total_bugs,
        "results": results,
    }


def main() -> None:
    raw = sys.stdin.read()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(json.dumps({"status": "error", "message": f"Invalid JSON input: {e}"}))
        sys.exit(1)

    if "directory" in data:
        out = scan_directory(data["directory"], data.get("extensions"))
        print(json.dumps(out, indent=2))
        return

    source = data.get("source", "")
    if not isinstance(source, str):
        print(json.dumps({"status": "error", "message": "'source' must be a string"}))
        sys.exit(1)

    findings = scan_code_patterns(source, filename=data.get("file", "<string>"))
    print(json.dumps({
        "status": "completed",
        "file": data.get("file", "unknown"),
        "findings": findings,
        "bug_count": len(findings),
    }, indent=2))


if __name__ == "__main__":
    main()

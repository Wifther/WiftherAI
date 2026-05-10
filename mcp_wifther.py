#!/usr/bin/env python3
"""
Wifther.AI MCP Server

Exposes two tools over MCP stdio transport:
  scan_project(directory_path)  — scan entire project, zero source tokens to Claude
  scan_for_bugs(file, source)   — scan source string (backward-compatible)

Install: pip install mcp
Add to Claude Code: claude mcp add wifther -- python path/to/mcp_wifther.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wifther import scan_code_patterns, scan_directory, scan_file

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Wifther.AI")


@mcp.tool()
def scan_project(directory_path: str) -> dict:
    """
    Scan an entire project directory for bugs and anti-patterns.

    Walks all .py files locally — Claude never reads the source code.
    Returns only findings: file paths, line numbers, types, fixes, and diffs.
    Detects: MutableDefaultArg, BareExceptPass, HardcodedSecret, DangerousFunction.

    Token cost: O(findings), not O(source lines).
    """
    return scan_directory(directory_path)


@mcp.tool()
def scan_single_file(file_path: str) -> dict:
    """
    Scan a single file by path for bugs and anti-patterns.

    Claude does not need to read the file — Wifther reads it locally.
    Returns findings with unified diffs for auto-fixable issues.
    """
    return scan_file(file_path)


@mcp.tool()
def scan_for_bugs(file: str, source: str) -> dict:
    """
    Scan source code string for bugs and anti-patterns.

    Use scan_project() or scan_single_file() instead when possible —
    those tools avoid sending source code to Claude entirely.

    Returns findings with type, line, severity, fix suggestion, and unified diff.
    Detects: MutableDefaultArg, BareExceptPass, HardcodedSecret, DangerousFunction.
    """
    findings = scan_code_patterns(source, filename=file)
    return {
        "status": "completed",
        "file": file,
        "findings": findings,
        "bug_count": len(findings),
    }


if __name__ == "__main__":
    mcp.run()

# Wifther.AI — Expert AST Bug Scanner (MCP)

Wifther.AI is a high-performance, locally-hosted bug scanning engine designed to integrate seamlessly with **Claude Code** and **Claude Desktop** via the Model Context Protocol (MCP).

## 🚀 Why Wifther.AI?

*   **Zero-Token Scanning**: Unlike traditional AI prompts, Wifther scans your files locally. It only sends findings to Claude, saving up to 99% of your context window and tokens.
*   **AST Intelligence**: Uses Abstract Syntax Tree (AST) analysis to understand code structure. No false positives from comments or strings.
*   **Smart Recommendations**: Every bug found comes with a specific fix and a Unified Diff that Claude can apply instantly.
*   **SIC-Native Architecture**: Built according to the SIC programming language specifications, ready for native machine-code execution.

---

## 🔍 Detected Patterns

- **MutableDefaultArg**: Detects `def f(x=[])` patterns that cause shared state bugs.
- **BareExceptPass**: Finds dangerous `except:` blocks that hide critical system errors.
- **HardcodedSecret**: Identifies passwords and API keys in source code.
- **DangerousFunction**: Flags `eval()` and `exec()` usage.

---

## 🛠 Installation

### 1. Quick Install (Windows)
Run the `install.bat` file. It will install the necessary dependencies and show you the exact command to link Wifther to Claude.

### 2. Manual Setup
```bash
pip install mcp
```

### 3. Add to Claude Code
Run this command in your terminal:
```bash
claude mcp add wifther -- python "C:/PATH/TO/YOUR/WiftherAI/mcp_wifther.py"
```

### 4. Add to Claude Desktop
Add this to your `%APPDATA%\Claude\claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "wifther": {
      "command": "python",
      "args": ["C:/PATH/TO/YOUR/WiftherAI/mcp_wifther.py"]
    }
  }
}
```

---

## 🏗 Architecture

Wifther.AI follows a **Cloud-Local Hybrid** model:
- **Specification**: Written in **SIC lang** (`main.sic`, `scanner.sic`) for maximum safety and performance.
- **Engine**: Currently powered by a high-speed Python AST fallback to ensure compatibility while the SIC compiler matures.

---

## 📄 License
This project is open-source. Feel free to contribute!

---

*(Česky: Wifther.AI je lokální skener chyb pro Claude Code, který šetří tokeny tím, že kód analyzuje přímo u vás na stroji pomocí AST analýzy.)*
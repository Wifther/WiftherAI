# Wifther.AI — Bug Scanner MCP Server

## English

### What is Wifther.AI?

Wifther.AI is a local, offline bug scanner that detects common code anti-patterns. It runs as an MCP server, exposing a `scan_for_bugs` tool directly inside Claude Code and Claude Desktop.

**Detected patterns:**
- `MutableDefaultArg` — `def f(x=[])` or `def f(x={})` shared across all calls
- `BareExceptPass` — bare `except:` catching `SystemExit` and `KeyboardInterrupt`
- `HardcodedSecret` — `password = "..."` or `api_key = "..."` literals in source

**Architecture:**
- `wifther.py` — core scan logic (Python polyglot fallback, all patterns here)
- `mcp_wifther.py` — MCP server wrapping wifther.py
- `main.sic` / `scanner.sic` — SIC architecture spec (becomes native binary when SIC body lowering is implemented)

### Requirements

- Python 3.10+
- `mcp` package: `pip install mcp`

### Install

Run `install.bat` or manually:

```bat
pip install mcp
```

### Add to Claude Code

```bat
claude mcp add wifther -- python C:\Users\Jenik\Desktop\WiftherAI\mcp_wifther.py
```

Verify it's registered:

```bat
claude mcp list
```

### Add to Claude Desktop

Open `%APPDATA%\Claude\claude_desktop_config.json` and add:

```json
{
  "mcpServers": {
    "wifther": {
      "command": "python",
      "args": ["C:\\Users\\Jenik\\Desktop\\WiftherAI\\mcp_wifther.py"]
    }
  }
}
```

Restart Claude Desktop after saving.

### Usage in Claude

Once installed, ask Claude:

> "Scan this Python code for bugs: `def process(items=[]): ...`"

Claude will call `scan_for_bugs` automatically and return findings.

### Run Tests

```bat
python test_wifther.py
```

Expected: 7/7 tests pass.

---

## Česky

### Co je Wifther.AI?

Wifther.AI je lokální, offline skener chyb, který detekuje běžné anti-vzory v kódu. Běží jako MCP server a zpřístupňuje nástroj `scan_for_bugs` přímo v Claude Code a Claude Desktop.

**Detekované vzory:**
- `MutableDefaultArg` — `def f(x=[])` nebo `def f(x={})` — sdílený objekt napříč všemi voláními
- `BareExceptPass` — holý `except:` zachytávající i `SystemExit` a `KeyboardInterrupt`
- `HardcodedSecret` — `password = "..."` nebo `api_key = "..."` literály ve zdrojovém kódu

### Požadavky

- Python 3.10+
- Balíček `mcp`: `pip install mcp`

### Instalace

Spusť `install.bat` nebo ručně:

```bat
pip install mcp
```

### Přidání do Claude Code

```bat
claude mcp add wifther -- python C:\Users\Jenik\Desktop\WiftherAI\mcp_wifther.py
```

Ověření registrace:

```bat
claude mcp list
```

### Přidání do Claude Desktop

Otevři `%APPDATA%\Claude\claude_desktop_config.json` a přidej:

```json
{
  "mcpServers": {
    "wifther": {
      "command": "python",
      "args": ["C:\\Users\\Jenik\\Desktop\\WiftherAI\\mcp_wifther.py"]
    }
  }
}
```

Po uložení restartuj Claude Desktop.

### Použití v Claudovi

Po instalaci řekni Claudovi:

> "Proskenuj tento Python kód pro chyby: `def process(items=[]): ...`"

Claude automaticky zavolá `scan_for_bugs` a vrátí nálezy.

### Spuštění testů

```bat
python test_wifther.py
```

Očekáváno: 7/7 testů projde.

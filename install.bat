@echo off
setlocal

echo ============================================
echo  Wifther.AI MCP Server - Installer
echo ============================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found.
    echo Install from https://python.org ^(add to PATH^)
    pause
    exit /b 1
)

echo Python found. Installing mcp package...
pip install mcp
if errorlevel 1 (
    echo ERROR: pip install mcp failed.
    pause
    exit /b 1
)

echo.
echo ============================================
echo  Installation complete!
echo ============================================
echo.
echo To add Wifther.AI to Claude Code, run:
echo.
echo   claude mcp add wifther -- python "%~dp0mcp_wifther.py"
echo.
echo To add to Claude Desktop, open:
echo   %%APPDATA%%\Claude\claude_desktop_config.json
echo.
echo And add inside "mcpServers":
echo   "wifther": {
echo     "command": "python",
echo     "args": ["%~dp0mcp_wifther.py"]
echo   }
echo.
pause

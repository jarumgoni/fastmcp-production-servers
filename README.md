# 🔌 Production MCP (Model Context Protocol) Servers Suite (2026)

> Turnkey FastMCP servers in Python for Claude Code, Claude Desktop, Cursor, and Windsurf. Connect your AI assistant to PostgreSQL, persistent SQLite memory, Playwright headless browsing, and Docker.

[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)
[![Get Full Suite](https://img.shields.io/badge/Gumroad-Get%20Full%20MCP%20Suite%20($14.50)-blue?logo=gumroad)](https://masbintoro.gumroad.com/l/production-mcp-server-suite/LAUNCH50)

---

## ⚡ Why This Exists
Connecting Claude or Cursor to real-world databases and tools via Anthropic's **Model Context Protocol (MCP)** frequently fails due to JSON-RPC crashes, stdio pollution (`print()` breaking protocol pipes), and environment PATH issues.

This repository provides clean, tested FastMCP servers with proper stderr isolation.

---

## 🛠️ Free Starter Servers Included

1. **`sqlite_memory_mcp.py`**: Gives Claude Code and Cursor persistent, durable semantic memory across terminal sessions.
2. **`postgres_inspector_mcp.py`**: Safe read-only PostgreSQL schema introspector and query runner.

---

## 📦 Production MCP Suite Includes:
- 🚀 **Playwright Headless Browser MCP**: Real Chromium web automation & DOM extractor.
- 💾 **SQLite Memory MCP**: Durable architecture decision tracker.
- 🐘 **Postgres Live Inspector**: Zero-risk read-only schema analyzer.
- 📋 **Pre-configured `claude_desktop_config.json`**: Ready to paste for macOS, Windows & Linux.
- 🔧 **Zero-Crash Stdio Logger**: Fixes "Connection closed" errors.

👉 **[Download the Full Production MCP Suite ($14.50)](https://masbintoro.gumroad.com/l/production-mcp-server-suite/LAUNCH50)** (50% OFF with code `LAUNCH50`)

---

## 🚀 Quick Setup

```bash
pip install mcp psycopg2-binary
```

Add to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "sqlite-memory": {
      "command": "python3",
      "args": ["/path/to/servers/sqlite_memory_mcp.py"]
    }
  }
}
```

*Maintained by Masbin Digital Labs.*

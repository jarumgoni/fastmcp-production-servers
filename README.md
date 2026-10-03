# 🔌 FastMCP Production Servers in Python (2026)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-brightgreen.svg)](https://python.org)
[![FastMCP](https://img.shields.io/badge/Model%20Context%20Protocol-Compatible-purple.svg)](https://modelcontextprotocol.io)

> Production-ready, turnkey **Model Context Protocol (MCP)** servers built in Python with FastMCP for **Claude Code**, **Cursor IDE**, and **Windsurf**.

---

### 🎁 Looking for 20+ Production MCP Connectors?
> Includes **PostgreSQL**, **Redis Cache**, **Stripe Billing**, **Playwright Web Browser**, and **Docker Host Management**:  
> 👉 **[Explore Full Developer Toolkits on Gumroad (Code: LAUNCH50)](https://masbintoro.gumroad.com/l/langgraph-multi-agent-starter-kit/LAUNCH50)**

---

## 📦 What's Inside

| Server Name | Protocol | Primary Capability | Auth Type |
| :--- | :--- | :--- | :--- |
| `sqlite-memory` | Stdio / SSE | Persistent short & long-term conversational memory | Local SQLite |
| `postgres-db` | Stdio / SSE | Zero-latency schema introspection & parameterized queries | Connection Pool |
| `playwright-browser` | Stdio | Headless DOM execution, screenshot & PDF generation | Native Headless |

## 🚀 Quick Setup with Claude Code / Cursor

Add to your `claude_desktop_config.json` or `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "sqlite-memory": {
      "command": "python3",
      "args": ["/path/to/fastmcp-production-servers/servers/sqlite_memory.py"]
    }
  }
}
```

## 📄 License
MIT License © 2026 Masbin. Commercial enterprise support at [ProChat Commerce Labs](https://prochatcommerce.com).

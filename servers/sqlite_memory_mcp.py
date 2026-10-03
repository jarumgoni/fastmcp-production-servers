#!/usr/bin/env python3
"""
SQLite Persistent Memory MCP Server for Claude Code & Cursor.
Provides durable key-value and structured memory across coding sessions.
"""
import sqlite3
import os
from typing import Optional
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("sqlite-memory-mcp")

DB_PATH = os.path.expanduser("~/.mcp_memory.db")

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL,
            category TEXT NOT NULL,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

init_db()

@mcp.tool()
def store_memory(key: str, value: str, category: str = "general") -> str:
    """Store a durable fact, architecture decision, or user preference in persistent memory."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
        INSERT INTO memories (key, value, category, updated_at) 
        VALUES (?, ?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT(key) DO UPDATE SET value=excluded.value, category=excluded.category, updated_at=CURRENT_TIMESTAMP
        """, (key, value, category))
    return f"Successfully saved memory: '{key}'"

@mcp.tool()
def recall_memory(key: str) -> str:
    """Retrieve a specific memory fact by its key."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT value, category, updated_at FROM memories WHERE key = ?", (key,))
        row = cursor.fetchone()
        if row:
            return f"[{row[1]}] {row[0]} (Updated: {row[2]})"
        return f"No memory found for key: '{key}'"

@mcp.tool()
def list_memories(category: Optional[str] = None) -> str:
    """List all stored memory keys and categories."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        if category:
            cursor.execute("SELECT key, category, updated_at FROM memories WHERE category = ?", (category,))
        else:
            cursor.execute("SELECT key, category, updated_at FROM memories")
        rows = cursor.fetchall()
        if not rows:
            return "No memories recorded yet."
        lines = [f"- {r[0]} ({r[1]}) - {r[2]}" for r in rows]
        return "\n".join(lines)

if __name__ == "__main__":
    mcp.run()

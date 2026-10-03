#!/usr/bin/env python3
"""
PostgreSQL Read-Only Schema & Data Inspector MCP Server.
Allows Claude Code & Cursor to inspect tables, schema, constraints, and execute safe queries.
"""
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("postgres-inspector-mcp")

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/mydb")

@mcp.tool()
def list_tables() -> str:
    """List all public tables, column counts, and approximate row counts."""
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            ORDER BY table_name;
        """)
        tables = [t[0] for t in cursor.fetchall()]
        conn.close()
        return "Public Tables:\n" + "\n".join([f"- {t}" for t in tables])
    except Exception as e:
        return f"Database Error: {str(e)}"

@mcp.tool()
def describe_table(table_name: str) -> str:
    """Get detailed column definitions, data types, and primary keys for a table."""
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("""
            SELECT column_name, data_type, is_nullable, column_default
            FROM information_schema.columns
            WHERE table_name = %s AND table_schema = 'public'
            ORDER BY ordinal_position;
        """, (table_name,))
        cols = cursor.fetchall()
        conn.close()
        if not cols:
            return f"Table '{table_name}' not found."
        lines = [f"- {c['column_name']} ({c['data_type']}) Nullable: {c['is_nullable']}" for c in cols]
        return f"Schema for {table_name}:\n" + "\n".join(lines)
    except Exception as e:
        return f"Database Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()

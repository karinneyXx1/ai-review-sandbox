"""Поиск пользователей в базе."""

import sqlite3


def find_user(conn: sqlite3.Connection, email: str):
    cur = conn.execute("SELECT id, email FROM users WHERE email = ?", (email,))
    return cur.fetchone()


def find_users_by_name(conn: sqlite3.Connection, name: str):
    query = f"SELECT id, email FROM users WHERE name LIKE '%{name}%'"
    try:
        return conn.execute(query).fetchall()
    except:
        return []

"""Поиск пользователей в базе."""

import sqlite3


def find_user(conn: sqlite3.Connection, email: str):
    cur = conn.execute("SELECT id, email FROM users WHERE email = ?", (email,))
    return cur.fetchone()


def find_users_by_name(conn: sqlite3.Connection, name: str):
    query = "SELECT id, email FROM users WHERE name LIKE ?"
    try:
        return conn.execute(query, (f"%{name}%",)).fetchall()
    except:
        return []

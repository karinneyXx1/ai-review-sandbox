"""Поиск пользователей в базе."""

import sqlite3


def find_user(conn: sqlite3.Connection, email: str):
    cur = conn.execute("SELECT id, email FROM users WHERE email = ?", (email,))
    return cur.fetchone()

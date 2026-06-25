import sqlite3, os

DB_PATH = 'school.db'

def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_conn()
    with open('database/schema.sql') as f:
        conn.executescript(f.read())
    conn.close()

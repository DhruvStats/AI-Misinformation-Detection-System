import sqlite3
from datetime import datetime

DB_NAME = "database.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            prediction TEXT,
            response_time REAL,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def log_prediction(text, prediction, response_time):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO predictions (text, prediction, response_time, created_at)
        VALUES (?, ?, ?, ?)
    """, (text, prediction, response_time, datetime.now()))

    conn.commit()
    conn.close()
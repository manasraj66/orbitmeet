import sqlite3
from pathlib import Path
DB_PATH = Path(__file__).resolve().parent.parent / 'orbit.db'

def init_db():
    with sqlite3.connect(DB_PATH) as db:
        db.execute('CREATE TABLE IF NOT EXISTS scheduled_meetings (id INTEGER PRIMARY KEY, title TEXT NOT NULL, starts_at TEXT NOT NULL)')

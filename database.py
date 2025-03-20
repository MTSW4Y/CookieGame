import sqlite3

DB_PATH = 'central_database.db'

def get_connection():
    return sqlite3.connect(DB_PATH)

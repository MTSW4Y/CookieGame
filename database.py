import sqlite3
import pandas as pd

DB_PATH = 'central_database.db'

def get_connection():
    return sqlite3.connect(DB_PATH)

def add_order(customer, stroopwafels, prince_koeken, orios):
    with get_connection() as conn:
        conn.execute(
            'INSERT INTO orders (customer, stroopwafels, prince_koeken, orios) VALUES (?, ?, ?, ?)',
            (customer, stroopwafels, prince_koeken, orios)
        )
        conn.commit()

def get_orders():
    with get_connection() as conn:
        return pd.read_sql('SELECT * FROM orders', conn)

def clear_orders():
    with get_connection() as conn:
        conn.execute('DELETE FROM orders')
        conn.commit()

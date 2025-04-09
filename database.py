import sqlite3
import pandas as pd
import time
# from datetime import datetime

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

def add_time(simulation_time):
    # clock_timestamp = int(time.time())  # Unix timestamp
    clock_timestamp = time.time()
    with get_connection() as conn:
        conn.execute(
            'INSERT INTO time (simulation_time, clock_time) VALUES (?, ?)',
            (simulation_time, clock_timestamp)
        )
        conn.commit()

def get_times():
    with get_connection() as conn:
        df = pd.read_sql('SELECT * FROM time', conn)
        # df['clock_time'] = pd.to_datetime(df['clock_time'], unit='s')  # omzetting naar leesbare datum
        return df

import sqlite3
import pandas as pd
import time

DB_PATH = 'central_database.db'

def get_connection():
    return sqlite3.connect(DB_PATH)

##############################  AANMAKEN KLANT ORDERS  ##############################

def add_order(customer, due_date, stroopwafels, prince_koeken, penny_wafels):
    with get_connection() as conn:
        conn.execute(
            'INSERT INTO orders (customer,due_date, stroopwafels, prince_koeken, penny_wafels) VALUES (?, ?, ?, ?, ?)',
            (customer, due_date, stroopwafels, prince_koeken, penny_wafels)
        )
        conn.commit()

def get_orders():
    with get_connection() as conn:
        result = pd.read_sql('SELECT * FROM orders ORDER BY id DESC', conn)
        return result.reset_index(drop=True)

def clear_orders():
    with get_connection() as conn:
        conn.execute('DELETE FROM orders')
        conn.commit()

##############################  GEREEDMELDEN KLANT ORDERS  ##############################

def add_ready_order(order_no, group_no, del_stroopwafels, del_prince_koeken, del_penny_wafels, q_del_stroopwafels, q_del_prince_koeken, q_del_penny_wafels):
    log_date = get_simulation_time()
    with get_connection() as conn:
        conn.execute(
            'INSERT INTO ready_orders (order_no, group_no, log_date, del_stroopwafels, del_prince_koeken, del_penny_wafels, q_del_stroopwafels, q_del_prince_koeken, q_del_penny_wafels) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (order_no, group_no, log_date, del_stroopwafels, del_prince_koeken, del_penny_wafels, q_del_stroopwafels, q_del_prince_koeken, q_del_penny_wafels)
        )
        conn.commit()

def get_ready_orders():
    with get_connection() as conn:
        result = pd.read_sql('SELECT * FROM ready_orders ORDER BY id DESC', conn)
        return result.reset_index(drop=True)

def clear_ready_orders():
    with get_connection() as conn:
        conn.execute('DELETE FROM ready_orders')
        conn.commit()

##############################  SUPPLIES  ##############################

def add_supply(group_no, cookie, supply_type, number):
    log_date = get_simulation_time()
    with get_connection() as conn:
        conn.execute(
            'INSERT INTO supplies (group_no, log_date, cookie, supply_type, number) VALUES (?, ?, ?, ?, ?)',
            (group_no, log_date, cookie, supply_type, number)
        )
        conn.commit()

def get_supplies():
    with get_connection() as conn:
        result = pd.read_sql('SELECT * FROM supplies ORDER BY id DESC', conn)
        return result.reset_index(drop=True)

def clear_supplies():
    with get_connection() as conn:
        conn.execute('DELETE FROM supplies')
        conn.commit()

##############################  SIMULATIETIJD  ##############################

def get_simulation_time():
    with get_connection() as conn:
        df = pd.read_sql('SELECT * FROM time', conn)
        if not df.empty:
            return df.iloc[0]['simulation_time']
        return 'Simulatie loopt nog niet'

def upsert_time(simulation_time, row_id=1):
    clock_timestamp = time.time()
    with get_connection() as conn:
        cursor = conn.execute('SELECT COUNT(*) FROM time WHERE id = ?', (row_id,))
        exists = cursor.fetchone()[0]
        if exists:
            conn.execute(
                'UPDATE time SET simulation_time = ?, clock_time = ? WHERE id = ?',
                (simulation_time, clock_timestamp, row_id)
            )
        else:
            conn.execute(
                'INSERT INTO time (id, simulation_time, clock_time) VALUES (?, ?, ?)',
                (row_id, simulation_time, clock_timestamp)
            )
        conn.commit()

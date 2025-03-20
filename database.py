import sqlite3

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

# Voeg hier alvast drie orders toe
add_order('AH', 3, 16, 0)
add_order('Lidl', 0, 0, 25)
add_order('Jamin', 5, 5, 5)

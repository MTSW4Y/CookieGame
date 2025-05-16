import sqlite3

# Set up the SQLite database
DB_PATH = 'central_database.db'

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            customer TEXT,
            due_date TEXT,
            stroopwafels INTEGER,
            prince_koeken INTEGER,
            orios INTEGER
        )''')

        conn.execute('''CREATE TABLE IF NOT EXISTS ready_orders (
            id INTEGER PRIMARY KEY,
            groep INTEGER,
            order_id INTEGER,
            ready_date TEXT,
            gel_stroopwafels INTEGER,
            gel_prince_koeken INTEGER,
            gel_orios INTEGER,
            goede_stroopwafels INTEGER,
            goede_prince_koeken INTEGER,
            goede_orios INTEGER
        )''')

        conn.execute('''CREATE TABLE IF NOT EXISTS time (
            id INTEGER PRIMARY KEY,
            simulation_time TEXT,
            clock_time TEXT
        )''')

init_db()

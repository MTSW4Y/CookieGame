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
            group_no INTEGER,
            order_no INTEGER,
            log_date TEXT,
            del_stroopwafels INTEGER,
            del_prince_koeken INTEGER,
            del_orios INTEGER,
            q_del_stroopwafels INTEGER,
            q_del_prince_koeken INTEGER,
            q_del_orios INTEGER
        )''')

        conn.execute('''CREATE TABLE IF NOT EXISTS supplies (
            id INTEGER PRIMARY KEY,
            group_no INTEGER,
            log_date TEXT,
            cookie TEXT,
            supply_type TEXT,
            number INTEGER
        )''')

        conn.execute('''CREATE TABLE IF NOT EXISTS time (
            id INTEGER PRIMARY KEY,
            simulation_time TEXT,
            clock_time TEXT
        )''')

init_db()

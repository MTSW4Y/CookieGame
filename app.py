import streamlit as st
import sqlite3
import threading
import time
import random
from database import add_order

# Set up the SQLite database
DB_PATH = 'central_database.db'

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            customer TEXT,
            stroopwafels INTEGER,
            prince_koeken INTEGER,
            orios INTEGER
        )''')


init_db()

# Background process for generating random orders
CUSTOMERS = ['AH', 'Lidl', 'Jamin']

def generate_random_order():
    while True:
        customer = random.choice(CUSTOMERS)
        stroopwafels = random.choice([0, 2, 4, 6])
        prince_koeken = random.choice([0, 3, 6, 9])
        orios = random.choice([0, 5, 10, 15, 20, 25])
        add_order(customer, stroopwafels, prince_koeken, orios)
        time.sleep(60)  # Wacht een minuut voordat een nieuwe order wordt toegevoegd


order_thread = threading.Thread(target=generate_random_order, daemon=True)
order_thread.start()


# Main app layout
st.set_page_config(page_title='Streamlit Multi-Page App', layout="centered")
st.title("Main Menu")
st.write("Select a page from the sidebar to get started.")

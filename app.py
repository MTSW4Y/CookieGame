import streamlit as st
from streamlit_autorefresh import st_autorefresh
import sqlite3
import threading
import time
import random
from database import add_order
from datetime import datetime, timedelta

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

        conn.execute('''CREATE TABLE IF NOT EXISTS time (
            id INTEGER PRIMARY KEY,
            simulation_time TEXT,
            clock_time TEXT
        )''')

init_db()

# Timer settings
if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False
    st.session_state.day_count = 1
    st.session_state.current_time = datetime.strptime('09:00', '%H:%M')
    st.session_state.start_time = None

def start_timer():
    st.session_state.timer_running = True
    if st.session_state.start_time:
        pass
    else:
        st.session_state.start_time = time.time()

def stop_timer():
    st.session_state.timer_running = False
    # order_thread.stop()

def reset_timer():
    st.session_state.day_count = 1
    st.session_state.start_time = None

# Update the timer
if st.session_state.timer_running:
    elapsed_real_time = time.time() - st.session_state.start_time
    elapsed_game_time = timedelta(seconds=elapsed_real_time * 120)  # 4 minuten = 8 uur
    st.session_state.current_time = datetime.strptime('09:00', '%H:%M') + elapsed_game_time

    if st.session_state.current_time.strftime('%H:%M') >= '17:00':
        st.session_state.day_count += 1
        st.session_state.current_time = datetime.strptime('09:00', '%H:%M')
        st.session_state.start_time = time.time()  # Reset de starttijd

# Background process for generating random orders
CUSTOMERS = ['AH', 'Lidl', 'Jamin']

# def generate_random_order():
#     while True:
#         customer = random.choice(CUSTOMERS)
#         stroopwafels = random.choice([0, 2, 4, 6])
#         prince_koeken = random.choice([0, 3, 6, 9])
#         orios = random.choice([0, 5, 10, 15, 20, 25])
#         add_order(customer, stroopwafels, prince_koeken, orios)
#         time.sleep(600)  # Wacht een minuut voordat een nieuwe order wordt toegevoegd

# order_thread = threading.Thread(target=generate_random_order, daemon=True)
# order_thread.start()

# Main app layout
st.set_page_config(page_title='The Cookie Game', layout="centered")
st.title("Main Menu")
st.write("Select a page from the sidebar to get started.")

st_autorefresh(interval=5000, key="order_refresh")

st.button('Start Timer', on_click=start_timer)
st.button('Stop Timer', on_click=stop_timer)
st.button('Reset Timer', on_click=reset_timer)

st.write(f"Dag {st.session_state.day_count} - Tijd: {st.session_state.current_time.strftime('%H:%M')}")

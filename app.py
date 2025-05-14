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

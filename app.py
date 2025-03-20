### Directory Structure
# streamlit_app/
# ├── app.py
# ├── pages/
# │   ├── teams.py
# │   ├── leaderboard.py
# │   ├── order_management.py
# │   ├── customers.py
# │   └── suppliers.py
# └── database.py


### app.py
import streamlit as st
import sqlite3
from pathlib import Path

# Set up the SQLite database
DB_PATH = 'central_database.db'

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS example (id INTEGER PRIMARY KEY, name TEXT)')

init_db()

# Main app layout
st.set_page_config(page_title='The Cookie Game', layout="centered")
st.title("Main Menu")
st.write("Select a page from the sidebar to get started.")

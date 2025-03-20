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
st.set_page_config(page_title='Streamlit Multi-Page App', layout="centered")
st.title("Main Menu")

options = {
    "Teams": "pages/teams.py",
    "Leaderboard": "pages/leaderboard.py",
    "Order Management": "pages/order_management.py",
    "Customers": "pages/customers.py",
    "Suppliers": "pages/suppliers.py",
}

choice = st.selectbox("Select a page:", list(options.keys()))

if st.button("Go"):
    selected_page = options[choice]
    st.experimental_set_query_params(page=selected_page)
    exec(Path(selected_page).read_text())

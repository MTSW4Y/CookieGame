import streamlit as st
import sqlite3
from database import get_connection

st.title('Order Management')

# Toon bestaande orders
with get_connection() as conn:
    orders = conn.execute('SELECT * FROM orders').fetchall()

st.write("### Existing Orders")
for order in orders:
    st.write(order)

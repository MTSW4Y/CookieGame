import streamlit as st
import time
from database import get_orders
# from app import new_order_message

st.title('Order Management')

st.write("### Openstaande Orders")
orders_placeholder = st.empty()

while True:
    orders_df = get_orders()
    orders_placeholder.dataframe(orders_df)
    time.sleep(10)  # Ververs de tabel elke 5 seconden

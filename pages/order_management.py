import streamlit as st
import time
from database import get_orders
from app import new_order_message, last_order_time

st.title('Order Management')

# Toon nieuwe order melding
# if new_order_message and last_order_time:
#     if time.time() - last_order_time <= 10:  # Meldingen worden 10 seconden weergegeven
#         st.success(new_order_message)

# Toon bestaande orders met automatische verversing
st.write("### Existing Orders")
orders_placeholder = st.empty()

while True:
    orders_df = get_orders()
    orders_placeholder.dataframe(orders_df)
    time.sleep(5)  # Ververs de tabel elke 5 seconden

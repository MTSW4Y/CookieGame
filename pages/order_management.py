import streamlit as st
import time
from database import get_orders
# from app import new_order_message

st.title('Order Management')

st.write("### Openstaande Orders")
orders_df = get_orders()
st.dataframe(orders_df)
st_autorefresh(interval=5000, key="order_refresh")

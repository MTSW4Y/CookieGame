import streamlit as st
from streamlit_autorefresh import st_autorefresh
from database import get_orders

st.title('Order Management')

st.write("### Openstaande Orders")
orders_df = get_orders()
st.dataframe(orders_df)
st_autorefresh(interval=5000, key="order_refresh")

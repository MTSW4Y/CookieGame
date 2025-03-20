import streamlit as st
from database import get_orders

st.title('Order Management')

# Toon bestaande orders
st.write("### Existing Orders")
orders_df = get_orders()
st.dataframe(orders_df)

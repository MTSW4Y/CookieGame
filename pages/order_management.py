import streamlit as st
from database import get_orders
from app import new_order_message


st.title('Order Management')

# Toon nieuwe order melding
if new_order_message:
    st.success(new_order_message)

# Toon bestaande orders
st.write("### Existing Orders")
orders_df = get_orders()
st.dataframe(orders_df)

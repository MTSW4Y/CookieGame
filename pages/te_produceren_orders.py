import streamlit as st
from streamlit_autorefresh import st_autorefresh
from database import get_orders

st.title('Order Management')

st_autorefresh(interval=5000, key="order_refresh")

st.write("### Dag en tijd")
st.write(f"##Dag {st.session_state.day_count} - Tijd: {st.session_state.current_time.strftime('%H:%M')}")

st.write("### Openstaande Orders")
orders_df = get_orders()
st.dataframe(orders_df)

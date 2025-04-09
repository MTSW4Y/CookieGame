import streamlit as st
from streamlit_autorefresh import st_autorefresh
from database import get_orders, get_simulation_time

st.title('🍪 - Openstaande orders')

st_autorefresh(interval=5000, key="order_refresh")

st.write(f"## Dag {st.session_state.day_count} - Tijd: {st.session_state.current_time.strftime('%H:%M')}")
st.write(get_simulation_time())

orders_df = get_orders()
st.dataframe(orders_df)

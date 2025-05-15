import streamlit as st
from streamlit_autorefresh import st_autorefresh
from database import get_orders

def start_timer():
  pass

def reset_timer():
  pass

st.title('Order Management')

st_autorefresh(interval=5000, key="order_refresh")

st.button('Start Timer', on_click=start_timer)
st.button('Reset', on_click=reset_timer)

st.write("### Dag en tijd")
st.write(f"Dag {st.session_state.day_count} - Tijd: {st.session_state.current_time.strftime('%H:%M')}")

st.write("### Openstaande Orders")
orders_df = get_orders()
st.dataframe(orders_df.reset_index(drop=True))

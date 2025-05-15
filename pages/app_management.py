import streamlit as st
import time
from datetime import datetime, timedelta
from streamlit_autorefresh import st_autorefresh
from database import get_orders, clear_orders, upsert_time, get_simulation_time, add_order
from orders import start_game, dag1, dag2, dag3, dag4

# def start_game():
#   add_order("Jumbo", 0, 8, 4)
#   add_order("AH", 0, 4, 2)
#   add_order("Jumbo", 0, 5, 3)
#   add_order("Hema", 2, 0, 4)

# def dag1():
#   add_order("Hema", 2, 3, 2)
  
# def dag2():
#   add_order("Jumbo", 0, 4, 3)
  
# def dag3():
#   add_order("AH", 0, 5, 2)
  
# def dag4():
#   add_order("Hema", 3, 0, 6)

# Timer settings
# dit is nodig om de timer te laten lopen
def start_timer():
    st.session_state.timer_running = True
    if st.session_state.start_time:
        pass
    else:
        st.session_state.start_time = time.time()

def reset_timer():
    st.session_state.day_count = 1
    st.session_state.start_time = None
    st.session_state.timer_running = False
    st.session_state.current_time = datetime.strptime('09:00', '%H:%M')
    clear_orders()
  
if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False
    st.session_state.day_count = 1
    st.session_state.current_time = datetime.strptime('09:00', '%H:%M')
    st.session_state.start_time = None
  
if st.session_state.timer_running:
    elapsed_real_time = time.time() - st.session_state.start_time
    elapsed_game_time = timedelta(seconds=elapsed_real_time * 120)  # 4 minuten = 8 uur
    st.session_state.current_time = datetime.strptime('09:00', '%H:%M') + elapsed_game_time

    if st.session_state.current_time.strftime('%H:%M') >= '17:00':
        st.session_state.day_count += 1
        st.session_state.current_time = datetime.strptime('09:00', '%H:%M')
        st.session_state.start_time = time.time()  # Reset de starttijd

st.title('App Management')

st_autorefresh(interval=1000, key="order_refresh")

col1, col2 = st.columns(2)

with col1:
    st.button('Start Timer', on_click=start_timer)

with col2:
    st.button('Reset Timer', on_click=reset_timer)

st.write(f"Dag {st.session_state.day_count} - Tijd: {st.session_state.current_time.strftime('%H:%M')}")
upsert_time(f"Dag {st.session_state.day_count} - Tijd: {st.session_state.current_time.strftime('%H:%M')}")

st.write("### Tijden")
st.write(get_simulation_time())

st.button('Start', on_click=start_game)
st.button('na dag 1', on_click=dag1)
st.button('na dag 2', on_click=dag2)
st.button('na dag 3', on_click=dag3)
st.button('na dag 4', on_click=dag4)

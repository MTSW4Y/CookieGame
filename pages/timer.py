import streamlit as st
import time
from datetime import datetime, timedelta
from streamlit_autorefresh import st_autorefresh
from database import get_orders, clear_orders
import threading

# Timer settings
if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False
    st.session_state.day_count = 1
    st.session_state.current_time = datetime.strptime('09:00', '%H:%M')
    st.session_state.start_time = None

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
    stop_event.set()
    order_thread.join()
    clear_orders()

# Update the timer
if st.session_state.timer_running:
    elapsed_real_time = time.time() - st.session_state.start_time
    elapsed_game_time = timedelta(seconds=elapsed_real_time * 120)  # 4 minuten = 8 uur
    st.session_state.current_time = datetime.strptime('09:00', '%H:%M') + elapsed_game_time

    if st.session_state.current_time.strftime('%H:%M') >= '17:00':
        st.session_state.day_count += 1
        st.session_state.current_time = datetime.strptime('09:00', '%H:%M')
        st.session_state.start_time = time.time()  # Reset de starttijd


CUSTOMERS = ['AH', 'Lidl', 'Jamin']

stop_event = threading.Event()

# def generate_random_order():
#     # while not stop_event.is_set():
#     while True:
#         customer = random.choice(CUSTOMERS)
#         stroopwafels = random.choice([0, 2, 4, 6])
#         prince_koeken = random.choice([0, 3, 6, 9])
#         orios = random.choice([0, 5, 10, 15, 20, 25])
#         add_order(customer, stroopwafels, prince_koeken, orios)
#         time.sleep(600)  # Wacht een minuut voordat een nieuwe order wordt toegevoegd

# order_thread = threading.Thread(target=generate_random_order, daemon=True)
# order_thread.start()

# Main app layout
st.title("Timer")

st_autorefresh(interval=1000, key="order_refresh")

col1, col2 = st.columns(2)

with col1:
    st.button('Start Timer', on_click=start_timer)

with col2:
    st.button('Reset Timer', on_click=reset_timer)

st.write(f"Dag {st.session_state.day_count} - Tijd: {st.session_state.current_time.strftime('%H:%M')}")

st.write("### Openstaande Orders")
orders_df = get_orders()
st.dataframe(orders_df)

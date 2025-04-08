import streamlit as st
import time

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

def stop_timer():
    st.session_state.timer_running = False

def reset_timer():
    st.session_state.day_count = 1
    st.session_state.start_time = None

# Update the timer
# if st.session_state.timer_running:
#     elapsed_real_time = time.time() - st.session_state.start_time
#     elapsed_game_time = timedelta(seconds=elapsed_real_time * 120)  # 4 minuten = 8 uur
#     st.session_state.current_time = datetime.strptime('09:00', '%H:%M') + elapsed_game_time

#     if st.session_state.current_time.strftime('%H:%M') >= '17:00':
#         st.session_state.day_count += 1
#         st.session_state.current_time = datetime.strptime('09:00', '%H:%M')
#         st.session_state.start_time = time.time()  # Reset de starttijd

# Main app layout
st.title("Timer")

st_autorefresh(interval=5000, key="order_refresh")

st.button('Start Timer', on_click=start_timer)
st.button('Stop Timer', on_click=stop_timer)
st.button('Reset Timer', on_click=reset_timer)

st.write(f"Dag {st.session_state.day_count} - Tijd: {st.session_state.current_time.strftime('%H:%M')}")

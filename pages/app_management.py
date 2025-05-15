import streamlit as st
import time
from datetime import datetime, timedelta
from streamlit_autorefresh import st_autorefresh
from database import get_orders, clear_orders, upsert_time, get_simulation_time, add_order

#########################TIMER############################

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

upsert_time(f"Dag {st.session_state.day_count} - Tijd: {st.session_state.current_time.strftime('%H:%M')}")
due_date = f"Dag {st.session_state.day_count+1} - Tijd: {st.session_state.current_time.strftime('%H:%M')}"

#########################ORDERS##################################

def start_game():
  add_order("Jumbo", due_date, 0, 8, 4)
  add_order("AH", due_date, 0, 4, 2)
  add_order("Jumbo", due_date, 0, 5, 3)
  add_order("Hema", due_date, 2, 0, 4)

def dag1():
  add_order("Hema", due_date, 2, 3, 2)
  
def dag2():
  add_order("Jumbo", due_date, 0, 4, 3)
  
def dag3():
  add_order("AH", due_date, 0, 5, 2)
  
def dag4():
  add_order("Hema", due_date, 3, 0, 6)

def bestel(klant, stroopwafel, oreo, prince):
  add_order("Hema", due_date, stroopwafel, oreo, prince)

#########################LAY-OUT##################################

st.title('App Management')

st_autorefresh(interval=1000, key="order_refresh")

col1, col2 = st.columns(2)

with col1:
    st.button('Start Timer', on_click=start_timer)

with col2:
    st.button('Reset Timer', on_click=reset_timer)

st.write("### Tijden")
st.write(get_simulation_time())

st.button('Startbestelling', on_click=start_game)
st.button('Bestelling dag 2', on_click=dag1)
st.button('Bestelling dag 3', on_click=dag2)
st.button('Bestelling dag 4', on_click=dag3)
st.button('Bestelling dag 5', on_click=dag4)

col3, col4 = st.columns(2)
    
with col3:
    stroopwafels = st.number_input("Vul het aantal stroopwafels in voor deze bestelling", min_value=0, max_value=10, step=1)
    oreos = st.number_input("Vul het aantal oreos in voor deze bestelling", min_value=0, max_value=10, step=1)
    prince_koeken = st.number_input("Vul het aantal prince koeken in voor deze bestelling", min_value=0, max_value=10, step=1)
    
with col4:
    klant = st.selectbox("Vul de klant in", ["Jumbo", "AH", "Hema"])
    st.button('Bestel', on_click=lambda: bestel(klant, stroopwafels, oreos, prince_koeken))
    # st.button('Bestel', on_click=dag4)

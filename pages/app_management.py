import streamlit as st
import time
from datetime import datetime, timedelta
from streamlit_autorefresh import st_autorefresh
from database import clear_orders, upsert_time, get_simulation_time, add_order, clear_ready_orders, clear_supplies, upsert_time, registrer_supplies
from orders import ronde_1, ronde_2, ronde_3, start_supplies

#########################ORDERS##################################

# dit moet ik nog even opslimmen..........

def schiet_eerste_order_in(orders):
    for order in orders:
        if order['Uur'] == st.session_state.last_hour:
            add_order(order['Klant'], f"Levermoment {order['Due']}", order['Stroopwafels'], order['Prince'], order['Penny_wafels'])
            
def schiet_nieuwe_orders_in(orders):
    for order in orders:
        if order['Uur'] == st.session_state.last_hour + 1:
            add_order(order['Klant'], f"Levermoment {order['Due']}", order['Stroopwafels'], order['Prince'], order['Penny_wafels'])

#########################TIMER############################

def start_timer(orders):
    st.session_state.timer_running = True
    if st.session_state.start_time:
        pass
    else:
        st.session_state.start_time = time.time()
        upsert_time(get_simulation_time(), row_id=2)
        schiet_eerste_order_in(orders)
        for groep in [1,2,3,4,5,6]:
            registrer_supplies(groep, **start_supplies)

def reset_game():
    del st.session_state.timer_running
    clear_orders()
    clear_ready_orders()
    clear_supplies()

if 'timer_running' not in st.session_state:
    st.session_state.start_time = None
    st.session_state.timer_running = False
    st.session_state.current_time = datetime.strptime('08:00', '%H:%M')
    st.session_state.last_hour = 8
    st.session_state.delivery_slot = 1
    st.session_state.timer_running = False
   
if st.session_state.timer_running:
    elapsed_real_time = time.time() - st.session_state.start_time
    # elapsed_game_time = timedelta(seconds=elapsed_real_time * 108)  # 5 minuten = 9 uur
    elapsed_game_time = timedelta(seconds=elapsed_real_time * 12)  # 5 minuten = 1 uur
    st.session_state.current_time = datetime.strptime('08:00', '%H:%M') + elapsed_game_time
    
    current_hour = st.session_state.current_time.hour
    if current_hour != st.session_state.last_hour:
        if current_hour != 12:
            st.session_state.delivery_slot += 1
            schiet_nieuwe_orders_in(st.session_state.orders)
        st.session_state.last_hour = current_hour

if st.session_state.last_hour == 12:
    upsert_time(f"Lunchpauze: {st.session_state.current_time.strftime('%H:%M')}")
else:
    upsert_time(f"Levermoment {st.session_state.delivery_slot}: {st.session_state.current_time.strftime('%H:%M')}")
due_date = f"Levermoment {st.session_state.delivery_slot+2}"
spoed_due_date = f"Levermoment {st.session_state.delivery_slot+1}"

#########################LAY-OUT##################################

st.title('App Management')

st_autorefresh(interval=1000, key="order_refresh")

selection = st.selectbox("Welke ronder wordt er gespeeld?", ["ronde 1", "ronde 2", "ronde 3"])

if selection == "ronde 1":
    st.session_state.orders = ronde_1
if selection == "ronde 2":
    st.session_state.orders = ronde_2
if selection == "ronde 3":
    st.session_state.orders = ronde_3

st.write(f"### {get_simulation_time()}")

col1, col2 = st.columns(2)

with col1:
    st.button('🕒 Start Timer', on_click=lambda: start_timer(st.session_state.orders))

with col2:
    st.button('🔴 Reset Game', on_click=reset_game)

st.write("### Spoed bestelling")

col5, col6 = st.columns(2)
    
with col5:
    stroopwafels = st.number_input("Vul het aantal stroopwafels in voor deze bestelling", min_value=0, max_value=10, step=1)
    penny_wafels = st.number_input("Vul het aantal penny wafels in voor deze bestelling", min_value=0, max_value=10, step=1)
    prince_koeken = st.number_input("Vul het aantal prince koeken in voor deze bestelling", min_value=0, max_value=10, step=1)
    
with col6:
    klant = st.selectbox("Vul de klant in", ["Jumbo", "AH", "Hema"])
    st.button('Bestel', on_click=lambda: add_order(klant, f"Levermoment {st.session_state.delivery_slot + 1}", stroopwafels, prince_koeken, penny_wafels))

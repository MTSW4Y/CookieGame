import streamlit as st
from database import add_order
st.title('Customers')
st.write('Hier kunnen de klanten straks hun orders gereedmelden en aangeven of ze compleet waren en of de kwaliteit voldoende was')



# add_order(customer, stroopwafels, prince_koeken, orios)

def start_game():
  add_order("Hema", 2, 2, 15)
  add_order("Jumbo", 2, 0, 3)
  add_order("AH", 3, 0, 2)
  add_order("Hema", 3, 3, 0)

def dag1():
  add_order("Hema", 2, 2, 15)

def dag2():
  add_order("Hema", 2, 2, 15)

def dag3():
  add_order("Hema", 2, 2, 15)

def dag4():
  add_order("Hema", 2, 2, 15)

st.button('Start', on_click=start_game)
st.button('na dag 1', on_click=dag1)
st.button('na dag 2', on_click=dag1)
st.button('na dag 3', on_click=dag1)
st.button('na dag 4', on_click=dag1)

import streamlit as st
from database import add_order
st.title('Customers')
st.write('Hier kunnen de klanten straks hun orders gereedmelden en aangeven of ze compleet waren en of de kwaliteit voldoende was')

# add_order(customer, stroopwafels, prince_koeken, orios)

def start_game():
  add_order("Jumbo", 0, 8, 4)
  add_order("AH", 0, 4, 2)
  add_order("Jumbo", 0, 5, 3)
  add_order("Hema", 2, 0, 4)

def dag1():
  add_order("Hema", 2, 3, 2)
  
def dag2():
  add_order("Jumbo", 0, 4, 3)
  
def dag3():
  add_order("AH", 0, 5, 2)
  
def dag4():
  add_order("Hema", 3, 0, 6)

def start_game():
  add_order("Hema", 2, 3, 2)
  add_order("Jumbo", 0, 4, 3)
  add_order("AH", 0, 5, 2)
  add_order("Hema", 3, 0, 6)




st.button('Start', on_click=start_game)
st.button('na dag 1', on_click=dag1)
st.button('na dag 2', on_click=dag1)
st.button('na dag 3', on_click=dag1)
st.button('na dag 4', on_click=dag1)

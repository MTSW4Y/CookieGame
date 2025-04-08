import streamlit as st
from database import add_order
st.title('Customers')
st.write('Hier kunnen de klanten straks hun orders gereedmelden en aangeven of ze compleet waren en of de kwaliteit voldoende was')

add_order("Patty", 1, 2, 3)

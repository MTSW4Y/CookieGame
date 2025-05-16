import streamlit as st

st.title('👤 - Klanten')

st.write("### Gereedmelden order")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("### Orderinfo")
    groep = st.number_input("Groepsnummer", step=1)
    ordernummer = st.number_input("Ordernummer", step=1)
    
with col2:
    st.write("### Geleverd")
    gel_aant_stroopwafels = st.number_input("Aantal stroopwafels", min_value=0, max_value=10, step=1)
    gel_aant_oreos = st.number_input("Aantal oreos", min_value=0, max_value=10, step=1)
    gel_aant_prince_koeken = st.number_input("Aantal prince koeken", min_value=0, max_value=10, step=1)

with col3:
    st.write("### Kwaliteit")
    kwal_stroopwafels = st.number_input("Goede stroopwafels", min_value=0, max_value=10, step=1)
    kwal_oreos = st.number_input("Goede oreos", min_value=0, max_value=10, step=1)
    kwal_prince_koeken = st.number_input("Goede prince koeken", min_value=0, max_value=10, step=1)

st.button('Registeer', on_click=lambda: bestel(klant, stroopwafels, oreos, prince_koeken))

import streamlit as st

def registreer(groep, ordernummer, gel_aant_stroopwafels, gel_aant_oreos, gel_aant_prince_koeken, kwal_stroopwafels, kwal_oreos, kwal_prince_koeken):
    pass

st.title('👤 - Klanten')

st.write("### Gereedmelden order")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("### Orderinfo")
    groep = st.number_input("Groepsnummer", step=1)
    ordernummer = st.number_input("Ordernummer", step=1)
    
with col2:
    pass

with col3:
    pass

st.button('Registeer', on_click=lambda: registreer(groep, ordernummer, gel_aant_stroopwafels, gel_aant_oreos, gel_aant_prince_koeken, kwal_stroopwafels, kwal_oreos, kwal_prince_koeken) )

import streamlit as st

st.title('👤 - Klanten')
st.write('Hier kunnen de klanten straks de inkomende orders en de kwaliteit registreren')

st.write("### iets?")

col1, col2, col3 = st.columns(3)

with col1:
    ordernummer = st.number_input("Vul hier het ordernummer in", step=1)
    groep = st.number_input("Vul hier het groepsnummer in", step=1)
    
with col2:
    gel_aant_stroopwafels = st.number_input("Vul het aantal geleverde stroopwafels in voor deze bestelling", min_value=0, max_value=10, step=1)
    gel_aant_oreos = st.number_input("Vul het aantal geleverde oreos in voor deze bestelling", min_value=0, max_value=10, step=1)
    gel_aant_prince_koeken = st.number_input("Vul het aantal geleverde prince koeken in voor deze bestelling", min_value=0, max_value=10, step=1)

with col3:
    kwal_stroopwafels = st.number_input("Vul het aantal geleverde stroopwafels in voor deze bestelling", min_value=0, max_value=10, step=1)
    kwal_oreos = st.number_input("Vul het aantal geleverde oreos in voor deze bestelling", min_value=0, max_value=10, step=1)
    kwal_prince_koeken = st.number_input("Vul het aantal geleverde prince koeken in voor deze bestelling", min_value=0, max_value=10, step=1)

st.button('Registeer', on_click=lambda: bestel(klant, stroopwafels, oreos, prince_koeken))

import streamlit as st
from database import add_ready_order, get_ready_orders

st.title('👤 - Klanten')

st.write("### Kwaliteitscontrole")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("### Orderinfo")
    groep = st.number_input("Groepsnummer", step=1)
    ordernummer = st.number_input("Ordernummer", step=1)
    
with col2:
    st.write("### Geleverd")
    gel_aant_stroopwafels = st.number_input("Aantal stroopwafels", step=1)
    gel_aant_prince_koeken = st.number_input("Aantal prince koeken", step=1)
    gel_aant_penny_wafels = st.number_input("Aantal penny wafels", step=1)

with col3:
    st.write("### Kwaliteit")
    kwal_stroopwafels = st.number_input("Goede stroopwafels", step=1, value=gel_aant_stroopwafels)
    kwal_prince_koeken = st.number_input("Goede prince koeken", step=1, value=gel_aant_prince_koeken)
    kwal_penny_wafels = st.number_input("Goede penny wafels", step=1, value=gel_aant_penny_wafels)

st.write("Geef hier aan welke groepen feedback hebben gevraagd:")
cols = st.columns(6)
groep_feedback = {}
for i, col in enumerate(cols):
    groep_feedback[i+1] = col.checkbox(f'Groep {i + 1}')

reject_reason = ""
if gel_aant_stroopwafels != kwal_stroopwafels or gel_aant_prince_koeken != kwal_prince_koeken or gel_aant_penny_wafels != kwal_penny_wafels:
    if groep_feedback[groep]:
        st.write(f"**Er zijn kwaliteitsissues bij groep {groep} en ze willen graag feedback**")
        reject_reason = st.selectbox("Wat is de reden voor de afkeur:", ["Vulling zichtbaar", "Lagen los", "Afwijking in vorm", "Verkeerde pakbon", "Overig"])
    else:
        st.write(f"**Er zijn kwaliteitsissues bij groep {groep}**")

if st.button('Registeer', on_click=lambda: add_ready_order(ordernummer, groep, gel_aant_stroopwafels, gel_aant_prince_koeken, gel_aant_penny_wafels, kwal_stroopwafels, kwal_prince_koeken, kwal_penny_wafels, reject_reason)):
    st.toast("Kwaliteit geregistreerd", icon="✅")

st.dataframe(get_ready_orders(), hide_index=True)

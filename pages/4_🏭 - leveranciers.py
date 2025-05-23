import streamlit as st
from database import add_supply, get_supplies

def registreer(groep, gel_aant_stroopwafels_vul, gel_aant_prince_koeken_vul, gel_aant_pennywafels_vul, gel_aant_stroopwafels_buit, gel_aant_prince_koeken_buit, gel_aant_pennywafels_buit):
    add_supply(groep, 'stroopwafel', 'vulling', gel_aant_stroopwafels_vul)
    add_supply(groep, 'princekoeken', 'vulling', gel_aant_prince_koeken_vul)
    add_supply(groep, 'pennywafels', 'vulling', gel_aant_pennywafels_vul)
    add_supply(groep, 'stroopwafel', 'koekje', gel_aant_stroopwafels_buit)
    add_supply(groep, 'princekoeken', 'koekje', gel_aant_prince_koeken_buit)
    add_supply(groep, 'pennywafels', 'koekje', gel_aant_pennywafels_buit)
    add_supply(groep, 'bakjes', 'rest', gel_aant_bakjes)

st.title('🏭 - Leveranciers')

st.write("### Uitgifte materialen")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("### Groep")
    groep = st.number_input("Groepsnummer", step=1)
    gel_aant_bakjes = st.number_input("Aantal bakjes", step=1)
    
with col2:
    st.write("### Vulling")
    gel_aant_stroopwafels_vul = st.number_input("Aantal stroopwafelvulling", step=1)
    gel_aant_prince_koeken_vul = st.number_input("Aantal princevulling", step=1)
    gel_aant_pennywafels_vul = st.number_input("Aantal pennywafelvulling", step=1)

with col3:
    st.write("### Buitenkant")
    gel_aant_stroopwafels_buit = st.number_input("Aantal stroopwafel-buitenkanten", step=1, value=gel_aant_stroopwafels_vul*2)
    gel_aant_prince_koeken_buit = st.number_input("Aantal prince koek-buitenkanten", step=1, value=gel_aant_prince_koeken_vul*2)
    gel_aant_pennywafels_buit = st.number_input("Aantal pennywafel-buitenkanten", step=1, value=gel_aant_pennywafels_vul*2)

if st.button('Registeer', on_click=lambda: registreer(groep, gel_aant_stroopwafels_vul, gel_aant_prince_koeken_vul, gel_aant_pennywafels_vul, gel_aant_stroopwafels_buit, gel_aant_prince_koeken_buit, gel_aant_pennywafels_buit)):
    st.toast("Inkoop geregistreerd", icon="✅")

st.dataframe(get_supplies(), hide_index=True)

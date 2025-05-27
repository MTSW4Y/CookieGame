import streamlit as st
from database import add_supply, get_supplies, delete_supply_by_id

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
    gel_aant_stroopwafels_vul = st.number_input("Aantal 1004 (stroop)", step=1)
    gel_aant_prince_koeken_vul = st.number_input("Aantal 1005 (princecrème)", step=1)
    gel_aant_pennywafels_vul = st.number_input("Aantal 1006 (pennycholcolade)vulling", step=1)

with col3:
    st.write("### Buitenkant")
    gel_aant_stroopwafels_buit = st.number_input("Aantal 1001 (stroopwafel deeg)", step=1, value=gel_aant_stroopwafels_vul*2)
    gel_aant_prince_koeken_buit = st.number_input("Aantal 1002 (princekoek deeg)", step=1, value=gel_aant_prince_koeken_vul*2)
    gel_aant_pennywafels_buit = st.number_input("Aantal 1003 (pennywafeldeeg)", step=1, value=gel_aant_pennywafels_vul*2)

if st.button('Registeer', on_click=lambda: registreer(groep, gel_aant_stroopwafels_vul, gel_aant_prince_koeken_vul, gel_aant_pennywafels_vul, gel_aant_stroopwafels_buit, gel_aant_prince_koeken_buit, gel_aant_pennywafels_buit)):
    st.toast("Inkoop geregistreerd", icon="✅")

supplies = get_supplies()
st.dataframe( supplies, hide_index=True)

col4, col5 = st.columns(2)

with col4:
    selected_id = st.number_input("Vul ID in om te verwijderen:")

with col5:
    if st.button("Verwijder regel"):
        delete_supply_by_id(selected_id)
        st.toast("Regel verwijderd", icon="✅")
        html('<script>parent.window.location.reload();</script>')

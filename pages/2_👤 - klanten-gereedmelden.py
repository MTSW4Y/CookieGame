import streamlit as st

def registreer(groep, ordernummer):
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

# st.button('Registeer', on_click=lambda: registreer(groep, ordernummer))

# if st.button('Registeer'):
#     st.toast("✔️ Opgeslagen!", icon="✅")


if st.button('Registeer', on_click=lambda: registreer(groep, ordernummer)):
    st.toast("✔️ Opgeslagen!", icon="✅")

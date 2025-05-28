import streamlit as st
from database import add_ready_order, get_ready_orders

st.title('👤 - Klanten')

st.write("### Gereedmelden order")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("### Orderinfo")
    groep = st.number_input("Groepsnummer", step=1)
    ordernummer = st.number_input("Ordernummer", step=1)
    
# with col2:
#     pass

# with col3:
#     pass

if st.button('Registeer', on_click=lambda: add_ready_order(ordernummer, groep, "", "", "", "", "", "")):
    st.toast("Order gereedgemeld", icon="✅")

orders_df = get_ready_orders()
st.dataframe(orders_df.iloc[:, :4], hide_index=True)

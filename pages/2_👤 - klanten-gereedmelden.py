import streamlit as st
from database import add_ready_order, get_ready_orders, get_simulation_time()

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


if st.button('Registeer', on_click=lambda: add_ready_order(ordernummer, groep, get_simulation_time(), "", "", "", "", "", "")):
    st.toast("Order gereedgemeld", icon="✅")

# add_ready_order(order_no, group_no, del_date, del_stroopwafels, del_prince_koeken, del_orios, q_del_stroopwafels, q_del_prince_koeken, q_del_orios)

orders_df = get_ready_orders()
st.dataframe(orders_df)

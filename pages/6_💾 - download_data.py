import streamlit as st
import sqlite3
import json
from io import BytesIO
from database import delete_supply_by_id

DB_PATH = 'central_database.db'

# Functie om alle data uit de database op te halen
def fetch_all_data():
    data = {}
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        tables = ['orders', 'ready_orders', 'supplies', 'time']
        for table in tables:
            cursor.execute(f"SELECT * FROM {table}")
            columns = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            data[table] = [dict(zip(columns, row)) for row in rows]
    return data

# Streamlit interface
st.title("📦 Data bekijken, editen en downloaden")

col4, col5, col6 = st.columns(3)

with col4:
    st.write("Verwijderen supplies")
    selected_id = st.number_input("Vul ID in om te verwijderen:", step=1)
    if st.button("Verwijder regel"):
        delete_supply_by_id(selected_id)
        st.toast(f"Supply met id {selected_id} verwijderd", icon="✅")

with col5:
    if st.button("Verwijder regel"):
        delete_supply_by_id(selected_id)
        st.toast("Regel verwijderd", icon="✅")


# Ophalen van data
data = fetch_all_data()

# Downloadknop voor JSON-bestand
json_data = json.dumps(data, indent=4)
buffer = BytesIO(json_data.encode('utf-8'))

st.download_button(
    label="⬇️ Download database als JSON",
    data=buffer,
    file_name="database_dump.json",
    mime="application/json"
)

# Tonen van JSON op de pagina
st.subheader("📄 JSON-weergave van database")
st.json(data)

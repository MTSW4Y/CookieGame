import streamlit as st
import pandas as pd
import time

# Sla logs en dynamische knoppen op in session state
if 'logs' not in st.session_state:
    st.session_state.logs = []

if 'dynamic_buttons' not in st.session_state:
    st.session_state.dynamic_buttons = {}

# Functie om een timestamp toe te voegen
def log_action(action):
    st.session_state.logs.append({'Action': action, 'Timestamp':  time.time()})

# UI Titel
st.title("🕰️ Koekjesgame Module 4")

col1, col2, col3 = st.columns(3)

# Dynamische knoppen toevoegen
st.subheader("➕ Voeg knoppen toe om tijd mee te registreren")

# Inputvelden voor nieuwe knop
new_button_name = st.text_input("Naam van de knop:")
add_button = st.button("Voeg Knop Toe")

if add_button and new_button_name:
    st.session_state.dynamic_buttons[new_button_name] = new_button_name
    log_action(f"Knop '{new_button_name}' toegevoegd")

# 📝 Weergeven van dynamische knoppen
if st.session_state.dynamic_buttons:
    st.divider()
    st.subheader("🎛️ Dynamisch Bedieningspaneel")
    
    dynamic_cols = st.columns(3)
    for i, (button_name, button_color) in enumerate(st.session_state.dynamic_buttons.items()):
        col = dynamic_cols[i % 3]
        if col.button(button_name, use_container_width=True, key=button_name):
            log_action(button_name)

# 📜 Toon logs in een tabel als er gegevens zijn
st.divider()
st.subheader("📜 Logs")

if st.session_state.logs:
    df = pd.DataFrame(st.session_state.logs)

    # Maak de tabel bewerkbaar
    edited_df = st.data_editor(df, num_rows="dynamic", key="editable_logs")

    # Update de session_state met de aangepaste data
    st.session_state.logs = edited_df.to_dict(orient='records')

    # Download knop voor de aangepaste logs
    csv = edited_df.to_csv(index=False).encode('utf-8')
    st.download_button("💾 Download Logs als CSV", csv, "logs.csv", "text/csv")
    

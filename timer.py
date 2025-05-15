# import time
# from datetime import datetime, timedelta
# from streamlit_autorefresh import st_autorefresh
# from database import get_orders, clear_orders, upsert_time, get_simulation_time, add_order

# # Timer settings
# # dit is nodig om de timer te laten lopen
# def start_timer():
#     st.session_state.timer_running = True
#     if st.session_state.start_time:
#         pass
#     else:
#         st.session_state.start_time = time.time()

# def reset_timer():
#     st.session_state.day_count = 1
#     st.session_state.start_time = None
#     st.session_state.timer_running = False
#     st.session_state.current_time = datetime.strptime('09:00', '%H:%M')
#     clear_orders()
  
# if 'timer_running' not in st.session_state:
#     st.session_state.timer_running = False
#     st.session_state.day_count = 1
#     st.session_state.current_time = datetime.strptime('09:00', '%H:%M')
#     st.session_state.start_time = None
  
# if st.session_state.timer_running:
#     elapsed_real_time = time.time() - st.session_state.start_time
#     elapsed_game_time = timedelta(seconds=elapsed_real_time * 120)  # 4 minuten = 8 uur
#     st.session_state.current_time = datetime.strptime('09:00', '%H:%M') + elapsed_game_time

#     if st.session_state.current_time.strftime('%H:%M') >= '17:00':
#         st.session_state.day_count += 1
#         st.session_state.current_time = datetime.strptime('09:00', '%H:%M')
#         st.session_state.start_time = time.time()  # Reset de starttijd

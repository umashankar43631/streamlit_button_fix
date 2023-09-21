import streamlit as st

# For Multiple Pages we use this session state
def initialize_session_state():
    return {'screen1': True, 'screen2': False}

def update_screen1():
    st.session_state.screen1 = True 
    st.session_state.screen2 = False

def update_screen2():
    st.session_state.screen1 = False 
    st.session_state.screen2 = True

# Initialize session state
if 'screen1' not in list(st.session_state.keys()):
    st.session_state.screen1 = True 
    st.session_state.screen2 = False
if st.session_state.screen1 == True:
    st.write("Hello World")
    graphical_ui = st.sidebar.button("Graphical UI", on_click=update_screen2)

elif st.session_state.screen2 == True:
    show_bar = st.checkbox("Show Bar Chart")
    show_line = st.checkbox("Show Line Chart")
    show_scatter = st.checkbox("Show Scatter Plot")
    normal_ui = st.sidebar.button("Analytics UI", on_click=update_screen1)
        # normal_ui = False
    if show_bar:
        st.write("its Bar chart")
    if show_line:
        st.write("its a line")
    if show_scatter:
        st.write("its a Scatter Plot")

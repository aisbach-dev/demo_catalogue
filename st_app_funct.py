import streamlit as st


def init_session_state():
    session_state_dict = {'user_email_collected': None,
                          'error_invalid_email': False,
                          'menu_current_page': None}

    # load default values into session state
    for key, val in session_state_dict.items():
        if key not in st.session_state:
            st.session_state[key] = val
        elif key in st.session_state:
            st.session_state.key = val

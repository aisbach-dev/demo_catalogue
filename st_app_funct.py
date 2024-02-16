# AISBACH Data Solutions DEMO App (Streamlit) - Implemented by Stefan Rummer, 2024

import os
import streamlit as st


# TODO turn this into universal config for app names and pages
page_name_mapping = {'app_page_demo1': 'Demo App 1',
                     'app_page_demo2': 'Demo App 2',
                     'app_page_demo3': 'Demo App 3',
                     'app_page_demo4': 'Demo App 4',
                     'app_page_demo5': 'Demo App 5',
                     'app_page_demo6': 'Demo App 6',
                     '': 'Welcome Info'}


def init_session_state():

    # TODO EFFECT of calling this function:

    #   IF the session state variables are already init. and loaded
    #   (due to calling the function before) nothing happens upon re-trigger

    #   IF the page is reloaded and hence all session state variables
    #   are cleared due to the cache being emptied during reload, this
    #   function adds the session state variables again, loads the init
    #   values and checks which page the code is being executed on
    #   --> eventually updates the page to be the right subdomain


    session_state_dict = {'user_email_collected': None,
                          'error_invalid_email': False,
                          'menu_current_page': "Welcome Info"}

    # load default values into session state
    for key, val in session_state_dict.items():
        if key not in st.session_state:
            st.session_state[key] = val
        elif key in st.session_state:
            st.session_state.key = val

    # in case of page re-load, make sure that all session variables are re-initialized
    # and that st.session_state.menu_current_page is set to the page that the user has
    # reloaded (not the default init page "Welcome Info")
    # url = st_javascript("await fetch('').then(r => window.parent.location.href)")
    # if isinstance(url, str):  # Check if the type of url is a string
    #     index = url.rfind('/')  # finds the last occurrence of "/" in the string
    #     page_id = url[index + 1:]  # select the string after the last "/"
    #     st.session_state.menu_current_page = page_name_mapping[page_id]


def page_switch():

    # TODO again mapping case PAGE NAME (from Menu) --> .py FILE PATH

    # loads the page as stored in the session state variable
    if st.session_state.menu_current_page == "Welcome Info":
        path = os.path.relpath("st_app_main.py")
        st.switch_page(str(path))
    elif st.session_state.menu_current_page == "Demo App 1":
        path = os.path.relpath("pages/app_page_demo1.py")
        st.switch_page(str(path))
    elif st.session_state.menu_current_page == "Demo App 2":
        path = os.path.relpath("pages/app_page_demo2.py")
        st.switch_page(str(path))
    elif st.session_state.menu_current_page == "Demo App 3":
        path = os.path.relpath("pages/app_page_demo3.py")
        st.switch_page(str(path))
    elif st.session_state.menu_current_page == "Demo App 4":
        path = os.path.relpath("pages/app_page_demo4.py")
        st.switch_page(str(path))
    elif st.session_state.menu_current_page == "Demo App 5":
        path = os.path.relpath("pages/app_page_demo5.py")
        st.switch_page(str(path))
    elif st.session_state.menu_current_page == "Demo App 6":
        path = os.path.relpath("pages/app_page_demo6.py")
        st.switch_page(str(path))
    else:  # if nothing is selected then return to landing page
        path = os.path.relpath("st_app_main.py")
        st.switch_page(str(path))


def callback_return_button():
    st.session_state.menu_current_page = 'Welcome Info'

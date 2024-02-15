# AISBACH Data Solutions DEMO App (Streamlit) - Implemented by Stefan Rummer, 2024

import os
import streamlit as st
import streamlit_float  # recommended
import streamlit_antd_components as sac
from streamlit_javascript import st_javascript

from st_app_design import apply_design
from st_app_design import footer_main
from st_app_design import app_top_navbar
from st_app_design import add_spacer


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
                          'menu_current_page': "Welcome Info",
                          'welcome_page_selected': None,
                          'welcome_page_triggered': False,
                          'image_click_coordinates':
                              {'img1': None,
                               'img2': None,
                               'img3': None,
                               'img4': None,
                               'img5': None,
                               'img6': None}}

    # load default values into session state
    for key, val in session_state_dict.items():
        if key not in st.session_state:
            st.session_state[key] = val
        elif key in st.session_state:
            st.session_state.key = val

    # in case of page re-load, make sure that all session variables are re-initialized
    # and that st.session_state.menu_current_page is set to the page that the user has
    # reloaded (not the default init page "Welcome Info")
    url = st_javascript("await fetch('').then(r => window.parent.location.href)")
    if isinstance(url, str):  # Check if the type of url is a string
        index = url.rfind('/')  # finds the last occurrence of "/" in the string
        page_id = url[index + 1:]  # select the string after the last "/"
        st.session_state.menu_current_page = page_name_mapping[page_id]


def page_switch():

    # loads the page as stored in the session state variable

    if st.session_state.menu_current_page == "Demo App 1":
        path = os.path.relpath("pages/app_page_demo1.py")
        st.switch_page(str(path))
    if st.session_state.menu_current_page == "Demo App 2":
        path = os.path.relpath("pages/app_page_demo2.py")
        st.switch_page(str(path))
    if st.session_state.menu_current_page == "Demo App 3":
        path = os.path.relpath("pages/app_page_demo3.py")
        st.switch_page(str(path))
    if st.session_state.menu_current_page == "Demo App 4":
        path = os.path.relpath("pages/app_page_demo4.py")
        st.switch_page(str(path))
    if st.session_state.menu_current_page == "Demo App 5":
        path = os.path.relpath("pages/app_page_demo5.py")
        st.switch_page(str(path))
    if st.session_state.menu_current_page == "Demo App 6":
        path = os.path.relpath("pages/app_page_demo6.py")
        st.switch_page(str(path))
    else:  # if nothing is selected then return to landing page
        path = os.path.relpath("st_app_main.py")
        st.switch_page(str(path))


def build_sidebar_menu():

    # TODO what does this do, do we actually need this --> research ?
    streamlit_float.float_init(include_unstable_primary=False)

    with st.sidebar:

        st.image('img/aisbach_logo_rounded.png')

        # source and documentation for this menu custom component
        # https://nicedouble-streamlitantdcomponentsdemo-app-middmy.streamlit.app/

        # fetch this insight so that the right item is colored and selected in the menu
        menu_current_page = st.session_state.menu_current_page
        mapping_selected_index = {'Welcome Info': 1,
                                  'Demo App 1': 3,
                                  'Demo App 2': 4,
                                  'Demo App 3': 5,
                                  'Demo App 4': 6,
                                  'Demo App 5': 7,
                                  'Demo App 6': 8}

        menu_choice = sac.menu([
            sac.MenuItem(type='divider'),
            sac.MenuItem('Welcome Info', icon='house-fill'),
            sac.MenuItem(type='divider'),
            sac.MenuItem('Demo App 1', icon='bar-chart-fill'),
            sac.MenuItem('Demo App 2', icon='bar-chart-fill'),
            sac.MenuItem('Demo App 3', icon='bar-chart-fill'),
            sac.MenuItem('Demo App 4', icon='bar-chart-fill'),
            sac.MenuItem('Demo App 5', icon='bar-chart-fill'),
            sac.MenuItem('Demo App 6', icon='bar-chart-fill'),
            sac.MenuItem(type='divider'),
            sac.MenuItem('About AISBACH', icon='info-circle-fill', children=[
                sac.MenuItem('Website', icon='browser-safari', href='https://www.aisbach.com'),
                sac.MenuItem('Linkedin', icon='linkedin', href='https://www.linkedin.com/company/aisbach'),
                sac.MenuItem('Contact', icon='envelope-fill', href='https://www.aisbach.com/#contact'),
                sac.MenuItem('Imprint', icon='file-earmark-medical-fill', href='https://www.aisbach.com/imprint'),
                sac.MenuItem('GDPR', icon='database-fill-check', href='https://www.aisbach.com/data-policy')
            ]),
            sac.MenuItem(type='divider')
        ], open_all=False, color="#16C89D", variant='light', size=16, index=mapping_selected_index[menu_current_page])


        # if user clicks menu item, load selected page into session state variable
        if st.session_state.menu_current_page != menu_choice and menu_choice!= "":
            st.session_state.menu_current_page = menu_choice
            page_switch()  # trigger switching process


def launch_page(page_build_function, page_title='TITLE', page_description=''):

    # initial page setup
    apply_design()
    init_session_state()
    build_sidebar_menu()

    # create header section
    app_top_navbar()
    st.divider()
    title_cols = st.columns([1, 1])
    with title_cols[0]:
        st.title(page_title)
    with title_cols[1]:
        add_spacer(1)
        st.write(page_description)
    st.divider()

    # load app content
    container_top = st.empty()  # build placeholder page in empty container
    container_top.markdown("<br>" * 2, unsafe_allow_html=True)
    with st.spinner('Loading app data ...'):  # have a spinner wrap this entire process
        container = st.empty()  # build placeholder page in empty container
        container.markdown("<br>" * 1000, unsafe_allow_html=True)
        page_build_function()  # build actual page below the white container
        container.empty()  # Clear the container once the page is built
        container_top.empty()


    footer_main()

import os
import streamlit as st
import streamlit_float  # recommended
import streamlit_antd_components as sac
from streamlit_javascript import st_javascript


page_name_mapping = {'app_page_demo1': 'Demo App 1',
                     'app_page_demo2': 'Demo App 2',
                     'app_page_demo3': 'Demo App 3',
                     'app_page_demo4': 'Demo App 4',
                     'app_page_demo5': 'Demo App 5',
                     'app_page_demo6': 'Demo App 6',
                     '': 'Welcome Info'}


def init_session_state():
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
                               'img6': None}
                          }

    # load default values into session state
    for key, val in session_state_dict.items():
        if key not in st.session_state:
            st.session_state[key] = val
        elif key in st.session_state:
            st.session_state.key = val


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

    streamlit_float.float_init(include_unstable_primary=False)

    # in case of page re-load, make sure that all session variables are re-initialized
    # and that st.session_state.menu_current_page is set to the page that the user has
    # reloaded (not the default init page "Welcome Info")
    init_session_state()

    url = st_javascript("await fetch('').then(r => window.parent.location.href)")
    # Check if the type of url is a string
    if isinstance(url, str):
        index = url.rfind('/')
        page_id = url[index + 1:]
        st.session_state.menu_current_page = page_name_mapping[page_id]
        # if page_id == None or page_id == '':
        #     st.write(page_name_mapping[''])
        # else:
        #     st.write(page_name_mapping[page_id])
        #     st.session_state.menu_current_page = page_name_mapping[page_id]


    with st.sidebar:

        st.image('img/aisbach_logo_rounded.png')

        menu_choice = sac.menu([
            sac.MenuItem(type='divider'),
            sac.MenuItem('Welcome Info', icon='house-fill'),
            sac.MenuItem(type='divider'),
            sac.MenuItem('Demo Products', icon='box-fill', children=[
                sac.MenuItem('Demo App 1', icon='bar-chart-fill'),
                sac.MenuItem('Demo App 2', icon='bar-chart-fill'),
                sac.MenuItem('Demo App 3', icon='bar-chart-fill'),
                sac.MenuItem('Demo App 4', icon='bar-chart-fill'),
                sac.MenuItem('Demo App 5', icon='bar-chart-fill'),
                sac.MenuItem('Demo App 6', icon='bar-chart-fill'),
            ]),
            sac.MenuItem(type='divider'),
            sac.MenuItem('About AISBACH', icon='info-square-fill', children=[
                sac.MenuItem('Website', icon='browser-safari', href='https://www.aisbach.com'),
                sac.MenuItem('Linkedin', icon='linkedin', href='https://www.linkedin.com/company/aisbach'),
                sac.MenuItem('Contact', icon='envelope-fill', href='https://www.aisbach.com/#contact'),
                sac.MenuItem('Imprint', icon='file-earmark-medical-fill', href='https://www.aisbach.com/imprint'),
                sac.MenuItem('GDPR', icon='database-fill-check', href='https://www.aisbach.com/data-policy'),
            ]),
            sac.MenuItem(type='divider'),
        ], open_all=False, color="black", size=16)

        # if user clicks menu item, load selected page into session state variable
        if st.session_state.menu_current_page != menu_choice and menu_choice!= "":
            st.session_state.menu_current_page = menu_choice
            page_switch()  # trigger switching process

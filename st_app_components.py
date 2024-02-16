# AISBACH Data Solutions DEMO App (Streamlit) - Implemented by Stefan Rummer, 2024

import streamlit as st
import streamlit_float
import streamlit_antd_components as sac
from htbuilder import HtmlElement, div, br, hr, a, p, styles
from htbuilder.units import percent, px

from st_app_funct import callback_return_button
from st_app_funct import init_session_state
from st_app_funct import page_switch

from st_app_design import apply_design
from st_app_design import add_spacer


def link(link_, text, color, **style):
    return a(_href=link_, _target="_blank", style=styles(**style, color=color))(text)


def layout(*args):
    style = """<style>
        # MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>"""

    body = p()
    style_div = styles(left=0, bottom=0, margin=px(0, 0, 0, 0),
                       width=percent(100), text_align="center",
                       height="60px", opacity=1, color="grey")
    foot = div(style=style_div)(hr(style=styles()), body)
    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)
        elif isinstance(arg, HtmlElement):
            body(arg)

    st.caption(str(foot), unsafe_allow_html=True)


def build_footer_main():

    myargs = ["Implemented by ",
              link("https://www.aisbach.com", "AISBACH Data Solutions UG", 'black'),
              br(), "© 2024, all rights reserved "]
    layout(*myargs)


def build_footer_sidebar():

    myargs = [link("https://www.aisbach.com/", "AISBACH", 'grey'),
              ", founded June 2023", br(), "[AI Use Case Demo]"]
    layout(*myargs)


def build_top_navbar():

    # display navbar on top of app page
    nav_cols = st.columns([1, 1])
    with nav_cols[0]:
        # callback making to update session state before triggering page switch (incl. page rerun/load)
        if st.button('⬅  **Return to Overview**', on_click=callback_return_button):
            st.write('return button clicked')
            st.switch_page('st_app_main.py')

    with nav_cols[1]:
        sac.buttons([
            sac.ButtonsItem(icon='envelope-fill', href='https://www.aisbach.com/#contact', color='#25C3B0'),
            sac.ButtonsItem(icon='linkedin', href='https://www.linkedin.com/company/aisbach', color='#25C3B0'),
            sac.ButtonsItem(icon='globe2', color='black', disabled=False)
        ], align='end', index=2, key='weblinks')



def build_sidebar_menu():

    # TODO what does this do, do we actually need this --> research ?
    streamlit_float.float_init(include_unstable_primary=False)

    with st.sidebar:

        st.image('img/aisbach_logo_rounded.png')

        # source and documentation for this menu custom component
        # https://nicedouble-streamlitantdcomponentsdemo-app-middmy.streamlit.app/

        # TODO mapping: PAGE NAME (from sidebar menu) --> MENU ITEM INDEX
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
        if st.session_state.menu_current_page != menu_choice and menu_choice != "":
            st.session_state.menu_current_page = menu_choice
            page_switch()  # trigger switching process


def launch_page(page_build_function, page_title='TITLE', page_description=''):

    # initial page setup
    apply_design()
    init_session_state()
    build_sidebar_menu()

    # create header section
    build_top_navbar()
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

    build_footer_main()

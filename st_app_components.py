# AISBACH Data Solutions DEMO App (Streamlit) - Implemented by Stefan Rummer, 2024

import streamlit as st
from typing import Callable
import streamlit_antd_components as sac
from htbuilder import HtmlElement, div, br, hr, a, p, styles
from htbuilder.units import percent, px

# import backend processing functions
from st_app_funct import callback_return_button
from st_app_funct import callback_collect_user_email
from st_app_funct import init_session_state
from st_app_funct import wrapper_loading_process
from st_app_funct import page_switch

# import design override functions
from st_app_design import apply_design
from st_app_design import add_spacer
from st_app_design import custom_message_box


def build_footer_main():

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

    myargs = ["Implemented by ",
              a(_href="https://www.aisbach.com",
                _target="_blank",
                style=styles(color='black'))("AISBACH Data Solutions UG"),
              br(), "© 2024, all rights reserved "]

    for arg in myargs:
        if isinstance(arg, str):
            body(arg)
        elif isinstance(arg, HtmlElement):
            body(arg)

    st.caption(str(foot), unsafe_allow_html=True)


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
            sac.ButtonsItem(icon='envelope-fill', href='https://www.aisbach.com/#contact', color='#16C89D'),
            sac.ButtonsItem(icon='linkedin', href='https://www.linkedin.com/company/aisbach', color='#16C89D'),
            sac.ButtonsItem(icon='globe2', href='https://www.aisbach.com', color='black')
        ], align='end', index=2, key='weblinks')


def build_sidebar_menu():

    with st.sidebar:

        st.image('img/aisbach_logo_rounded.png')
        add_spacer(1)

        # source and documentation for this menu custom component
        # https://nicedouble-streamlitantdcomponentsdemo-app-middmy.streamlit.app/

        # TODO mapping: PAGE NAME (from sidebar menu) --> MENU ITEM INDEX
        # fetch this insight so that the right item is colored and selected in the menu
        menu_current_page = st.session_state.menu_current_page
        mapping_selected_index = {'Welcome Info': 0,
                                  'Demo App 1': 2,
                                  'Demo App 2': 3,
                                  'Demo App 3': 4,
                                  'Demo App 4': 5}

        menu_choice = sac.menu([
            sac.MenuItem('Welcome Info', icon='house-fill'),
            sac.MenuItem(type='divider'),
            sac.MenuItem('Demo App 1', icon='bar-chart-fill'),
            sac.MenuItem('Demo App 2', icon='bar-chart-fill'),
            sac.MenuItem('Demo App 3', icon='bar-chart-fill'),
            sac.MenuItem('Demo App 4', icon='bar-chart-fill'),
            sac.MenuItem(type='divider'),
            sac.MenuItem('About AISBACH', icon='info-circle-fill', children=[
                sac.MenuItem('Website', icon='browser-safari', href='https://www.aisbach.com'),
                sac.MenuItem('Linkedin', icon='linkedin', href='https://www.linkedin.com/company/aisbach'),
                sac.MenuItem('Contact', icon='envelope-fill', href='https://www.aisbach.com/#contact'),
                sac.MenuItem('Imprint', icon='file-earmark-medical-fill', href='https://www.aisbach.com/imprint'),
                sac.MenuItem('GDPR', icon='database-fill-check', href='https://www.aisbach.com/data-policy')
            ])
        ], open_all=False, color="black", variant='filled', size=16, index=mapping_selected_index[menu_current_page])


        # if user clicks menu item, load selected page into session state variable
        if st.session_state.menu_current_page != menu_choice and menu_choice != "":
            st.session_state.menu_current_page = menu_choice
            page_switch()  # trigger switching process


def build_email_funnel():

    # set custom background image for the given page
    # image is fetched from url (GitHub repo) TODO how to source locally (from deployment?)
    # set_bg_hack_url()

    st.container(height=50, border=False)

    cols = st.columns([0.5, 1, 0.5])
    with cols[1]:

        with st.expander("Disclaimer & Access", expanded=True):

            input_mail = st.text_input('please enter your email address')
            # input_consent = st.checkbox('By clicking the button below I consent to AISBACH storing my email
            # address for user analytics purposes, tracking which demo apps I have accessed and eventually contacting
            # me for further questioning or marketing purposes via the entered email address.')

            st.caption(" By clicking \"Access Demo App Now\" you accept AISBACH's"
                       " [Terms of Service](https://tenderport.tilda.ws/terms-and-conditions) and"
                       " [Data Privacy Policy](https://tenderport.tilda.ws/privacy-policy).")

            submit_button_disabled = True
            if input_mail != "":  # let the user press the button once they have managed to enter something
                # only if they have entered a false email, they will be displayed the error message
                # the error message is not displayed from the ver beginning (when user has not yet entered anything)
                submit_button_disabled = False

            if st.session_state.error_invalid_email:
                custom_message_box('**Error:** Invalid e-mail address format.')

            st.button('Access Demo App Now',
                      disabled=submit_button_disabled,
                      type='primary',
                      on_click=callback_collect_user_email,
                      args=(input_mail, ))


    st.container(height=600, border=False)


def launch_page(build_function: Callable, access: str = 'public_open',
                title: str = 'Title', description: str = 'App Description') -> None:
    """
    Create and display a web page with specified access controls and content.

    Parameters:
    - build_function (Callable): The function responsible for building the main content of the page.
    - access (str, optional): Specifies the access control for the page.
        Possible values: 'public_open', 'email_funnel', 'login_required'.
        Defaults to 'open'.
    - title (str, optional): The title of the web page. Defaults to 'Title'.
    - description (str, optional): The description or subtitle of the web page. Defaults to 'App Description'.

    Returns:
    None

    Example Usage:
    launch_page(my_page_builder, access='public_open', title='AI App', description='Explore the awesomeness!')
    """

    apply_design()          # apply design overrides before spawning any streamlit component
    init_session_state()    # (re-) initialize the session variables / load existing values
    build_sidebar_menu()    # generate an instance of the sidebar, including the menu etc.

    build_top_navbar()      # generate top-level navigation buttons, similar on every page

    st.divider()
    title_cols = st.columns([1, 1])
    with title_cols[0]:
        st.title(title)
    with title_cols[1]:
        add_spacer(1)
        st.write(description)
    st.divider()

    # load app content OR email collection
    # funnel depending on access settings
    if access == 'public_open':
        wrapper_loading_process(build_function)
    elif access == 'email_funnel':
        # after entered once, mail is stored in session_state
        if st.session_state.user_email_collected is None:
            build_email_funnel()
        else:  # if user has already submitted email
            wrapper_loading_process(build_function)
    elif access == 'login_required':
        # TODO implement when required
        pass

    build_footer_main()     # generate footer menu, with clickable link to AISBACH website

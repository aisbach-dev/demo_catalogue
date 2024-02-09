import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime

from st_app_design import footer_main
from st_app_design import apply_design
from st_app_design import add_spacer
from st_app_design import get_option_menu_design

# IMPORT app menu navigation & session states
from st_app_funct import init_session_state

# IMPORT PAGES (aka the individual demo apps)
from st_app_pages import app_page_welcome
from st_app_pages import app_page_modal
from st_app_pages import app_page_demo1
from st_app_pages import app_page_demo2
from st_app_pages import app_page_demo3
from st_app_pages import app_page_demo4
from st_app_pages import app_page_demo5
from st_app_pages import app_page_demo6
from st_app_pages import app_page_contact
from st_app_pages import app_page_website

# APPLY GRAPHIC DESIGN
apply_design()


def callback_tender_details(tender_id):
    st.session_state.selected_tender_id = tender_id

def callback_menu_choice(menu_choice):
    st.session_state.menu_choice = menu_choice


def wrapper_build_page_loading(page, page_changed):

    if page_changed:
        container_top = st.empty()  # build placeholder page in empty container
        container_top.markdown("<br>" * 2, unsafe_allow_html=True)

        with st.spinner(''):  # have a spinner wrap this entire process
            container = st.empty()  # build placeholder page in empty container
            container.markdown("<br>" * 1000, unsafe_allow_html=True)
            page.build_page()  # build actual page below the white container
            container.empty()  # Clear the container once the page is built
            container_top.empty()

    else:  # if the page is reloaded upon user click, however the page did not change
        page.build_page()  # Build the selected page


def app_content():

    # temp storage to transfer page change information
    # from menu sidebar to page builder algorithms
    menu_page_changed = False

    # SIDEBAR MENU
    with st.sidebar:
        st.image('img/aisbach_logo_rounded.png')


        # TOP HEADER NAV MENU BAR (horizontal)
        menu_choice = option_menu(None, ["Welcome Info",
                                         "---",
                                         "Demo App 1",
                                         "Demo App 2",
                                         "Demo App 3",
                                         "Demo App 4",
                                         "Demo App 5",
                                         "Demo App 6",
                                         "---",
                                         "Our Website",
                                         "Contact Us"],
                                  icons=["bi-info-circle",
                                         '',
                                         'bi-bar-chart',
                                         'bi-bar-chart',
                                         'bi-bar-chart',
                                         'bi-bar-chart',
                                         'bi-bar-chart',
                                         'bi-bar-chart',
                                         '',
                                         'bi-window-stack',
                                         'bi-envelope-at'],
                                  menu_icon="cast", default_index=0, orientation="vertical", key='menu_choice',
                                  styles=get_option_menu_design('white', '1rem'))


        # PAGE SWITCH UPDATE page aggrid page keys if page is switched
        if st.session_state.menu_current_page != menu_choice:

            # update grid key before page viewing
            st.session_state.saved_tender_grid_key = datetime.now()
            # update grid key before page viewing
            st.session_state.private_tender_grid_key = datetime.now()
            # WHY is it required to update the aggrid keys before updating?
            # grid keys are used to control table reloads (only necessary on page switch)

            # load selected page into session state variable
            st.session_state.menu_current_page = menu_choice

            menu_page_changed = True  # information that page change




    # this variable contains either the mail of the user as a string or nothing
    active_email_collection_process = st.session_state.user_email_collected

    # TODO re-evaluate the order of these if conditions?
    # TODO also use loading wrapper for these + session states for page switches etc

    # if the session state value evaluates to not None (because it holds the user email) green light
    if active_email_collection_process is None:
        if menu_choice == 'Welcome Info':
            wrapper_build_page_loading(app_page_welcome, menu_page_changed)
        elif menu_choice == 'Our Website':
            wrapper_build_page_loading(app_page_website, menu_page_changed)
        elif menu_choice == 'Contact Us':
            wrapper_build_page_loading(app_page_contact, menu_page_changed)
        else:
            app_page_modal.build_page()

    elif active_email_collection_process is not None:

        # only if the page changes, use spinner plus placeholder page --> if it is the same page do not use these
        # every page is built using a dedicated build function that is executed in a dedicated loading environment
        # so only when the pages are switched --> wrap the build process inside a spinner+placeholder environment
        # make sure that only page switches get the loading environment (not every click in the app)


        if menu_choice == 'Welcome Info':
            wrapper_build_page_loading(app_page_welcome, menu_page_changed)
        elif menu_choice == 'Demo App 1':
            wrapper_build_page_loading(app_page_demo1, menu_page_changed)
        elif menu_choice == 'Demo App 2':
            wrapper_build_page_loading(app_page_demo2, menu_page_changed)
        elif menu_choice == 'Demo App 3':
            wrapper_build_page_loading(app_page_demo3, menu_page_changed)
        elif menu_choice == 'Demo App 4':
            wrapper_build_page_loading(app_page_demo4, menu_page_changed)
        elif menu_choice == 'Demo App 5':
            wrapper_build_page_loading(app_page_demo5, menu_page_changed)
        elif menu_choice == 'Demo App 6':
            wrapper_build_page_loading(app_page_demo6, menu_page_changed)
        elif menu_choice == 'Our Website':
            wrapper_build_page_loading(app_page_website, menu_page_changed)
        elif menu_choice == 'Contact Us':
            wrapper_build_page_loading(app_page_contact, menu_page_changed)


if __name__ == '__main__':

    init_session_state()    # initialize session states
    app_content()
    footer_main()           # insert app footer

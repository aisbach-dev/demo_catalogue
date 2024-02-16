# AISBACH Data Solutions DEMO App (Streamlit) - Implemented by Stefan Rummer, 2024

import time
import streamlit as st
from st_app_components import launch_page


def build_page():

    st.write('building page content')
    time.sleep(3)
    st.write('page built successfully')


launch_page(build_page,
            access='email_funnel',
            title='Demo App 2',
            description='lorem ipsum Beschreibung dies das')

# AISBACH Data Solutions DEMO App (Streamlit) - Implemented by Stefan Rummer, 2024

import streamlit as st
from st_app_funct import build_sidebar_menu
from st_app_design import footer_main
from st_app_design import apply_design

# APPLY GRAPHIC DESIGN
apply_design()

build_sidebar_menu()

st.title('Demo App Page 3')

footer_main()
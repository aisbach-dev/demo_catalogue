import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html

from st_app_design import custom_subheader

def build_page():

   st.link_button('Open Website in **NEW TAB**', "https://www.aisbach.com", type="primary", use_container_width=False)
   iframe_src = "https://www.aisbach.com"
   components.iframe(iframe_src, height=5000)

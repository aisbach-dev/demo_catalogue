import streamlit as st
import streamlit.components.v1 as components


def build_page():

   st.link_button('Open Website in **NEW TAB**', "https://www.aisbach.com/#contact", type="secondary", use_container_width=True)
   iframe_src = "https://www.aisbach.com/contact"
   components.iframe(iframe_src, height=1000)
import streamlit as st
from st_app_design import add_spacer

def set_bg_hack_url():
   '''
   A function to unpack an image from url and set as bg.
   Returns
   -------
   The background.
   '''

   st.markdown(
      f"""
        <style>
        .stApp {{
            background: url("https://raw.githubusercontent.com/aisbach-dev/demo_catalogue/main/img/bg_blurred_light.png?raw=true");
            background-size: contain
        }}
        </style>
        """,
      unsafe_allow_html=True
   )

def build_page():
   set_bg_hack_url()

   add_spacer(10)

   cols = st.columns([1, 1, 1])
   with cols[1]:
      with st.expander("please enter mail to access DEMO app", expanded=True):
         st.write('dfgdgf')




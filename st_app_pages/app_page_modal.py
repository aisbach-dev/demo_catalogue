import streamlit as st


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
            background: url("https://github.com/aisbach-dev/demo_catalogue/blob/main/img/bg_blurred_light.png?raw=true");
            background-size: cover
        }}
        </style>
        """,
      unsafe_allow_html=True
   )

def build_page():
   set_bg_hack_url()

   st.title('modal')


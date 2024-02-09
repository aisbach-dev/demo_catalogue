import streamlit as st
import requests
import re

from st_app_design import custom_message_box

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
            background: url("https://github.com/aisbach-dev/demo_catalogue/blob/main/img/bg_blurred_light_right.png?raw=true?raw=true");
            background-size: contain
        }}
        </style>
        """,
      unsafe_allow_html=True
   )


def send_event_to_formspark(user_email, event_tag):

   form_url = "https://submit-form.com/LnO7yguR8"
   form_data = {"email": user_email, "event": event_tag}
   # Send a POST request to submit the form
   response = requests.post(form_url, data=form_data)
   # Check the response status
   if response.status_code == 200:
      return True
   else:
      return False


def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return (re.match(pattern, email) is not None) and (email != "")


def callback_collect_user_email(input_mail,):

   email_valid = validate_email(input_mail)
   if not email_valid:
      st.session_state.error_invalid_email = True
   else:  # only if the email is of valid format
      st.session_state.error_invalid_email = False
      send_event_to_formspark(input_mail, "user access consent")
      st.session_state.user_email_collected = input_mail


def build_page():
   set_bg_hack_url()

   st.container(height=200, border=False)

   cols = st.columns([0.5, 1, 0.5])
   with cols[1]:

      with st.expander("Disclaimer & Access", expanded=True):

         input_mail = st.text_input('please enter your email address')
         # input_consent = st.checkbox('By clicking the button below I consent to AISBACH storing my email
         # address for user analytics purposes, tracking which demo apps I have accessed and eventually contacting
         # me for further questioning or marketing purposes via the entered email address.')

         st.caption(" By clicking \"Access Demo App Now\" you accept AISBACH's"
                    " [Terms of Service](http://tenderport.tilda.ws/terms-and-conditions) and"
                    " [Data Privacy Policy](http://tenderport.tilda.ws/privacy-policy).")

         submit_button_disabled = True
         if input_mail != "": # let the user press the button once they have managed to enter something
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

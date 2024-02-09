import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates


def build_page():

   st.title('Demo App Overview')
   st.divider()

   st.container(height=50, border=False)

   image_click_coordinates = {}



   img_cols = st.columns([0.25,0.5,0.5, 0.5, 0.25])
   with img_cols[1]:

      st.subheader('**DEMO App 1**')
      st.caption('lorem ipsum app beschreibung (click image to learn more)   \n'
                 'lorem ipsum app beschreibung (click image to learn more)')
      image_click_coordinates['img1'] = streamlit_image_coordinates("img/app_thumbnail_template.png", key='app_img1', width=300)

      st.subheader('**DEMO App 4**')
      st.caption('lorem ipsum app beschreibung (click image to learn more)    \n'
                 'lorem ipsum app beschreibung (click image to learn more)')
      image_click_coordinates['img4'] = streamlit_image_coordinates("img/app_thumbnail_template.png", key='app_img4', width=300)
      # value_app_img7 = streamlit_image_coordinates("img/app_thumbnail_template.png", key='app_img7', width=300)

   with img_cols[2]:

      st.subheader('**DEMO App 2**')
      st.caption('lorem ipsum app beschreibung (click image to learn more)    \n'
                 'lorem ipsum app beschreibung (click image to learn more)')
      image_click_coordinates['img2'] =  streamlit_image_coordinates("img/app_thumbnail_template.png", key='app_img2', width=300)

      st.subheader('**DEMO App 5**')
      st.caption('lorem ipsum app beschreibung (click image to learn more)    \n'
                 'lorem ipsum app beschreibung (click image to learn more)')
      image_click_coordinates['img5'] =  streamlit_image_coordinates("img/app_thumbnail_template.png", key='app_img5', width=300)
      # value_app_img8 = streamlit_image_coordinates("img/app_thumbnail_template.png", key='app_img8', width=300)

   with img_cols[3]:

      st.subheader('**DEMO App 3**')
      st.caption('lorem ipsum app beschreibung (click image to learn more)    \n'
                 'lorem ipsum app beschreibung (click image to learn more)')
      image_click_coordinates['img3'] =  streamlit_image_coordinates("img/app_thumbnail_template.png", key='app_img3', width=300)

      st.subheader('**DEMO App 6**')
      st.caption('lorem ipsum app beschreibung (click image to learn more)    \n'
                 'lorem ipsum app beschreibung (click image to learn more)')
      image_click_coordinates['img6'] =  streamlit_image_coordinates("img/app_thumbnail_template.png", key='app_img6', width=300)
      # value_app_img9 = streamlit_image_coordinates("img/app_thumbnail_template.png", key='app_img9', width=300)


   st.write(image_click_coordinates)


   st.container(height=300, border=False)

   # wenn eines geclickt wird dann werden alle anderen ungeclickt?
   # once clicked  --> session state update which app is clicked --> update sidebar menu value




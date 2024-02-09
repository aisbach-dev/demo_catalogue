import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates


def build_page():

   st.title('Demo App Overview')
   st.divider()

   st.container(height=50, border=False)

   image_click_coordinates = {'img1': None,
                              'img2': None,
                              'img3': None,
                              'img4': None,
                              'img5': None,
                              'img6': None}

   img_cols = st.columns([0.25, 0.5, 0.5, 0.5, 0.25])
   with img_cols[1]:
      st.subheader('**DEMO App 1**')
      st.caption('lorem ipsum app beschreibung (click image to learn more)   \n'
                 'lorem ipsum app beschreibung (click image to learn more)')
      image_click_coordinates['img1'] = streamlit_image_coordinates("img/app_thumbnail_template.png",
                                                                    key='app_img1', width=300)

      st.subheader('**DEMO App 4**')
      st.caption('lorem ipsum app beschreibung (click image to learn more)    \n'
                 'lorem ipsum app beschreibung (click image to learn more)')
      image_click_coordinates['img4'] = streamlit_image_coordinates("img/app_thumbnail_template.png",
                                                                    key='app_img4', width=300)

   with img_cols[2]:
      st.subheader('**DEMO App 2**')
      st.caption('lorem ipsum app beschreibung (click image to learn more)    \n'
                 'lorem ipsum app beschreibung (click image to learn more)')
      image_click_coordinates['img2'] =  streamlit_image_coordinates("img/app_thumbnail_template.png",
                                                                     key='app_img2', width=300)

      st.subheader('**DEMO App 5**')
      st.caption('lorem ipsum app beschreibung (click image to learn more)    \n'
                 'lorem ipsum app beschreibung (click image to learn more)')
      image_click_coordinates['img5'] =  streamlit_image_coordinates("img/app_thumbnail_template.png",
                                                                     key='app_img5', width=300)

   with img_cols[3]:
      st.subheader('**DEMO App 3**')
      st.caption('lorem ipsum app beschreibung (click image to learn more)    \n'
                 'lorem ipsum app beschreibung (click image to learn more)')
      image_click_coordinates['img3'] =  streamlit_image_coordinates("img/app_thumbnail_template.png",
                                                                     key='app_img3', width=300)

      st.subheader('**DEMO App 6**')
      st.caption('lorem ipsum app beschreibung (click image to learn more)    \n'
                 'lorem ipsum app beschreibung (click image to learn more)')
      image_click_coordinates['img6'] =  streamlit_image_coordinates("img/app_thumbnail_template.png",
                                                                     key='app_img6', width=300)

   st.write('new', image_click_coordinates)
   st.write('old', st.session_state.image_click_coordinates)

   mapping = {'img1': 'Demo App 1',
              'img2': 'Demo App 2',
              'img3': 'Demo App 3',
              'img4': 'Demo App 4',
              'img5': 'Demo App 5',
              'img6': 'Demo App 6'}

   if image_click_coordinates != st.session_state.image_click_coordinates:

       for key in image_click_coordinates.keys():
           # find out where the new values differ to the old ones (stored in session state)
           if image_click_coordinates[key] != st.session_state.image_click_coordinates[key]:
               st.session_state.menu_current_page = mapping[key]
               # after finding the newly selected image, updatet the session state
               st.session_state.image_click_coordinates = image_click_coordinates


   st.write(st.session_state.menu_current_page)



   # if the coordinate set that currently exists in

   st.container(height=300, border=False)

   # wenn eines geclickt wird dann werden alle anderen ungeclickt?
   # once clicked  --> session state update which app is clicked --> update sidebar menu value




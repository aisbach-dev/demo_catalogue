# AISBACH Data Solutions DEMO App (Streamlit) - Implemented by Stefan Rummer, 2024

import base64
import streamlit as st
from streamlit_clickable_images import clickable_images

# IMPORT app menu navigation & session states
from st_app_funct import page_switch
from st_app_components import launch_page


def build_app_content():

    st.container(height=50, border=False)

    cols = st.columns([0.2, 1, 0.1, 1, 0.1, 1, 0.1, 1, 0.2])


    # clickable_images returns -1 if not yet clicked and changes to 0 if it has been clicked
    # create dict with keys 'img1' to 'img6', each initialized with -1
    image_click_coordinates = {'img{}'.format(i): -1 for i in range(1, 5)}


    with cols[1]:
        st.subheader('Demo App 1')
        st.caption('lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum ')
        images1 = []
        with open("img/app_thumbnail_template.png", "rb") as image:
            encoded = base64.b64encode(image.read()).decode()
            images1.append(f"data:image/jpeg;base64,{encoded}")
        # clickable_images returns -1 if not yet clicked and changes to 0 if it has been clicked
        clicked = clickable_images(images1, titles=[f"Image #{str(i)}" for i in range(len(images1))],
                                   div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
                                   img_style={"margin": "5px", "height": "auto", "width": '100%'}, key='0')
        image_click_coordinates['img1'] = clicked

    with cols[3]:
        st.subheader('Demo App 2')
        st.caption('lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum ')
        images2 = []
        with open("img/app_thumbnail_template.png", "rb") as image:
            encoded = base64.b64encode(image.read()).decode()
            images2.append(f"data:image/jpeg;base64,{encoded}")
        clicked = clickable_images(images2, titles=[f"Image #{str(i)}" for i in range(len(images2))],
                                   div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
                                   img_style={"margin": "5px", "height": "auto", "width": '100%'}, key='1')
        image_click_coordinates['img2'] = clicked

    with cols[5]:
        st.subheader('Demo App 3')
        st.caption('lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum ')
        images3 = []
        with open("img/app_thumbnail_template.png", "rb") as image:
            encoded = base64.b64encode(image.read()).decode()
            images3.append(f"data:image/jpeg;base64,{encoded}")
        clicked = clickable_images(images3, titles=[f"Image #{str(i)}" for i in range(len(images3))],
                                   div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
                                   img_style={"margin": "5px", "height": "auto", "width": '100%'}, key='2')
        image_click_coordinates['img3'] = clicked

    with cols[7]:
        st.subheader('Demo App 4')
        st.caption('lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum ')
        images4 = []
        with open("img/app_thumbnail_template.png", "rb") as image:
            encoded = base64.b64encode(image.read()).decode()
            images4.append(f"data:image/jpeg;base64,{encoded}")
        clicked = clickable_images(images4, titles=[f"Image #{str(i)}" for i in range(len(images4))],
                                   div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
                                   img_style={"margin": "5px", "height": "auto", "width": '100%'}, key='3')
        image_click_coordinates['img4'] = clicked


    # TODO MAPPING MENU IMAGE --> PAGE NAME (from sidebar menu)
    mapping = {'img1': 'Demo App 1',
               'img2': 'Demo App 2',
               'img3': 'Demo App 3',
               'img4': 'Demo App 4'}

    for key in image_click_coordinates.keys():
        if image_click_coordinates[key] == 0:
            # after finding the selected image, update the session state
            st.session_state.menu_current_page = mapping[key]
            page_switch()


    # spacer between footer and the image array
    st.container(height=300, border=False)


if __name__ == '__main__':

    page_title = 'Landing Page Grid Overview'
    page_description = \
        'Welcome to our app page, where innovation meets exploration! Dive into a captivating' \
        ' overview of cutting-edge AI use cases and dynamic data analytics apps, providing potential' \
        ' buyers with an immersive playground to experience the future of intelligent technology firsthand.' \
        ' Discover, engage, and unleash the power of possibilities right at your fingertips!'

    launch_page(build_app_content, 'public_open', page_title, page_description)

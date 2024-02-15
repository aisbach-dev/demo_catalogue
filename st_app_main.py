# AISBACH Data Solutions DEMO App (Streamlit) - Implemented by Stefan Rummer, 2024

import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates

# IMPORT custom design elements
from st_app_design import add_spacer
from st_app_design import custom_subheader

# IMPORT app menu navigation & session states
from st_app_funct import page_switch
from st_app_funct import launch_page




# TODO this function is currently not used --> maybe use for build process of the pages
def wrapper_build_page_loading(page, page_changed):

    if page_changed:
        container_top = st.empty()  # build placeholder page in empty container
        container_top.markdown("<br>" * 2, unsafe_allow_html=True)

        with st.spinner('Loading app data ...'):  # have a spinner wrap this entire process
            container = st.empty()  # build placeholder page in empty container
            container.markdown("<br>" * 1000, unsafe_allow_html=True)
            page.build_page()  # build actual page below the white container
            container.empty()  # Clear the container once the page is built
            container_top.empty()

    else:  # if the page is reloaded upon user click, however the page did not change
        page.build_page()  # Build the selected page


def build_app_content():

    st.container(height=50, border=False)

    # create dict with keys 'img1' to 'img6', each initialized with None
    image_click_coordinates = {'img{}'.format(i): None for i in range(1, 7)}

    img_cols = st.columns([0.2, 0.5, 0.5, 0.5, 0.2])

    # ROW 1 --> for optimal loading
    with img_cols[1]:
        st.header('**Demo App 1**')
        st.caption('lorem ipsum app beschreibung (click image to learn more)   \n'
                   'lorem ipsum app beschreibung (click image to learn more)')
        image_click_coordinates['img1'] = \
            streamlit_image_coordinates("img/app_thumbnail_template.png",
                                        key='app_img1', width=300)
        st.page_link("pages/app_page_demo1.py", label='**View Demo App 1**')
        add_spacer(2)

    with img_cols[2]:
        st.header('**Demo App 2**')
        st.caption('lorem ipsum app beschreibung (click image to learn more)    \n'
                   'lorem ipsum app beschreibung (click image to learn more)')
        image_click_coordinates['img2'] = \
            streamlit_image_coordinates("img/app_thumbnail_template.png",
                                        key='app_img2', width=300)
        if st.button("**View Demo App 2**", type='primary', key='button2'):
            st.switch_page("pages/app_page_demo2.py")
        add_spacer(2)

    with img_cols[3]:
        st.header('**Demo App 3**')
        custom_subheader('servus')
        st.caption('lorem ipsum app beschreibung (click image to learn more)    \n'
                   'lorem ipsum app beschreibung (click image to learn more)')
        image_click_coordinates['img3'] = \
            streamlit_image_coordinates("img/app_thumbnail_template.png",
                                        key='app_img3', width=300)
        if st.button("**View Demo App 3**", type='secondary', key='button3'):
            st.switch_page("pages/app_page_demo3.py")
        add_spacer(2)


    # ROW 2 --> for optimal loading
    with img_cols[1]:
        st.header('**Demo App 4**')
        st.caption('lorem ipsum app beschreibung (click image to learn more)    \n'
                   'lorem ipsum app beschreibung (click image to learn more)')
        image_click_coordinates['img4'] = \
            streamlit_image_coordinates("img/app_thumbnail_template.png",
                                        key='app_img4', width=300)

    with img_cols[2]:
        st.header('**Demo App 5**')
        st.caption('lorem ipsum app beschreibung (click image to learn more)    \n'
                   'lorem ipsum app beschreibung (click image to learn more)')
        image_click_coordinates['img5'] = \
            streamlit_image_coordinates("img/app_thumbnail_template.png",
                                        key='app_img5', width=300)

    with img_cols[3]:
        st.header('**Demo App 6**')
        st.caption('lorem ipsum app beschreibung (click image to learn more)    \n'
                   'lorem ipsum app beschreibung (click image to learn more)')
        image_click_coordinates['img6'] = \
            streamlit_image_coordinates("img/app_thumbnail_template.png",
                                        key='app_img6', width=300)


    # st.write('new', image_click_coordinates)
    # st.write('old', st.session_state.image_click_coordinates)

    # TODO make this dynamic so that fr every page added there is an image added automatically
    # TODO automate so that this image added automatically is automatically synced with the mapping of pagefile names and page names
    mapping = {'img1': 'Demo App 1',
               'img2': 'Demo App 2',
               'img3': 'Demo App 3',
               'img4': 'Demo App 4',
               'img5': 'Demo App 5',
               'img6': 'Demo App 6'}


    # IF someone clicks on one of the images, identify which image
    # depending on the image switch pages to the corresponding page
    if image_click_coordinates != st.session_state.image_click_coordinates:
        for key in image_click_coordinates.keys():
            # find out where the new values differ to the old ones (stored in session state)
            if image_click_coordinates[key] != st.session_state.image_click_coordinates[key]:
                st.session_state.menu_current_page = mapping[key]
                # after finding the newly selected image, update the session state
                st.session_state.image_click_coordinates = image_click_coordinates
                page_switch()  # switch to the page stored in st.session_state.menu_current_page


    # spacer between footer and the image array
    st.container(height=300, border=False)


if __name__ == '__main__':

    page_title = 'Landing Page Grid Overview'
    page_description = \
        'Welcome to our app page, where innovation meets exploration! Dive into a captivating' \
        ' overview of cutting-edge AI use cases and dynamic data analytics apps, providing potential' \
        ' buyers with an immersive playground to experience the future of intelligent technology firsthand.' \
        ' Discover, engage, and unleash the power of possibilities right at your fingertips!'

    launch_page(build_app_content, page_title, page_description)

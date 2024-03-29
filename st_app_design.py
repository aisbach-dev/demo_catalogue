# AISBACH Data Solutions DEMO App (Streamlit) - Implemented by Stefan Rummer, 2024

import re
import streamlit as st


def add_spacer(lines):
    count = 0  # line breaks
    while count < lines:
        st.write('\n')
        count += 1


def markdown_bold_to_html(text):
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)


def custom_message_box(message_text, background_color='lightgrey', text_color='black',
                       border_width='1px', border_color='white', font_weight='regular'):
    message_text = markdown_bold_to_html(message_text)

    my_custom_div = f"""<div style='background-color: {background_color};
                                    padding: 15px; padding-left:15px;
                                    padding-right:15px; border-radius: 5px;
                                    margin-bottom: 0.6rem;
                                    border: {border_width} solid {border_color};'>
                            <span style='color: {text_color};
                                         text-align: center;
                                         font-size: 1rem;
                                         font-weight: {font_weight};'>{message_text}
                        </div>"""
    st.markdown(my_custom_div, unsafe_allow_html=True)


def custom_status(status_text, subtitle_text, background_color, text_color,
                  border_width='1px', border_color='white',
                  font_weight='regular', font_size_title="1.2rem"):

    # TODO margin bottom has been changed --> potentially other regions of app need fixing now
    my_custom_div = f"""<div style='background-color: {background_color};
                                    padding: 15px; padding-left:15px;
                                    padding-right:15px; border-radius: 5px;
                                    margin-bottom: 0.0rem;
                                    border: {border_width} solid {border_color};'>
                            <span style='color: {text_color};
                                         text-align: center;
                                         font-size: {font_size_title};
                                         font-weight: {font_weight};'>{status_text}
                            </span><br>
                            <span style='color: {text_color};
                                         text-align: left;
                                         font-size: 0.85rem;
                                         font-weight: regular;'>{subtitle_text}
                            </span>
                        </div>"""
    st.markdown(my_custom_div, unsafe_allow_html=True)


def custom_subheader(header_text, font_size="1.75rem"):
    # font-family: Roboto;

    subheader_styled = f"""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');
                        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap'); 
                        </style>
                        <span style='color:black;
                                     font-weight:bold;
                                     font-size:{font_size};
                                     margin-bottom:0.2rem;'>
                        {header_text}</span>
                        """
    st.markdown(subheader_styled, unsafe_allow_html=True)


def custom_subheader_status(header_text, header_status):
    # st.subheader(header_text)
    subheader_styled = f"""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');
                        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap'); 
                        </style>
                        <span style='color: black;
                                     font-weight:bold;
                                     font-family: Roboto;
                                     font-size:1.75rem;
                                     margin-bottom:0.2rem;
                                     background-color: white;'>
                        {header_text}</span>
                        <span style='color: #424242;
                                     font-weight:bold;
                                     font-family: Roboto;
                                     font-size:1.75rem;
                                     margin-bottom:0.2rem;
                                     background-color: white;'>
                        &nbsp;{header_status}&nbsp;&nbsp;</span>
                        """
    st.markdown(subheader_styled, unsafe_allow_html=True)


def set_bg_hack_url():
    """
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    """

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("https://github.com/aisbach-dev/demo_catalogue/blob/main/img/aisbach_page_bg.svg?raw=true?raw=true");
            background-size: contain;
            background-position: right bottom;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


def apply_design():

    # Design implement changes to the standard streamlit UI/UX
    st.set_page_config(page_title="AISBACH Demo", layout="wide", page_icon="img/aisbach_logo.png")

    # set_bg_hack_url()  # Override Default Page and insert background image

    # Design hide top header line
    hide_decoration_bar_style = '''<style>header {visibility: hidden;}</style>'''
    st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)


    # Design move app body further up and remove top padding
    st.markdown('''<style>.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 {padding-top: 0rem;}</style>''',
                unsafe_allow_html=True)


    # Design change hyperlink href link color
    st.markdown('''<style>.st-emotion-cache-etkl18 a {color: black;}</style>''',
                unsafe_allow_html=True)


    # Add custom CSS styles SideBar BACKGROUND COLOR
    # st.markdown("""
    #     <style>
    #         [data-testid="stSidebarContent"] {
    #             background-color: black; /* Change this to your desired color */
    #             /* Add any other styles you want to modify */
    #         }
    #     </style>
    # """, unsafe_allow_html=True)


    # Design hide "made with streamlit" footer menu area
    hide_streamlit_footer = """<style>#MainMenu {visibility: hidden;}
                            footer {visibility: hidden;}</style>"""
    st.markdown(hide_streamlit_footer, unsafe_allow_html=True)

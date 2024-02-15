# AISBACH Data Solutions DEMO App (Streamlit) - Implemented by Stefan Rummer, 2024

import streamlit as st
import pandas as pd
import time
import re
from htbuilder import HtmlElement, div, br, hr, a, p, styles
from htbuilder.units import percent, px
import streamlit_antd_components as sac


def add_spacer(lines):
    count = 0  # line breaks
    while count < lines:
        st.write('\n')
        count += 1


def markdown_bold_to_html(text):
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)


def add_seperator_line():
    markdown_sepline = """<hr style="border:0.1px solid #e0dcdc;
                                     margin-top:-0.5rem;
                                     margin-bottom:-0.5rem">"""
    st.markdown(markdown_sepline, unsafe_allow_html=True)


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
                  border_width='1px', border_color='white', font_weight='regular', font_size_title="1.2rem"):
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


def apply_design():
    # Design implement changes to the standard streamlit UI/UX
    st.set_page_config(page_title="AISBACH Demo", layout="wide", page_icon="img/aisbach_logo.png")

    # Design hide top header line
    hide_decoration_bar_style = '''<style>header {visibility: hidden;}</style>'''
    st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

    # Design move app body further up and remove top padding
    st.markdown('''<style>.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 {padding-top: 0rem;}</style>''',
                unsafe_allow_html=True)

    # Global Font Roboto
    global_font_style = """
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap'); 
                        html, body, [class*="css"] {font-family: 'Roboto', sans-serif;}
                        </style>
                        """
    # TODO do we need this?
    # st.markdown(global_font_style, unsafe_allow_html=True)

    # Design change hyperlink href link color (st.write)
    st.markdown('''<style>.css-16lush4 a {color: #00e68a;}</style>''',
                unsafe_allow_html=True)  # for st.write

    # Design move app body further up and remove top padding
    st.markdown('''<style>.css-k1vhr4 {margin-top: -6.5rem;}</style>''',
                unsafe_allow_html=True)



    # Design change margins below subheader titles
    st.markdown('''<style>.st-emotion-cache-qowy96{background: white;}</style>''',
                unsafe_allow_html=True)



    # Design hide "made with streamlit" footer menu area
    hide_streamlit_footer = """<style>#MainMenu {visibility: hidden;}
                            footer {visibility: hidden;}</style>"""
    st.markdown(hide_streamlit_footer, unsafe_allow_html=True)


def link(link_, text, color, **style):
    return a(_href=link_, _target="_blank", style=styles(**style, color=color))(text)


def layout(*args):
    style = """<style>
        # MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>"""

    body = p()
    style_div = styles(left=0, bottom=0, margin=px(0, 0, 0, 0),
                       width=percent(100), text_align="center",
                       height="60px", opacity=1, color="grey")
    foot = div(style=style_div)(hr(style=styles()), body)
    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)
        elif isinstance(arg, HtmlElement):
            body(arg)

    st.caption(str(foot), unsafe_allow_html=True)


def footer_main():

    myargs = ["Implemented by ",
              link("https://www.aisbach.com", "AISBACH Data Solutions UG", 'black'),
              br(), "© 2024, all rights reserved "]
    layout(*myargs)


def footer_sidebar():

    myargs = [link("http://www.aisbach.com/", "AISBACH", 'grey'),
              ", founded June 2023", br(), "[AI Use Case Demo]"]
    layout(*myargs)


def app_top_navbar():

    # display navbar on top of app page
    nav_cols = st.columns([1, 1])
    with nav_cols[0]:
        if st.button('⬅  **Return to Overview**'):
            st.switch_page('st_app_main.py')
    with nav_cols[1]:
        sac.buttons([
            sac.ButtonsItem(icon='envelope-fill', href='https://www.aisbach.com/#contact', color='#25C3B0'),
            sac.ButtonsItem(icon='linkedin', href='https://www.linkedin.com/company/aisbach', color='#25C3B0'),
            sac.ButtonsItem(icon='globe2', color='black', disabled=False)
        ], align='end', index=2, key='weblinks')

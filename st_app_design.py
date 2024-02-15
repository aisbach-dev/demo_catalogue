import streamlit as st
import pandas as pd
import time
import re
from htbuilder import HtmlElement, div, br, hr, a, p, styles
from htbuilder.units import percent, px


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

    '''st.markdown("""<style>[data-testid=stSidebar] {background-color: #125140;}</style>""",
                unsafe_allow_html=True)'''

    # fix sidebar element spacing --> for all elements remove top padding
    # st.markdown('''<style>.css-yq6wmf {margin-top:-10px;}</style>''',
    #             unsafe_allow_html=True)

    """"# Design change button text size
    st.markdown('''<style>.css-1nt1o6y p{font-size: 0.8rem;}</style>''',
                unsafe_allow_html=True)

    # Design change multiselect font size
    st.markdown('''<style>.st-em{font-size: 0.8rem;}</style>''',
                unsafe_allow_html=True)
    # Design change multiselect text max chars length
    st.markdown('''<style>.st-el{font-size: 0.8rem;}</style>''',
                unsafe_allow_html=True)
    # Design change multiselect text max chars length
    st.markdown('''<style>.st-el{max-width: 200px;}</style>''',
                unsafe_allow_html=True)
    # Design change multiselect select dropdown font size
    st.markdown('''<style>.css-8ojfln{font-size: 0.8rem;}</style>''',
                unsafe_allow_html=True)

    # Design change spinner color to primary color
    st.markdown('''<style>.stSpinner > div > div {border-top-color: #00e68a;}</style>''',
                unsafe_allow_html=True)

    # Design change info notification text color
    st.markdown('''<style>.st-al{color: black;}</style>''',
                unsafe_allow_html=True)

    # Design change height of text input box
    st.markdown('''<style>.st-cd{line-height: 1.2}</style>''',
                unsafe_allow_html=True)"""

    # Design move app body further up and remove top padding
    st.markdown('''<style>.css-k1vhr4 {margin-top: -6.5rem;}</style>''',
                unsafe_allow_html=True)
    # Design move sidebar header further up and remove top padding
    # st.markdown('''<style>.css-1vq4p4l{margin-top: -2.5rem;}</style>''',
    #             unsafe_allow_html=True)

    """# Design change metrics header first line (empty)
    st.markdown('''<style>.css-186pv6d{min-height: 0rem;}</style>''',
                unsafe_allow_html=True)

    # Design change height of text input fields headers
    st.markdown('''<style>.css-qrbaxs {min-height: 0.0rem;}</style>''',
        unsafe_allow_html=True)

    # Design change margins below subheader titles
    st.markdown('''<style>.css-10trblm{margin-bottom: -1.5rem;}</style>''',
                unsafe_allow_html=True)"""

    # Design change margins below subheader titles
    st.markdown('''<style>.st-emotion-cache-qowy96{background: white;}</style>''',
                unsafe_allow_html=True)

    #


    # Design hide top header line
    hide_decoration_bar_style = '''<style>header {visibility: hidden;}</style>'''
    st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

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

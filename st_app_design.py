import streamlit as st
import pandas as pd
import time
import re
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
from htbuilder import HtmlElement, div, br, hr, a, p, styles
from htbuilder.units import percent, px
from bokeh.models.widgets import Div


def add_spacer(lines):
    count = 0  # line breaks
    while count < lines:
        st.write('\n')
        count += 1


def open_website_url_new_window(website_url):
    with st.spinner('opening external website'):
        container = st.container()
        # Create the Bokeh chart inside the container
        with container:
            js = f"window.open('{website_url}')"  # New tab or window
            # js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            # st.bokeh_chart(div)
            st.bokeh_chart(div)

            time.sleep(0.5)  # maybe longer? --> not rerun before page is opened
            # no rerun - otherwise the external website won't open

    # does not work when deployed to the web
    """# other approaches did not work locally and deployed
    with st.spinner('loading external website'):
        new_tab = 2  # Open URL in a new tab
        webbrowser.open(website_url, new=new_tab)"""


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


def button_cell_renderer_view(button_text):
    button_renderer = JsCode('''
                        class BtnCellRenderer {
                            init(params) {
                                this.params = params;
                                this.eGui = document.createElement('div');
                                this.eGui.innerHTML = `
                                 <span>
                                    <button id='click-button' 
                                        class='btn-simple' 
                                        style='color: ${this.params.color};
                                               background-color: ${this.params.background_color};
                                               border:none;outline:none; font-weight:bold;
                                               border-radius:4px; height:1.45rem; 
                                               padding-right:0.5rem; padding-left:0.5rem;'>'''
                             + f'{button_text}' + '''

                                    </button>
                                 </span>
                              `;

                                this.eButton = this.eGui.querySelector('#click-button');

                                this.btnClickedHandler = this.btnClickedHandler.bind(this);
                                this.eButton.addEventListener('click', this.btnClickedHandler);

                            }

                            getGui() {
                                return this.eGui;
                            }

                            refresh() {
                                return true;
                            }

                            destroy() {
                                if (this.eButton) {
                                    this.eGui.removeEventListener('click', this.btnClickedHandler);
                                }
                            }

                            btnClickedHandler(event) {

                                var timeStamp = Date.now();
                                var dateFormat = new Date(timeStamp);

                                this.refreshTable((
                                dateFormat.getDate()+"."+
                                (dateFormat.getMonth()+1)+"."+
                                dateFormat.getFullYear()+" "+
                                dateFormat.getHours()+":"+
                                dateFormat.getMinutes()+":"+
                                dateFormat.getSeconds()+":"+
                                dateFormat.getMilliseconds()));
                            }

                            refreshTable(value) {
                                this.params.setValue(value);
                            }
                        };
                        ''')
    return button_renderer


def offer_status_cell_renderer():
    renderer = JsCode('''
            function(params) {
                var cellValue = params.value;
                var eCell = document.createElement('div');
                eCell.style.marginTop = '0.1rem';
                if (cellValue === 'supplier_withdrew') {
                    eCell.style.backgroundColor = '#F0F2F6';
                    eCell.style.color = 'grey';
                    eCell.style.paddingLeft = '10px';
                    eCell.style.paddingRight = '10px';
                } else if (cellValue === 'offer_submitted') {
                    eCell.style.backgroundColor = '#CCE0DE';
                    eCell.style.fontWeight = 'regular';
                    eCell.style.paddingLeft = '10px';
                    eCell.style.paddingRight = '10px';
                } else if (cellValue === 'buyer_rejected') {
                    eCell.style.backgroundColor = 'lightgrey';
                    eCell.style.color = '#424242';
                    eCell.style.fontWeight = 'bold';
                    eCell.style.paddingLeft = '10px';
                    eCell.style.paddingRight = '10px';
                } else if (cellValue === 'buyer_accepted') {
                    eCell.style.backgroundColor = '#EEF9EE';
                    eCell.style.color = '#125140';
                    eCell.style.fontWeight = 'bold';
                    eCell.style.paddingLeft = '10px';
                    eCell.style.paddingRight = '10px';
                } else if (cellValue === 'buyer_next_steps') {
                    eCell.style.backgroundColor = '#CCE0DE';
                    eCell.style.fontWeight = 'bold';
                    eCell.style.paddingLeft = '10px';
                    eCell.style.paddingRight = '10px';
                }
                eCell.textContent = cellValue.split("_").map(function (word) {
                return word.charAt(0).toUpperCase() + word.slice(1);
                }).join(" ");
                return eCell;

            }''')

    return renderer


def aggrid_custom_css():
    # TODO change font to roboto and change font weight to be easy on the eye

    aggrid_table_custom_css = {  # customize the background color when hovering over a row
        ".ag-row-hover": {"background-color": "rgba(0,230,138, 0.2) !important"},
        # customize the top and bottom borders of the rows
        '.ag-theme-streamlit .ag-row': {
            'border-top-color': 'white',
            'border-bottom-color': '#E0DCDC',
            'border-top-style': 'solid',
            'border-bottom-style': 'solid',
            'border-top-width': '0px',
            'border-bottom-width': '1px'},
        # customize the overall theme of the table
        '.ag-theme-streamlit': {
            '--ag-alpine-active-color': 'green',  # color of checkboxes
            '--ag-range-selection-background-color-4': '#EEF9EE',
            '--ag-range-selection-background-color-3': '#EEF9EE',
            '--ag-range-selection-background-color-2': '#EEF9EE',
            '--ag-range-selection-background-color': '#EEF9EE',
            '--ag-range-selection-border-color': '#CCE0DE',
            '--ag-input-focus-border-color': '#CCE0DE',
            '--ag-input-border-color-invalid': '#CCE0DE',
            '--ag-selected-row-background-color': '#CCE0DE',  # table row current hover
            '--ag-row-hover-color': '#CCE0DE',
            '--ag-column-hover-color': '#CCE0DE',
            'border-color': 'white !important',
            'border-style': 'solid',
            'border-width': '0px',
            'box-shadow': 'none',
            'outline': 'none'},
        # customize the border of the root wrapper
        '.ag-root-wrapper': {
            'border': 'none',
            'border-color': 'white !important'},
        # customize the appearance of selected cells
        ".ag-cell-focus": {
            "border": "1px solid white !important",
            "border-right": "1px solid #F0ECEC !important"}}

    return aggrid_table_custom_css


def aggrid_dict_table(data_dict, aggrid_table_key, height):
    df_data_display = pd.DataFrame.from_dict(data_dict, orient='index')
    df_data_display = df_data_display.reset_index()
    df_data_display.columns.values[0] = 'attributes'
    df_data_display.columns.values[1] = 'content'

    # BUILD AGGRID TABLE CONFIG
    gb = GridOptionsBuilder.from_dataframe(df_data_display)
    gb.configure_default_column(wrapText=True, autoHeight=True, editable=False, resizable=True, flex=True)
    gb.configure_column('attributes', maxWidth=200, )

    # generate the grid options object
    grid_options = gb.build()

    grid_options['enableCellTextSelection'] = True
    grid_options['headerHeight'] = 0  # TODO do we keep this or naw? maybe rename the columns?
    # grid_options['gridStyle'] = {'border': '1px solid white'}  # TODO not working :(

    # find grid_options['columnDefs'] for attributes and modify cellStyle
    attributes_col_def = next((col_def for col_def in grid_options['columnDefs']
                               if col_def['field'] == 'attributes'), None)
    if attributes_col_def:  # BOLD FONT styling of the text in column offer_status
        attributes_col_def['cellStyle'] = {'fontWeight': 'bold', 'color': 'black'}

    AgGrid(df_data_display,
           gridOptions=grid_options,
           # options=table_options,
           # suppress_header=True,
           key=aggrid_table_key,
           fit_columns_on_grid_load=True,
           custom_css=aggrid_custom_css(),
           enable_enterprise_modules=True,
           width='100%',
           height=height,
           reload_data=True)


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


    # Design hide top header line
    hide_decoration_bar_style = '''<style>header {visibility: hidden;}</style>'''
    st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

    # Design hide "made with streamlit" footer menu area
    hide_streamlit_footer = """<style>#MainMenu {visibility: hidden;}
                            footer {visibility: hidden;}</style>"""
    st.markdown(hide_streamlit_footer, unsafe_allow_html=True)


def get_option_menu_design(background_color="#F0F2F6", margin_bottom=""):
    styles = {"container": {"padding": "0!important",
                            "background-color": background_color,
                            "margin-bottom": margin_bottom},
              "icon": {"color": "#16C89D", "font-size": "0.9rem"},
              "nav-link": {"font-size": "0.95rem", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
              "nav-link-selected": {"background-color": "black"}}
    return styles


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

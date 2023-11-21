import streamlit as st
from streamlit_option_menu import option_menu
from st_on_hover_tabs import on_hover_tabs
import pandas as pd
import time
import functions as fu

#establezco la configuración global de la página, tamaño, título de ventana e icono datos

st.set_page_config(page_title='lili_casanova', layout='wide', page_icon=':chart_with_upwards_trend:')

with st.container():
    st.markdown(
    """
    <style>

    .reportview-container .sidebar-content {{
                    padding-top: {1}rem;
                }}
                .reportview-container .main .block-container {{
                    padding-top: {1}rem;
                }}
    .st-cc {

        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        padding: 0px 0;
        background-color: #fbfbfb;
        z-index: 1;
    }

    .st-cv {
        font-size: 14px;
        font-family: monospace;
        text-align: center;
        margin: 0px;
        padding: 5px 20px;
        cursor: pointer;
    }

    .st-cu {
        background-color: #c77652 !important;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

page = fu.menu()

#muestra home
if page == "home":
        fu.home()

#muestra about
if page == "about":
        fu.about()

#muestra academics
if page == "academic":
    fu.academics(use_container_width=True)

#muestra experiencia
if page == "job experience":
    fu.job_experience()

#muestra skills
if page == "skills":
    fu.skills()
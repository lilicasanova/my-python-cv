import streamlit as st
import streamlit_toggle as tog
from streamlit_lottie import st_lottie 
from streamlit_timeline import timeline
from streamlit_bmc import st_bmc
from st_on_hover_tabs import on_hover_tabs
import altair as alt
import pandas as pd
import numpy as np
import json
import os

#creo mi menu lateral(on hover)

def menu():
    #abrir mi archivo style.css
    st.markdown('<style>' + open('./data/style.css').read() + '</style>', unsafe_allow_html=True)

    with st.sidebar:
        page = on_hover_tabs(tabName=['home', 'about', 'job experience', 'academic', 'skills'], 
                            iconName=['home', 'coffee', 'work', 'book', 'computer'], 
                            styles = {'navtab': {'background-color':'#0e121b', #azul
                                                    'color': '#c77652',
                                                    'font-size': '12px',
                                                    "font-family": "monospace",
                                                    'transition': '.3s',
                                                    'white-space': 'nowrap',
                                                    'text-transform': 'lowercase'},
                                        'tabOptionsStyle': {':hover :hover': {'color': '#c77652', #rosa
                                                            'cursor': 'pointer'}},
                                        'iconStyle':{'position':'fixed',
                                                    'left':'7.5px',
                                                    'text-align': 'left'},
                                        'tabStyle' : {'list-style-type': 'none',
                                                        'margin-bottom': '35px',
                                                        'padding-left': '30px'}},
                            default_choice= 0
                            )
        return page

#creo mi función página HOME

def home():
    hide_anchor_link()
    #divido la página en columnas, para poder centrar mi texto inicio usando sólo la 2
    col1, col2, col3 = st.columns([2, 5, 2])

    #a continuación llamo únicamente a mi segunda columna y establezco margen superior para aprovechar el espacio, así como tamaño letra
    col2.markdown("<h1 style='text-align: center; margin-top: 0px; font-size: 30px;'>I'M LILI AND I'M A DATA SCIENTIST</h1>", unsafe_allow_html=True)

    #repito el patrón para las siguientes cinco líneas
    col2.markdown("<h1 style='text-align: center; font-size: 30px;'>I'M  LILI  AND  I'M  A  DATA  SCIENTIST</h1>", unsafe_allow_html=True)
    col2.markdown("<h1 style='text-align: center; font-size: 30px;'>I'M LILI AND I'M A DATA SCIENTIST</h1>", unsafe_allow_html=True)
    col2.markdown("<h1 style='text-align: center; color: #0e121b; text-shadow: 1px 1px 1px #0e121b, 0 0 15px #c77652, 0 0 5px darkblue; font-size: 30px;'>I'M LILI AND I'M A DATA SCIENTIST</h1>", unsafe_allow_html=True)
    col2.markdown("<h1 style='text-align: center; font-size: 30px;'>I'M LILI AND I'M A DATA SCIENTIST</h1>", unsafe_allow_html=True)
    col2.markdown("<h1 style='text-align: center; font-size: 30px;'>I'M LILI AND I'M A DATA SCIENTIST</h1>", unsafe_allow_html=True)

    #establezco en mi última línea el margen inferior para aprovechar de nuevo el espacio
    col2.markdown("<h1 style='text-align: center; font-size: 30px ;margin-bottom: -120px; '>I'M LILI AND I'M A DATA SCIENTIST</h1>", unsafe_allow_html=True)

    #espacio vacío
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")

    #logotipos git y linkedin centrados con hipervínculo y tamaño 30x30
    st.markdown(
        "<p style='text-align: center; margin-bottom: 0px;'>"
        "<a href='https://github.com/lilicasanova'>"
        "<img src='https://raw.githubusercontent.com/lilicasanova/logo/main/github-mark-white.png' alt='GitHub' width='30' height='30'>"
        "</a>"
        "&nbsp;&nbsp;&nbsp;"
        "<a href='https://www.linkedin.com/in/lilicasanova'>"
        "<img src='https://raw.githubusercontent.com/lilicasanova/logo/main/In-White-96.png' alt='LinkedIn' width='30' height='30'>"
        "</a>"
        "</p>",
        unsafe_allow_html=True
    )

    #ahora me centro en mi columna izquierda para añadir la imagen a la izquierda
    with col1:
        hide_anchor_link()
        st.markdown("") 
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")       
  
        path = "./data/animation2.json"
        with open(path,"r") as file: 
            url = json.load(file) 
               
        st_lottie(url, 
            reverse=True, 
            height=300, 
            width=300, 
            speed=1, 
            loop=True, 
            quality='high', 
            key='dataleft'
        )

    #hago lo mismo con mi columna derecha
    with col3:
        hide_anchor_link()
        st.markdown("") 
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")       
  
        path = "./data/animation2.json"
        with open(path,"r") as file: 
            url = json.load(file) 
               
        st_lottie(url, 
            reverse=False, 
            height=300, 
            width=300, 
            speed=1, 
            loop=True, 
            quality='high', 
            key='dataright'
        )

#creo mi función página ABOUT

def about():

    st.markdown(
        """
        <div style='text-align: center; font-family: monospace; color: #c25847;'>
            <h1>some things about me </h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

    #creo unas columnas y uso la segunda para que mi info quede recogida 
    col1, col2, col3 = st.columns([1, 2, 1])

    #coloco el párrafo en la columna céntrica
    with col2:

        st.write(
    
            "Me he demostrado a mí misma una destreza envidiable a cargo de cualquier tipo de tecnología. Aprender algo nuevo y dominarlo me toma un tiempo muy \
            reducido, lo que ha llevado a mi carrera a encaminarse al unísono con los pasos que sigue la Tierra: hacia el mundo del dato y de la inteligencia artificial.\
            \
            Soy una persona muy activa y siempre con sed de aprendizaje y nuevos retos. Considero que sé sacarle provecho a cada minuto y exprimirlo al máximo, \
            lo que me convierte en una persona altamente eficaz y resolutiva. A mis espaldas llevo un recorrido profesional en el que se ha exigido mucho el sentido de la urgencia, \
            lo que me ha hecho desenvolverme en entornos muy ágiles, con una necesidad de adaptación al cambio continua."
        )

        st.write("")

    #defino el estilo del botón para que encaje con el resto de la página
        button_style = (
            "text-align: center; "
            "background-color: #0e121b; "
            "border: 1px solid #c25847; "
            "color: #c25847; "
            "border-radius: 5px; "
            "padding: 10px 20px; "
        )

    #creo la ruta de dónde tendrá que conseguirlo


        cv_filename = "LILI_CASANOVA.pdf"
        cv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), cv_filename)


        with open(cv_path, "rb") as file:
                st.download_button(
                    label="Download CV",
                    data=file,
                    file_name=cv_filename,
                    mime="application/pdf",
                    key="download_cv",
                    help="Click to download my CV",
                )

        st.write("")

        #voy a crear columnas dentro de mi columna céntrica (2) para alinear mi contenido
        col2 = st.columns([1, 1])
        col2[0].write(" ")  #vacía
        col2[1].write(" ")  #vacía

        #alinear a la izquierda
        st.markdown(
                """
                <style>
                .element-container:nth-child(2) {
                    display: flex;
                    justify-content: flex-start;
                }
                </style>
                """,
                unsafe_allow_html=True,
            )

        with col2[0]:
            #titulo de contacto
            st.markdown(
            """
            <div style='text-align: center; font-family: monospace; color: #c25847;'>
                <h2>contact </h2>
            </div>
            """,
            unsafe_allow_html=True,
            )
            #toggle 1 con tlf
            phone_toggle = tog.st_toggle_switch(label="phone number", 
                    key="Key1", 
                    default_value=False, 
                    label_after = False, 
                    inactive_color = '#D3D3D3', 
                    active_color="#11567f", 
                    track_color="#29B5E8"
                    )   
            #toggle 2 con email
            email_toggle = tog.st_toggle_switch(label="e-mail", 
                    key="Key2", 
                    default_value=False, 
                    label_after = False, 
                    inactive_color = '#D3D3D3', 
                    active_color="#11567f", 
                    track_color="#29B5E8"
                    ) 

            #añado bucle para displayear mi tlf o mi email según elección del usuario
            with col2[1]:

                if phone_toggle:
                    st.balloons()
                    phone_number = "+34 675 45 53 22"
                    col2[0].write(f"Puedes llamarme al {phone_number}")

                if email_toggle:
                    st.balloons()
                    email = "lcasanovadut@gmail.com"
                    col2[0].write(f"Puedes contactarme en {email}")

#creo mi función página ACADEMICS

def academics(use_container_width: bool):

    # #titulo
    st.markdown("<h1 style=>Academic evolution chart</h1>", unsafe_allow_html=True)
    st.markdown("") #espacio blanco

    #cargo mi dato
    source = pd.read_csv('./data/academics.csv')

    line_chart = alt.Chart(source).mark_line(point= {
      "filled": False,
      "fill": "pink"
    }).encode(
        x='Year',
        y='Value',
        text='Degree',
        description='Degree'
    )

    st.altair_chart(line_chart, theme="streamlit", use_container_width=True)

    
    #breve descripción
    st.markdown('Aquí se muestra el valor adquirido a lo largo de mi línea de formación en los últimos doce años. Tomando con diferencia el punto más álgido durante el presente año. Con una experiencia inmersiva y práctica en el mundo del análisis del dato, los algoritmos de aprendizaje automático y la productización de los mismos')
    st.markdown("")
    st.markdown('Entre los años **2011**-**2013** finalizo mis estudios pre-universitarios centrándome en disciplinas enfocadas a la *posproducción* audiovisual. Allí aprendo a controlar software de edición de todo tipo. Con el tiempo me desligo del mundo artístico-creativo y debido a mi primera experiencia laboral empiezo a interesarme por decisiones de negocio y análisis de datos de cara a rentabilidad y presupuestos de la empresa.')
    st.markdown("")

#creo mi función página JOB XPERIENCE

def job_experience():

    # load data
    with open('./data/example.json', "r") as f:
        data = f.read()

    # render timeline
    timeline(data, height=500)

#creo mi función página SKILLS

def skills():

    data = {
        "visual": {
            "company_name": "skills acquired"
        },
        "key_partners": {
            "cards": [
                { "id":"1", "text": "Trabajo en equipo" },
                { "id":"2", "text": "Habilidades comunicativas" },
                { "id":"3", "text": "Mente agil y resolutiva" },
                { "id":"4", "text": "Inteligencia emocional" }
            ]
        },
        "key_activities": {
            "cards": [
                { "id":"1", "text": "Python programming" },
                { "id":"2", "text": "Data Analysis, Cleaning & Preprocessing" },
                { "id":"3", "text": "Machine Learning (Supervised & Un-supervised)" },
                { "id":"4", "text": "Data Engineering" }
            ]
        },
        "key_resources": {
            "cards": [
                { "id":"1", "text": "SQL" },
                { "id":"2", "text": "Power BI" },
                { "id":"3", "text": "Office" },
            ]
        },
        "value_propositions": {
            "cards": [
                { "id":"1", "text": "Profesionalidad y compromiso" },
                { "id":"2", "text": "Compañerismo y empatía" },
                { "id":"3", "text": "Buena energía y positividad" }
            ]
        },
        "customer_relationship": {
            "cards": [
                { "id":"1", "text": "Mente abierta" },
                { "id":"2", "text": "Resolución de problemas efectiva" },
                { "id":"3", "text": "Fácil adaptación" }
            ]
        },
        "channels": {
            "cards": [
                { "id":"1", "text": "Alto nivel de Inglés" },
                { "id":"2", "text": "Carnet de conducir y vehículo propio" }
            ]
        },
        "customer_segments": {
            "cards": [
                { "id":"1", "text": "Webscrapping" },
                { "id":"2", "text": "Creación y ataque de APIs" }
            ]
        },
        "cost_structure": {
            "cards": [
                { "id":"1", "text": "Control de versiones, git" },
                { "id":"2", "text": "Conocimientos de diseño" },
                { "id":"3", "text": "Soltura comunicativa" }
            ]
        },
        "revenue_streams": {
            "cards": [
                { "id":"1", "text": "Visualizaciones estáticas" },
                { "id":"2", "text": "Visualizaciones interactivas" }
            ]
        }
    }

    # binding into model
    st_bmc(data)


def hide_anchor_link():
    st.markdown("""
            <style>
            .css-15zrgzn {display: none}
            .css-eczf16 {display: none}
            .css-jn99sy {display: none}
            </style>
            """, unsafe_allow_html=True)

            
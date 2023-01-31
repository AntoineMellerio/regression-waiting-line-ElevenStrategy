import requests
from PIL import Image
import streamlit as st



# Sidebar __________________________________________________________________________
st.set_page_config(page_title="Home Page", page_icon=":roller_coaster:", layout="wide") 
 
markdown = """
GitHub Repository: <https://github.com/AntoineMellerio/regression-waiting-line-ElevenStrategy>
"""

st.sidebar.title("💻 Our work: ")
st.sidebar.info(markdown)

st.sidebar.title("📬 Contact:")
markdown = """
antoine.razeghi@hec.edu  
jiahe.zhu@hec.edu  
antoine.mellerio@hec.edu  
sai-abhishikth.ayyadevara@hec.edu  
zhexuanqiu@gmail.com  
evangelos.viskadouros@hec.edu  
"""
st.sidebar.info(markdown)

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# local_css("style/style.css")
# ---- LOAD ASSETS ----
#lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_4lyswkde.json")
#img_silos_satelite = Image.open("images/silos_satelite.png").resize((250, 250))
#img_silos_segmentation = Image.open("images/silos_segmentation.png").resize((250, 250))
#img_food = Image.open("images/danger.png")
#img_food = img_food.resize((200, 200))
#img_mckinsey = Image.open('images/McKinsey_Script_Mark_2019.svg.png')

# ---- HEADER SECTION ----
with st.container():
    st.title("The Endless Line")

    image_column, text_column = st.columns([3, 1])
    with image_column:

        st.header("A Data Driven Approach to Optimize Customer Wait Times")
        st.subheader('''
        "With great power comes great responsibility" - With more footfalls, come longer queues
        ''')
    st.markdown('''<h3 style='text-align: center; 
                color: lightgreen;
                '>Our goal is to harness the power of data science by accurately forecasting wait times across the park to enable you to enhance customer experience</h3>''', 
        unsafe_allow_html=True)

# ---- Eleven description ----
with st.container():
    st.write("---")
    st.header("About Us:")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("We are 6 Eleven consultants with a strong background in data science")
    with right_column:
        st.write('')
    left_column_2, right_column_2 = st.columns(2)
    with left_column_2:
        st.write( """
            - Holders of Masters in Data Science for Business from École Polytechnique and HEC Paris
            - Diverse technical and business expertise
            - 60+ data science projects amongst us
            """
        )
        st.write("##")
        st.write(
            """
            About Eleven:
            First European strategy consulting firm specifically founded to accompany its clients in their transformation to adapt to the new paradigm of the digital and AI (artificial intelligence) economy thanks to a novel combination of strategic analysis, an entrepreneurial approach and a strong proximity to the digital and data ecosystem.
      
            If this interests to you, consider hiring us for your project.
            """
        )
        st.write("[Our Website >](https://eleven-strategy.com/)")
    image = Image.open('Eleven.jpeg')
    with right_column_2:
        st.image(image, caption = 'Eleven Strategy')
    

# ---- Project Overview ----
with st.container():
    st.write("---")
    st.header("A brief overview of our project")
    st.write("To help you get started")
    st.write("##")

with st.container():
    st.subheader("Forecasting Wait Times To Enhance Customer Experience")
    st.write(
            """
                - An extensive database ranging from customer footfalls to weather patterns.
                - Rigorous preprocessing to clean and identify key predictors
                - Complex models to acheive high accuracy
                - Analysis of predictions to identify impact on KPIs
            For more details please navigate to the "Overview" page.
            """
        )

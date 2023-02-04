from PIL import Image
import streamlit as st
from PIL import Image
from pathlib import Path
import os

# Sidebar __________________________________________________________________________
st.set_page_config(page_title="Home Page", page_icon=":roller_coaster:", layout="wide") 
 


root_path = Path(os.getcwd())
data_path = os.path.join(root_path, 'data')

# Global analysis __________________________________________________________________________
banner = Image.open(os.path.join(root_path,"images/banner_page2.jpeg"))
st.image(banner)

st.sidebar.title("💻 Our work: ")
st.sidebar.info("[GitHub Repository](hhttps://github.com/AntoineMellerio/regression-waiting-line-ElevenStrategy.git)")

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

# ---- HEADER SECTION ----
with st.container():
    st.title("The Endless Line")
    st.header("A data driven approach to optimize customer waiting times.")

    st.markdown('''<h3 style='text-align: center; 
                color: lightgreen;
                '>Our goal is to harness the power of data science by accurately forecasting wait times across the park to enable you to enhance customer experience.</h3>''', 
        unsafe_allow_html=True)

# ---- Eleven description ----
with st.container():
    st.write("---")
    st.header("About us")
    st.subheader("We are 6 Eleven consultants with a strong background in data science.")
    st.write( """
        - Holders of Masters in Data Science for Business from École Polytechnique and HEC Paris
        - Diverse technical and business expertise
        - 60+ data science projects amongst us
        """
    )
    left_column_2, right_column_2 = st.columns([2, 1])
    with left_column_2:
 
        st.write("##")
        st.write(
            """
            About Eleven:  
            First European strategy consulting firm specifically founded to accompany its clients in their transformation to adapt to the new paradigm of the digital and AI (artificial intelligence) economy thanks to a novel combination of strategic analysis, an entrepreneurial approach and a strong proximity to the digital and data ecosystem.
      
            If this interests to you, consider hiring us for your project.
            """
        )
        st.write("[Our Website >](https://eleven-strategy.com/)")
    image = Image.open('images/Eleven.jpeg')
    with right_column_2:
        st.image(image, caption = 'Eleven Strategy')
    
st.write('---')

with st.container():
    st.subheader("Forecasting waiting times to enhance customer experience")
    st.write(
            """
                - An extensive database ranging from customer footfalls to weather patterns.
                - Rigorous preprocessing to clean and identify key predictors
                - Complex models to achieve high accuracy
                - Analysis of predictions to identify impact on KPIs
            For more details please navigate to the "Global insights" page.
            """
        )

st.write("")
st.write("")
st.write("")

st.markdown('''<h6 style='text-align: center; 
            '>"With great power comes great responsibility" - With more footfalls, come longer queues.</h3>''', 
    unsafe_allow_html=True)

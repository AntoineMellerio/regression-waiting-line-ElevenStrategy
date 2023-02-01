import streamlit as st
import os
from PIL import Image
from pathlib import Path

# Sidebar __________________________________________________________________________
st.set_page_config(page_title="Next steps", page_icon=":roller_coaster:", layout="wide")  

st.sidebar.title("💻 Our work: ")
st.sidebar.info("[GitHub Repository](https://github.com/MRL1998/MCK_Silos.git)")
st.sidebar.title("📬 Contact:")
st.sidebar.info("""
sai-abhishikth.ayyadevara@hec.edu  
antoine.mellerio@hec.edu  
evangelos.viskadouros@hec.edu  
antoine.razeghi@hec.edu  
zhexuanqiu@gmail.com  
jiahe.zhu@hec.edu  
""")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

root_path = Path(os.getcwd())
data_path = os.path.join(root_path, 'data')

banner = Image.open(os.path.join(root_path,"images/banner_page2.jpeg"))
st.image(banner)

st.title("Next steps")

st.subheader("Create a pipeline for automatic updating")
st.write("""
         Building a pipeline automatically integrating the latest data (weather, number of people in the park, etc.) 
         would allow us to have updated predictions.
         """
        )
st.write("---")

st.subheader("Improve the predictive model")
st.write("""
         Our model baseline is currently reaching a good 0.6 accuracy.  
         Though, it could be improved using the following technics :
            - blabla
            - blabla
         """
        )
st.write("---")

st.subheader("Reduce the temporal granularity")
st.write("""
         Our model outputs daily predictions on the waiting time of the next months, giving you insights to adapt efficiently.  
         By reducing the granularity to the hour and gathering live data on th park, we would be able to emit hour-to-hour predictions.  
         """
        )
st.write("---")
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

banner = Image.open(os.path.join(root_path,"images/banner_page1.jpg"))
st.image(banner)

st.title("Next steps")

st.subheader("Automatic updating")
st.write("""
         Build a pipeline to automatically integrate the latest data (weather, number of people in the park, etc.).  
         Using APIs would allow us not to base our models on static tables and thus to have automatically updated predictions.
         """
        )

st.subheader("Improve the predictive model")
st.write("""
         Our model baseline currently has a Mean Absolute Percentage Error of 3%.  
         Further parameter tuning and data integration would allow us to improve its accuracy. 
         """
        )

st.subheader("Predict hour-to-hour")
st.write("""
         Our model outputs daily predictions on the waiting time of the next months, giving you insights to adapt efficiently.  
         By reducing the granularity to the hour and gathering live data on the park, we would be able to emit hour-to-hour predictions.  
         """
        )
st.write("---")

st.title("Next features")
st.subheader("Live app for clients")
st.write("""
         Generate a live map showing the estimated waiting time of each ride.
         """
        )

st.subheader("Itinary recommendation")
st.write("""
         Based on the waiting time predictions, on the client's tastes and on it location, recommend an itinary.
         """
        )

st.subheader("Integrate the influence of our recommendations")
st.write("""
         For exemple, recommending intinaries to the clients will surely modify the waiting times. We hence need to take it into acount in our predictions. 
         """
        )

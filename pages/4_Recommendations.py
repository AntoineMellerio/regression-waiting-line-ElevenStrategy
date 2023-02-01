import streamlit as st
from PIL import Image
import os
from pathlib import Path

# Sidebar __________________________________________________________________________
st.set_page_config(page_title="Recommendation", page_icon=":roller_coaster:", layout="wide")

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


# Main Body __________________________________________________________________________
root_path = Path(os.getcwd())
data_path = os.path.join(root_path, 'data')
banner = Image.open(os.path.join(root_path,"images/banner_page5.jpg"))
st.image(banner)
st.title("Recommendations")
st.subheader("Next week results")
st.write("""
         Select limit acceptable waiting time : 45 minutes
         """
        )
st.write("""
         - Attraction 1 and 2 will be overcrowded on Saturday.  
           
        Recommendations : 
         - blabla
         """
        )
st.write("---")
st.subheader("Deep dive into the predictions")

st.write("---")

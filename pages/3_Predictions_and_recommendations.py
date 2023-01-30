import streamlit as st

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
st.title("Check your Coordinates 🌍")
st.subheader("Select any coordinates in the world amd check for Silos")

st.write("""
         How it works
         - Insert the coordinates of the farm you wish to check, press Enter
         - The map will autolocate itself and crop the image (100m x 100m)
         - The image is processed and analyzed by the classification and segmentation model
         """
        )
st.write("---")
st.subheader("Interactive Map")

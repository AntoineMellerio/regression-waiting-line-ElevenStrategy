import io
import os 
import tensorflow as tf
import streamlit as st
import leafmap.foliumap as leafmap
import utils

# Sidebar __________________________________________________________________________
st.set_page_config(page_title="Foodix-Coordinates", page_icon=":corn:", layout="wide")
markdown = """
GitHub Repository: <https://github.com/MRL1998/MCK_Silos.git>
"""
st.sidebar.success("👆👆👆 Select a page above:")
st.sidebar.title("💻 Our work: ")
st.sidebar.info(markdown)

st.sidebar.title("📬 Contact:")
markdown = """
zidi.yang@hec.edu 
milos.basic@hec.edu
antoine.mellerio@hec.edu
camille.epitalon@hec.edu
augustin.de-la-brosse@hec.edu
michael.liersch@hec.edu
"""
st.sidebar.info(markdown)

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

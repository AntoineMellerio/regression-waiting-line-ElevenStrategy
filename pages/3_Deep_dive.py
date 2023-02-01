import streamlit as st
import io
from PIL import Image
import os
import plotly.graph_objects as go
import pandas as pd
from pathlib import Path
from utils.utils import wait_time_figures

root_path = Path(os.getcwd())
data_path = os.path.join(root_path, 'data')

# Sidebar __________________________________________________________________________
st.set_page_config(page_title="Detailed Insights", page_icon=":roller_coaster:", layout="wide") 

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

def saveImage(byteImage):
    bytesImg = io.BytesIO(byteImage)
    imgFile = Image.open(bytesImg)   
   
    return imgFile

# Load data
wait_time_df = pd.read_csv(os.path.join(data_path, 'waiting_times.csv'))

# Global analysis __________________________________________________________________________
banner = Image.open(os.path.join(root_path,"images/banner_page4.jpeg"))
st.image(banner)
st.title("Detailed insights")

# Parameter selection __________________________________________________________________________
# Select the date range
with st.container(): 
    min_date = pd.to_datetime(wait_time_df.WORK_DATE.min())
    max_date = pd.to_datetime(wait_time_df.WORK_DATE.max())

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        start_date = st.date_input('Start date', min_date)

    with c2:
        end_date = st.date_input('End date', max_date)

    if start_date >= end_date:
        st.error('Error: End date must fall after start date.')

    start_date = str(start_date.strftime("%Y-%m-%d"))
    end_date = str(end_date.strftime("%Y-%m-%d"))

# Select the attraction
with st.container():
    c1, c2, c3, = st.columns(3)
    with c1:
        attraction_list = st.multiselect('Rides :roller_coaster:', wait_time_df.ENTITY_DESCRIPTION_SHORT.unique())


# Wait Time insights __________________________________________________________________________
st.subheader("Wait Times")

if len(wait_time_df[(pd.to_datetime(wait_time_df.WORK_DATE)>pd.to_datetime(start_date))&\
    (pd.to_datetime(wait_time_df.WORK_DATE)<pd.to_datetime(end_date))])==0:
    st.write("No data on this period.")
    
else: # Display the metrics
    if attraction_list:
        fig = wait_time_figures(wait_time_df,\
            attraction_list,
            start_date,
            end_date,
            date_label="WORK_DATE",
            wait_time_label="WAIT_TIME_MAX",
            attraction_label="ENTITY_DESCRIPTION_SHORT")
        st.plotly_chart(fig)
    
    else:
        st.write("Please select an attraction.")

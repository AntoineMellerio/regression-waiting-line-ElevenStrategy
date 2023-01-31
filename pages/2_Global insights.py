import streamlit as st
import io
from PIL import Image
import datetime
import os
import plotly.graph_objects as go
import pandas as pd
from pathlib import Path
from utils.utils import attendance_figures

root_path = Path(os.getcwd())
data_path = os.path.join(root_path, 'data')

# Sidebar __________________________________________________________________________
st.set_page_config(page_title="Past performances", page_icon=":roller_coaster:", layout="wide") 

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
attendance_df = pd.read_csv(os.path.join(data_path, 'attendance.csv'))

# Global analysis __________________________________________________________________________
st.title("Global insights")

# Parameter selection __________________________________________________________________________
# Select the date range
with st.container(): 
    min_date = pd.to_datetime(attendance_df.USAGE_DATE.min())
    max_date = pd.to_datetime(attendance_df.USAGE_DATE.max())

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        start_date = st.date_input('Start date', min_date)

    with c2:
        end_date = st.date_input('End date', max_date)

    if start_date >= end_date:
        st.error('Error: End date must fall after start date.')

    start_date = str(start_date.strftime("%Y-%m-%d"))
    end_date = str(end_date.strftime("%Y-%m-%d"))

# Select the park
with st.container():
    c1, c2, c3, = st.columns(3)
    with c1:
        park_list = st.multiselect('Parks :roller_coaster:', attendance_df.FACILITY_NAME.unique())


# Attendance insights __________________________________________________________________________
st.subheader("Attendance")

if len(attendance_df[(pd.to_datetime(attendance_df.USAGE_DATE)>pd.to_datetime(start_date))&\
    (pd.to_datetime(attendance_df.USAGE_DATE)<pd.to_datetime(end_date))])==0:
    st.write("No data on this period.")
    
else: # Display the metrics
    if park_list:
        fig, L = attendance_figures(attendance_df,\
            park_list,
            start_date,
            end_date,
            date_label="USAGE_DATE",
            attendance_label="attendance",
            attraction_label="FACILITY_NAME")

        with st.container():
            c1, c2, c3, = st.columns(3)
            with c1:
                st.metric("Minimum daily attendance", value=L[0])
            with c2:
                st.metric("Average daily attendance", value=L[1])
            with c3:
                st.metric("Maximum daily attendance", value=L[2])

        st.plotly_chart(fig)
    
    else:
        st.write("Please select a park.")
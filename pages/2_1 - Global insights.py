import streamlit as st
import io
from PIL import Image
import os
import plotly.graph_objects as go
import pandas as pd
from pathlib import Path
from utils.utils import attendance_figures, attendance_week_month
import altair as alt
import numpy as np

st.set_page_config(page_title="Past performances", page_icon=":roller_coaster:", layout="wide") 

def saveImage(byteImage):
    bytesImg = io.BytesIO(byteImage)
    imgFile = Image.open(bytesImg)   
   
    return imgFile

# Sidebar __________________________________________________________________________
st.sidebar.title("💻 Our work: ")
st.sidebar.info("[GitHub Repository](https://github.com/AntoineMellerio/regression-waiting-line-ElevenStrategy.git)")
st.sidebar.title("📬 Contact:")
st.sidebar.info("""
sai-abhishikth.ayyadevara@hec.edu  
antoine.mellerio@hec.edu  
evangelos.viskadouros@hec.edu  
antoine.razeghi@hec.edu  
zhexuanqiu@gmail.com  
jiahe.zhu@hec.edu  
""")


# Load data __________________________________________________________________________
root_path = Path(os.getcwd())
data_path = os.path.join(root_path, 'data')
attendance_df = pd.read_csv(os.path.join(data_path, 'attendance.csv'))
link_attraction_park = pd.read_csv(os.path.join(data_path, 'link_attraction_park.csv'))
waiting_times = pd.read_csv(os.path.join(data_path, 'waiting_times.csv'))

# Global analysis __________________________________________________________________________
banner = Image.open(os.path.join(root_path,"images/banner_page3.jpg"))
st.image(banner)

st.title("Global insights")

# Titles container
with st.container():
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Average waiting time")
    with c2:
        st.subheader("Number of attractions")

# Figures and plots container
with st.container():
    # Mean waiting time
    c1, c2, c3, c4 = st.columns(4)
    Lc = [c1, c2, c3, c4]
    waiting_times['year'] = pd.to_datetime(waiting_times.WORK_DATE).apply(lambda x: x.year)
    waiting_times_2019 = waiting_times[waiting_times.year==2019]
    waiting_times_2022 = waiting_times[waiting_times.year==2022]    
    avg_time_2019 = int(waiting_times_2019.WAIT_TIME_MAX.mean().round())
    avg_time_2022 = int(waiting_times_2022.WAIT_TIME_MAX.mean().round())
    delta = int(np.round((avg_time_2022-avg_time_2019)*100/avg_time_2019))
    with c1:
        st.metric("2022", f"{int(waiting_times_2022.WAIT_TIME_MAX.mean().round())} minutes", f"{delta}% compared to 2019")
        
    # Attractions per park
    to_plot = link_attraction_park.copy()
    to_plot["Attraction"] = to_plot["ATTRACTION;PARK"].apply(lambda x: x.split(";")[0])
    to_plot["Park"] = to_plot["ATTRACTION;PARK"].apply(lambda x: x.split(";")[1])
    to_plot = to_plot.drop("ATTRACTION;PARK", axis=1)\
        .groupby("Park")\
        .agg(list)\
        .reset_index()
    for idx, park in enumerate(to_plot.Park) : 
        with Lc[idx+2]:
            attractions = to_plot.loc[idx, 'Attraction']
            st.metric(f"{park}", len(attractions))

st.write("---")

# Attendance seasonalities __________________________________________________________________________
st.subheader("Attendance tendancies")

# Weekly and Monthly tendancies
with st.container():
    # Only apply on significative year (aka without covid) : 2019
    attendance_df['year'] = pd.to_datetime(attendance_df.USAGE_DATE).apply(lambda x: x.year)
    attendance_2019 = attendance_df[attendance_df.year==2019]
    fig_day, fig_month = attendance_week_month(attendance_2019)

    c1, c2, = st.columns(2)
    with c1:
        st.plotly_chart(fig_day)
    with c2:
        st.plotly_chart(fig_month)

st.write("---")


# Attendance day-to-day evolutions __________________________________________________________________________
st.subheader('Attendance day-to-day evolutions')

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
        park_list = st.multiselect('Park :roller_coaster:', attendance_df.FACILITY_NAME.unique())

# Attendance metrics __________________________________________________________________________
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

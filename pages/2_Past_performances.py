import streamlit as st
import io
from PIL import Image
import datetime

# Sidebar __________________________________________________________________________
st.set_page_config(page_title="Past performances", page_icon=":roller_coaster:", layout="centered") 

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

# Global analysis __________________________________________________________________________
st.title("Past performances")
st.subheader("Global analysis and insights")

# Select the date range
with st.container(): 
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)

    c1, c2, c3, c4 = st.columns(4)
    with c2:
        start_date = st.date_input('Start date', today)

    with c3:
        end_date = st.date_input('End date', tomorrow)

    if start_date >= end_date:
        st.error('Error: End date must fall after start date.')


# Select the attraction
with st.container():
    c1, c2, c3, = st.columns(3)
    with c2:
        attraction = st.multiselect('Attractions :roller_coaster:',('All', 'Attraction 1', 'Attraction 2'))


# Display the metrics
with st.container():
    c1, c2, c3, = st.columns(3)

    with c2:
        st.metric("Average time spent per client", value="30 minutes")

import requests
import streamlit as st
#from PIL import Image

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

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

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



col1, arrow ,col2 = st.columns([4, 2, 4])

#france_heatmap = Image.open("images/agriculture_france.png")
#marked_map = Image.open("images/map_marked.png")

with col1:
     st.markdown("<h5 style='text-align: center; color: midnightblue;'>Multilayered agricultural data heatmaps </h5>", unsafe_allow_html=True)
     #st.image(france_heatmap)
with arrow:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    # st.image(arrow_pic)
with col2:
    st.markdown("<h5 style='text-align: center; color: midnightblue;'>Marked Silos next to roads in 10km radius</h5>", unsafe_allow_html=True)
    #st.image(marked_map)

st.write("---")

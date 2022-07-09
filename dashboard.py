# get firebase for the app install python-firebase package.
from firebase import firebase
import streamlit as st  #web development purpose
import plotly.graph_objects as go
from streamlit_option_menu import option_menu


firebase = firebase.FirebaseApplication('https://esp32-5c542-default-rtdb.firebaseio.com', None)
bpm = firebase.get('/test/a', '')
print(bpm)
#sometimes, When we run above code firsttime it can propagate and syntax error, to solve that error please
#rename 'async' file as 'async_' which is in this path C:\Users\mrsak\OneDrive\Desktop\dashboard\venv\Lib\site-packages\firebase
#also reaname the import location of the async file as async_ inside the firebase and _init_ file which are located
# in same path.

#make title of the page(U can see this in this as the tab name)
st.set_page_config(
    page_title='Real-Time Data Medical Dashboard',
    page_icon='✅',
    layout='wide'
)

#title of the page inside the
st.title("Real-Time Medical Dashboard")

#make empty body
placeholder = st.empty()

while True:
    bpm = firebase.get('/test/a', '')
    spo2 =  firebase.get('/test/b', '') #get values from the databse

    with placeholder.container():
        kpi1,kpi2 = st.columns(2) #creation of kpi

        kpi1.metric(label="BPM1 ⏳", value=bpm)
        kpi2.metric(label="SPO2 ⏳", value=spo2)

        gauge1,gauge2 = st.columns(2)
        g1 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=bpm,
            gauge={
                'axis': {
                    'range': [None, 200]
                }
            },
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "BPM"}))
        g2 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=spo2,
            gauge={
                'axis': {
                    'range': [None, 200]
                }
            },
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "SPO2"}))
        gauge1.plotly_chart(g1, use_container_width=True)
        gauge2.plotly_chart(g2, use_container_width=True)
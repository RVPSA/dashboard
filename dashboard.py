# get firebase for the app install python-firebase package.
from firebase import firebase
import streamlit as st  #web development purpose
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from notifypy import Notify


firebase = firebase.FirebaseApplication('https://esp32-5c542-default-rtdb.firebaseio.com', None)
bpm = firebase.get('/test/a', '')
print(bpm)

bpm2 = firebase.get('/test2/a', '')
print(bpm2)
#sometimes, When we run above code firsttime it can propagate and syntax error, to solve that error please
#rename 'async' file as 'async_' which is in this path C:\Users\mrsak\OneDrive\Desktop\dashboard\venv\Lib\site-packages\firebase
#also reaname the import location of the async file as async_ inside the firebase and _init_ file which are located
# in same path.

#make title of the page(U can see this in this as the tab name)
st.set_page_config(
    page_title='Real-Time Data Medical Dashboard',
    page_icon='💗',
    layout='wide'
)

#title of the page inside the
st.title("🧑🏻‍⚕️ Real-Time Medical Dashboard 🫁")

#make empty body
placeholder = st.empty()

with st.sidebar:
    selected = option_menu(
        menu_title= "Main Menu",
        options = ["Patient_1","Patient_2"]
    )
i = 1
j = 1
bpmlist = []
spo2list = []
timelist = []

bpmlist2 = []
spo2list2 = []
timelist2 = []

if selected == "Patient_1":
    while True:
        bpm = firebase.get('/test/a', '')
        spo2 = firebase.get('/test/b', '')  # get values from the databse
        bpm2 = firebase.get('/test2/a', '')

        bpmlist.append(bpm)
        spo2list.append(spo2)
        timelist.append(i)

        with placeholder.container():
            kpi1, kpi2 = st.columns(2)  # creation of kpi

            kpi1.metric(label="BPM1 🫀", value=bpm)
            kpi2.metric(label="SPO2 % 🫒", value=spo2)

            gauge1, gauge2 = st.columns(2)
            g1 = go.Figure(go.Indicator(
                mode="gauge+number",
                value=bpm,
                gauge={
                    'axis': {
                        'range': [None, 200]
                    },
                    'borderwidth': 3,
                    'bordercolor': "white",
                    'threshold' : {
                        'line' : {'color': 'rgb(25,25,112)', 'width' : 2.0},
                        'thickness' : 0.8,
                        'value' : 150
                    },
                    'bgcolor' : "rgb(240,230,140)",
                    'steps' : [
                        {'range' : [0.0,50],'color':"rgb(255,99,71)"},
                        {'range': [155, 200], 'color': "rgb(255,127,80)"}
                    ],
                    'bar' : {'color' : "darkblue", 'thickness': 0.2}
                },
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "BPM 🫀"}))
            g2 = go.Figure(go.Indicator(
                mode="gauge+number",
                value=spo2,
                gauge={
                    'axis': {
                        'range': [None, 100]
                    },
                    'borderwidth': 3,
                    'bordercolor': "white",
                    'threshold': {
                        'line': {'color': 'rgb(25,25,112)', 'width': 2.0},
                        'thickness': 0.8,
                        'value': 95
                    },
                    'steps': [
                        {'range': [0.0, 90], 'color': "rgb(250,128,114)"},
                        {'range': [90, 100], 'color': "rgb(135,206,235)"}
                    ],
                    'bar' : {'color' : "rgb(0,0,128)", 'thickness': 0.2}
                },
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "SPO2 % 🫒"}))
            gauge1.plotly_chart(g1, use_container_width=True)
            gauge2.plotly_chart(g2, use_container_width=True)

            trace0 = go.Scatter(
                x = timelist,
                y = bpmlist,
                mode = 'lines',
                name = 'BPM'
            )
            trace1 = go.Scatter(
                x = timelist,
                y = spo2list,
                mode = 'lines',
                name = 'SPO2'
            )
            data = [trace0, trace1]
            layout = go.Layout(title = "BPM and SPO2")
            figure = go.Figure(data = data, layout = layout)
            st.plotly_chart(figure, use_container_width=True)
            i = i+1
            if bpm < 50 or bpm >150 :
                notification = Notify()
                notification.title = "Alert from Patient 1"
                notification.message = "BPM alert!!!"
                notification.audio = "alarm.wav"
                notification.icon = "heart.png"
                notification.send()
            if spo2 < 90 :
                notification = Notify()
                notification.title = "Alert from Patient 1"
                notification.message = "SPO2 alert!!!"
                notification.audio = "spo2.wav"
                notification.icon = "spo2.png"
                notification.send()
            #notify detail of patient2 while selected on first patient1
            if bpm2 < 50 or bpm2 >150 :
                notification = Notify()
                notification.title = "Alert from Patient 2"
                notification.message = "BPM alert!!!"
                notification.audio = "alarm.wav"
                notification.icon = "heart.png"
                notification.send()
            if bpm2 < 90 :
                notification = Notify()
                notification.title = "Alert from Patient 2"
                notification.message = "SPO2 alert!!!"
                notification.audio = "spo2.wav"
                notification.icon = "spo2.png"
                notification.send()

if selected == "Patient_2":
    while True:
        bpm2 = firebase.get('/test2/a', '')

        bpm = firebase.get('/test/a', '')
        spo2 = firebase.get('/test/b', '')  # get values from the databse
        #spo2 = firebase.get('/test/b', '')  # get values from the databse

        bpmlist2.append(bpm2)
        spo2list2.append(bpm2)
        timelist2.append(j)

        with placeholder.container():
            kpi1, kpi2 = st.columns(2)  # creation of kpi

            kpi1.metric(label="BPM1 🫀", value=bpm2)
            kpi2.metric(label="SPO2 % 🫒", value=bpm2)

            gauge1, gauge2 = st.columns(2)
            g1 = go.Figure(go.Indicator(
                mode="gauge+number",
                value=bpm2,
                gauge={
                    'axis': {
                        'range': [None, 200]
                    },
                    'borderwidth': 3,
                    'bordercolor': "white",
                    'threshold': {
                        'line': {'color': 'rgb(25,25,112)', 'width': 2.0},
                        'thickness': 0.8,
                        'value': 150
                    },
                    'bgcolor': "rgb(240,230,140)",
                    'steps': [
                        {'range': [0.0, 50], 'color': "rgb(255,99,71)"},
                        {'range': [155, 200], 'color': "rgb(255,127,80)"}
                    ],
                    'bar': {'color': "darkblue", 'thickness': 0.2}
                },
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "BPM 🫀"}))
            g2 = go.Figure(go.Indicator(
                mode="gauge+number",
                value=bpm2,
                gauge={
                    'axis': {
                        'range': [None, 100]
                    },
                    'borderwidth': 3,
                    'bordercolor': "white",
                    'threshold': {
                        'line': {'color': 'rgb(25,25,112)', 'width': 2.0},
                        'thickness': 0.8,
                        'value': 95
                    },
                    'steps': [
                        {'range': [0.0, 90], 'color': "rgb(250,128,114)"},
                        {'range': [90, 100], 'color': "rgb(135,206,235)"}
                    ],
                    'bar' : {'color' : "rgb(0,0,128)", 'thickness': 0.2}
                },
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "SPO2 % 🫒"}))
            gauge1.plotly_chart(g1, use_container_width=True)
            gauge2.plotly_chart(g2, use_container_width=True)

            trace0 = go.Scatter(
                x = timelist2,
                y = bpmlist2,
                mode = 'lines',
                name = 'BPM'
            )
            trace1 = go.Scatter(
                x = timelist2,
                y = spo2list2,
                mode = 'lines',
                name = 'SPO2'
            )
            data = [trace0, trace1]
            layout = go.Layout(title = "BPM and SPO2")
            figure = go.Figure(data = data, layout = layout)
            st.plotly_chart(figure, use_container_width=True)
            j = j+1
            if bpm2 < 50 or bpm2 >150 :
                notification = Notify()
                notification.title = "Alert from Patient 2"
                notification.message = "BPM alert!!!"
                notification.audio = "alarm.wav"
                notification.icon = "heart.png"
                notification.send()
            if bpm2 < 90 :
                notification = Notify()
                notification.title = "Alert from Patient 2"
                notification.message = "SPO2 alert!!!"
                notification.audio = "spo2.wav"
                notification.icon = "spo2.png"
                notification.send()
            # notify detail of patient 1 while selected on first patient2
            if bpm < 50 or bpm >150 :
                notification = Notify()
                notification.title = "Alert from Patient 1"
                notification.message = "BPM alert!!!"
                notification.audio = "alarm.wav"
                notification.icon = "heart.png"
                notification.send()
            if spo2 < 90 :
                notification = Notify()
                notification.title = "Alert from Patient 1"
                notification.message = "SPO2 alert!!!"
                notification.audio = "spo2.wav"
                notification.icon = "spo2.png"
                notification.send()



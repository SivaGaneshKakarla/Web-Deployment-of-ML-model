from dataclasses import dataclass
from tkinter import S
import streamlit as st
import pickle
import numpy as np
import pandas as pd


def load_model():
    with open('saved_steps.pkl','rb') as file:
        data=pickle.load(file)
    return data

data=load_model()

regressor=data['model']
le_Gender=data['le_Gender']
le_Day=data['le_Day']
le_Event_i=data['le_Event_i']
le_Event_d=data['le_Event_d']
le_No_Event=data['le_No_event']
le_Time_Slot=data['le_Time_Slot']

def show_predict_page():

    st.title('Attendance of College Mess Prediction')
       
    Gender_t=("male","female")
    Day_t=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
    Event_i_t=("yes","no")
    Event_d_t=("yes","no")
    No_event_t=("yes","no")
    Time_Slot_t=("12:30-1:30","1:30-2:30")
    
    Standard_Table ={
    'Case' : ['No event','Normal Decrement','Normal Increment','Special Increment','Special Decrement'],
    'Rating(in %)' : ['12-15%','17-23%','34-40%','46-52%','72-78%'],
    }
    dfs=pd.DataFrame(Standard_Table)

    st.subheader('STANDARD TABLE')
    st.dataframe(dfs.style.highlight_max(axis=0))

    Gender=st.selectbox("Gender",Gender_t)
    Day=st.selectbox("Day",Day_t)
    Event_i=st.selectbox("Event Increment",Event_i_t)
    Event_d=st.selectbox("Event Decrement",Event_d_t)
    No_event=st.selectbox("No Event",No_event_t)
    Time_Slot=st.selectbox("Time Slot",Time_Slot_t)
    Rating=st.text_input('Rating (Choose from Standard Table)')

    ok=st.button('Predict the number of people attending the Mess')

    if ok:
        X=np.array([[Gender,Day,Event_i,Event_d,No_event,Time_Slot,Rating]])
        X[:,0]=le_Gender.transform(X[:,0])
        X[:,1]=le_Day.transform(X[:,1])
        X[:,2]=le_Event_i.transform(X[:,2])
        X[:,3]=le_Event_d.transform(X[:,3])
        X[:,4]=le_No_Event.transform(X[:,4])
        X[:,5]=le_Time_Slot.transform(X[:,5])
        X=X.astype(float)

        Number=regressor.predict(X)
        st.subheader(f"The number of people attending the Mess is  {int(Number)}")
        

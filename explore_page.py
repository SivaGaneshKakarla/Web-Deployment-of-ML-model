import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

@st.cache
def load_data():
    df=pd.read_csv('College_Mess_Data.csv')
    df.pop('Unnamed: 0')
    return df
df=load_data()

def show_explore_page():
    st.title("Dataset Analysis and Visualization")

    st.subheader("Number males vs females attending the mess on different days")
    fig=plt.figure(figsize=(20,5))
    plt.title('Male vs Female')
    sns.barplot(x='Day',y='Number',hue='Gender',data=df)

    st.pyplot(fig)

    
    
    st.subheader("Number of people attending the mess on different events")
    barWidth=0.25
    fig1,ax1=plt.subplots(figsize=(15,6))
    Event_i=[759,716,826,730,820,685]
    Event_d=[638,602,636,600,637,564]     # Average values found from datset are in a lists
    No_event=[709,669,709,673,713,632]
    br1=np.arange(len(Event_i))
    br2=[x+barWidth for x in br1]
    br3=[x+barWidth for x in br2]
    ax1.bar(br1,Event_i,color='r',width=barWidth,edgecolor='grey',label='Event_i')
    ax1.bar(br2,Event_d,color='g',width=barWidth,edgecolor='grey',label='Event_d')
    ax1.bar(br3,Event_i,color='b',width=barWidth,edgecolor='grey',label='No_event')
    ax1.set_xlabel('Days',fontweight='bold',fontsize=15)
    ax1.set_ylabel('Number of students attending the Mess',fontweight='bold',fontsize=15)
    ax1.set_xticks([r+barWidth for r in range(len(Event_i))],['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'])
    ax1.set_title(' in Timeslot 1:30-2:30 ',fontweight='bold',fontsize=20)
    ax1.legend()
    st.pyplot(fig1)
    

    barWidth=0.25
    fig2,ax2=plt.subplots(figsize=(15,6))
    Event_i=[2167,2045,2312,2014,2303,1892]  # Average values found from dataset are in a lists
    Event_d=[1768,1669,1763,1661,1749,1561]
    No_event=[2003,1890,1977,1874,1982,1761]
    br1=np.arange(len(Event_i))
    br2=[x+barWidth for x in br1]
    br3=[x+barWidth for x in br2]
    ax2.bar(br1,Event_i,color='r',width=barWidth,edgecolor='grey',label='Event_i')
    ax2.bar(br2,Event_d,color='g',width=barWidth,edgecolor='grey',label='Event_d')
    ax2.bar(br3,Event_i,color='b',width=barWidth,edgecolor='grey',label='No_event')
    ax2.set_xlabel('Days',fontweight='bold',fontsize=15)
    ax2.set_ylabel('Number of students attending the Mess',fontweight='bold',fontsize=15)
    ax2.set_xticks([r+barWidth for r in range(len(Event_i))],['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'])
    ax2.set_title(' in Timeslot 12:30-1:30 ',fontweight='bold',fontsize=20)
    plt.legend()
    st.pyplot(fig2)
    
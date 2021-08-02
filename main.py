import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.title("Impact of Weather on Corona")

st.write("Graphs Comparison")


### ---LOAD DATAFRAME


# Add a sidebar

st.sidebar.subheader("Visualization Settings")

# Setup file upload
dataset = st.sidebar.file_uploader(label="Upload your Dataset file.", type=['csv', 'xls'])


#country= df['country'].unique().tolist()
#province=df['city/province'].unique().tolist()
#date=df['date'].unique().tolist()
#days=df['days'].unique().tolist()
#daily_cases=df['daily_cases'].unique().tolist()
#avg_temp=df['avg_temp'].unique().tolist()
#max_temp=df['max_temp'].unique().tolist()
#min_temp=df['min_temp'].unique().tolist()
#humidity=df['min_temp'].unique().tolist()
#wind_pressure=df['min_temp'].unique().tolist()
#ma3days=df['MA_cases(3-days)'].unique().tolist()
#maAvg3days=df['MA_avgTemp(3-days)'].unique().tolist()
#ma4days=df['MA_cases(4-days)'].unique().tolist()
#maAvg4days=df['MA_avgTemp(4-days)'].unique().tolist()
#ma5days=df['MA_cases(5-days)'].unique().tolist()
#maAvg5days=df['MA_avgTemp(5-days)'].unique().tolist()
#ma6days=df['MA_cases(6-days)'].unique().tolist()
#maAvg6days=df['MA_avgTemp(6-days)'].unique().tolist()
#madays=df['MA_cases(7-days)'].unique().tolist()
#maAvg7days=df['MA_avgTemp(7-days)'].unique().tolist()


st.write(dataset)

dataset.columns=['Country','Date', 'total_cases']


country_options =dataset['Country'].unique().tolist()
date_options= dataset['Date'].unique().tolist()
date= st.selectbox( 'Which date would you like to see?', date_options, 100)
country= st.multiselect('Which country would you like to see?', country_options, ['Brazil'])
dataset = dataset[dataset['Country'].isin(country)]


fig= px.bar(covid, x="Country", y="Confirmed", color="Country", range_y=[0,35000], animation_frame="Date", animation_group="Country")
fig.update_layout (width=800)

st.write(fig)


#selected_feature = st.selectbox("Select Feature", ("Avg Temp", "Max Temp", "Min Temp", "Humidity","Wind-Pressure"))








#cases_selection = st.slider('daily_cases',min_value=min(daily_cases), max_value=max(daily_cases), value=(min(daily_cases),max(daily_cases)))
#temp_selection = st.slider('avg_temp',min_value=min(avg_temp), max_value=max(avg_temp), value=(min(avg_temp),max(avg_temp)))


#bar_chart = px.bar(df_grouped, x='daily_cases',y='avg_temp', text='avg_temp',color_discrete_sequence = ['#F63366']*len(df_grouped),template='plotly_white')
#st.plotly_chart(bar_chart)

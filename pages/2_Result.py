import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import time
import datetime


from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

table_service = TableService(connection_string=os.getenv("CONNECTION_STRING"))


# @st.cache_data
def get_result():

    tasks = table_service.query_entities('resulttracking')
    #df = pd.read_csv('sample_result.csv')
    df = pd.DataFrame(tasks)
    # df = df[['date', 'name', 'band', 'scenario', 'perc']]

    return df



try:

    df = get_result()


    st.subheader(':blue[Result Tracking]')

    today = datetime.datetime.now()
    current_year = today.year
    sep_7 = datetime.date(current_year, 9, 5)
    dec_31 = datetime.date(current_year, 12, 31)

    a_date = st.date_input(
        "Select the shortlisted date",
        (sep_7, datetime.date(current_year, 9, 7)),
        sep_7,
        dec_31,
        format="YYYY/MM/DD",
    )

    df['date'] = pd.to_datetime(df['date']).dt.date


    df = df[(df['date'] >= a_date[0]) & (df['date'] <= a_date[1])]
 
    options_band = st.multiselect("Choose confidence band", sorted(df['band'].unique()))
    df = df[df['band'].isin(options_band)]

    options = st.multiselect("Choose scenario", sorted(df['scenario'].unique()))
    df = df[df['scenario'].isin(options)]

       
    value_hit = round(np.mean(df['hit'])*100,1)
    portfolio_gain = round(np.mean(df['perc'])*100,1)
    num_records = len(df['date'])



    st.text(" ") 
    st.text(" ")
    st.text(" ")
    
    st.markdown(':blue[Hit Rate and Portfolio Movement 📈]')
  


    kpi0, kpi1, kpi2 = st.columns(3)

    st.markdown(
        """
            <style>
            [data-testid="stMetricValue"] {
                font-size: 80px;
            }
            </style>
            """,
                unsafe_allow_html=True,
            )


    kpi0.metric(label = "Number of shortlisted stock",
                value = num_records)


    kpi1.metric(label = "Hit Rate (%)",
                value = value_hit,
                )

    kpi2.metric(label = "Portfolio Gain (%)",
                value = portfolio_gain)


    

    st.text(" ")
    st.text(" ") 
    st.text(" ")
    st.text(" ")
    st.text(" ") 
    st.text(" ") 
    st.text(" ")
    st.text(" ") 
    st.text(" ")
    st.text(" ")
    st.text(" ") 
    st.text(" ") 
    st.text(" ")
    st.text(" ") 
    st.text(" ") 

    st.subheader(":blue[Raw Data with Price]")



    st.dataframe(df[['date', 'name', 'band', 'scenario', 'hit', 't0_price', 'tfinal_price', 'perc']], width=1000000) 

    


except :
    st.error(
        """
        **Please select date and scenario**
    """
    )

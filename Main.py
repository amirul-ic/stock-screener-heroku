import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import time
import datetime
import os

from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

## CONNECTION_STRING = azure_table_connection_string
table_service = TableService(connection_string=os.getenv("CONNECTION_STRING"))



# @st.cache_data
def get_UN_data():
    tasks = table_service.query_entities('dailyscorednew')
    df = pd.DataFrame(tasks)
    # df = df[['dailyraw_name', 'index', 'PartitionKey']]
    df = df[['date', 'name', 'scenario', 'band']]
    df = df[df['band'].isin(['High','Medium'])]   
    return df

try:
    df = get_UN_data()
    df['date'] = pd.to_datetime(df['date']).dt.date
    
    st.subheader(':blue[Daily Shortlisted Stocks]')
 
    today = datetime.datetime.now()
    current_year = today.year
    sep_7 = datetime.date(current_year, 9, 7)
    dec_31 = datetime.date(current_year, 12, 31)

    a_date = st.date_input(
        "Select the shortlisted date",
        (sep_7, datetime.date(current_year, 9, 7)),
        sep_7,
        dec_31,
        format="YYYY/MM/DD",
    )

    
    df = df[(df['date'] >= a_date[0]) & (df['date'] <= a_date[1])]
 
    options_band = st.multiselect("Choose confidence band", sorted(df['band'].unique()))
    df = df[df['band'].isin(options_band)]

    options = st.multiselect("Choose scenario", sorted(df['scenario'].unique()))
    df = df[df['scenario'].isin(options)]

        
    st.dataframe(df, width=1000000) 

    
    st.markdown(''' 
    Note: 
    The scenario is in the format of dx_py
    - **:red[dx]** refers to the number of days
    - **:blue[py]** refers to price percentage increase   
    e.g. d5_p3 indicates 'by 5 days, with increment of 3%
    ''')


except :
    st.error(
        """
        **Please select at least one scenario, one date and one confidence band**
    """
    )



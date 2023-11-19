import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import time
import datetime

from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

## CONNECTION_STRING = "azure table connection string"
table_service = TableService(connection_string=CONNECTION_STRING)


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









































































# min_date = datetime.datetime(2020,1,1)
# max_date = datetime.date(2023,9,1)

# a_date = st.date_input("Pick a date", (min_date, max_date))


# Sidebar for navigate

# with st.sidebar:
#     st.write("This code will be printed to the sidebar.")

#     with st.spinner("Loading..."):
#         time.sleep(5)
#     st.success("Done!")



# with st.sidebar:
    
#     selected = option_menu('Page Guide',
#                             ['D7_P3', 'D3_P3', 'D3_P3_1'],
                           
#                            icons = ['cash-coin', 'wallet', 'bank'],
#                            default_index = 0)


# # d7_p3 page

# if (selected == 'D7_P3'):

#     # page title
#     st.title('D7_P3 using ML')

#     # date = st.text_input('Select date of interest')
#     date = st.text_input('Coffee or tea?')

#     # code for prediction
#     predict_result = ''

#     # creating a button for prediction

#     if st.button('Prediction Result'):
#         # stock_prediction = d7_p3_model.predict[['date']]
#         if(date == 'tea'):
#             predict_result  = ("Betul bossku")
#         else:
#             predict_result  = ("Salah bossku")

#     st.success (predict_result)

    

#     # st.dataframe(df)  # Same as st.write(df)

#     st.header('A header with _italics_ :blue[colors] and emojis :sunglasses:')


#     tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])
#     with tab1:       
#         df['date'] = pd.to_datetime(df['date']).dt.date
#         dfa = pd.crosstab(df['date'], df['scenario'], dropna=False)
#         st.bar_chart(dfa)
#     with tab2:
#         st.dataframe(df.style.highlight_max(axis=0))  # Same as st.write(df)
#         st.line_chart(df)


# if (selected == 'D3_P3'):

#     # page title
#     st.title('D3_P3 using ML')
#     st.write("Here's our first attempt at using data to create a table:")
    
#     st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     }))

# if (selected == 'D3_P3_1'):

#     # page title
#     st.title('D3_P3_1 using ML')

#     x = st.slider('x')  # 👈 this is a widget
#     st.write(x, 'squared is', x * x)


#     if st.checkbox('Show dataframe'):
#         df

#         option = st.selectbox(
#         'Which number do you like best?',
#         df['a'])

#         'You selected: ', option


#     add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone'))

#     # Add a slider to the sidebar:
#     add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0))


#     left_column, right_column = st.columns(2)
#     # You can use a column just like st.sidebar:
#     left_column.button('Press me!')

#     # Or even better, call Streamlit functions inside a "with" block:
#     with right_column:
#         chosen = st.radio(
#             'Sorting hat',
#             ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#         st.write(f"You are in {chosen} house!")

#     with st.sidebar:
#         with st.echo():
#             st.write("This code will be printed to the sidebar.")

#         with st.spinner("Loading..."):
#             time.sleep(5)
#         st.success("Done!")

#     'Starting a long computation...'

#     # Add a placeholder
#     latest_iteration = st.empty()
#     bar = st.progress(0)

#     for i in range(100):
#         # Update the progress bar with each iteration.
#         latest_iteration.text(f'Iteration {i+1}')
#         bar.progress(i + 1)
#         time.sleep(0.1)

#     '...and now we\'re done!'

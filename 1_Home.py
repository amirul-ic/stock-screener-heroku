import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import time


print ("hello")
# Import model

d7_p3_model = pickle.load(open('C:/Users/TM36899/Desktop/20230806/python_model_objects/d7_p3_lgbmcv_model.pkl', "rb"))
d3_p3_model = pickle.load(open('C:/Users/TM36899/Desktop/20230806/python_model_objects/d3_p3_lgbmcv_model.pkl', "rb"))

df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "d"])


st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

# Sidebar for navigate

with st.sidebar:
    selected = option_menu('Model Scenario',
                            ['D7_P3', 'D3_P3', 'D3_P3_1'],
                           
                           icons = ['cash-coin', 'wallet', 'bank'],
                           default_index = 0)


# d7_p3 page

if (selected == 'D7_P3'):

    # page title
    st.title('D7_P3 using ML')

    # date = st.text_input('Select date of interest')
    date = st.text_input('Coffee or tea?')

    # code for prediction
    predict_result = ''

    # creating a button for prediction

    if st.button('Prediction Result'):
        # stock_prediction = d7_p3_model.predict[['date']]
        if(date == 'tea'):
            predict_result  = ("Betul bossku")
        else:
            predict_result  = ("Salah bossku")

    st.success (predict_result)

    

    # st.dataframe(df)  # Same as st.write(df)
    df

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])
    with tab1:
        st.bar_chart(df)
    with tab2:
        st.dataframe(df.style.highlight_max(axis=0))  # Same as st.write(df)
        st.line_chart(df)


if (selected == 'D3_P3'):

    # page title
    st.title('D3_P3 using ML')
    st.write("Here's our first attempt at using data to create a table:")
    
    st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    }))

if (selected == 'D3_P3_1'):

    # page title
    st.title('D3_P3_1 using ML')

    x = st.slider('x')  # 👈 this is a widget
    st.write(x, 'squared is', x * x)


    if st.checkbox('Show dataframe'):
        df

        option = st.selectbox(
        'Which number do you like best?',
        df['a'])

        'You selected: ', option


    add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

    # Add a slider to the sidebar:
    add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))


    left_column, right_column = st.columns(2)
    # You can use a column just like st.sidebar:
    left_column.button('Press me!')

    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        chosen = st.radio(
            'Sorting hat',
            ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
        st.write(f"You are in {chosen} house!")



    'Starting a long computation...'

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    '...and now we\'re done!'
import streamlit as st
import streamlit.components.v1 as components


st.title('Background')

multi = ''' Hello everyone.  

In late 2021, this project was initially an assignment for a machine learning subject in postgraduate school.  
In September 2023, I revive this project for the purpose of self-learning in areas such as cloud computing, data engineering, and model deployment.
'''
st.markdown(multi)

#
multi_premise = ''' 
The premise behind this project i.e. screener is simple. We extract all the Bursa Malaysia stocks shortlisted by the freely available technical indicators, 
and find the best possible combination which high chance of percentage increase within the specified time windows, without ever meeting the 
cut loss percentage of -3%.  


'''
st.markdown(multi_premise)









components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vRaN8PQ2krtWep60qucwxR6vRXRmXqfio7EHUEhnBdhCq-d7F44T3XYX5cLYd6RFQnjAE_3wzqV6wfT/embed?start=false&loop=false&delayms=60000", height=480)

multi_space = ''' 
















'''
st.markdown(multi_space)


disclaimer = ''' 
































**Disclaimer**

This stock screener tool is provided solely for personal and educational purposes. It is not intended, nor should it be considered, as a source of financial advice or a tool for making investment decisions. The information and data presented by this stock screener are for informational purposes only and should not be used as a basis for any financial actions.

Investing in financial markets carries inherent risks, and decisions related to buying, selling, or holding stocks should be made with careful consideration of your individual financial situation, risk tolerance, and investment goals. It is strongly recommended that you consult with a qualified financial advisor or conduct thorough research and analysis before making any financial decisions.

The creators and providers of this stock screener do not endorse or guarantee the accuracy, completeness, or reliability of the data and information it presents. We shall not be held responsible for any financial losses, damages, or consequences that may arise from the use of this tool for making investment decisions.

By using this stock screener, you acknowledge and agree to this disclaimer and absolve its creators and providers of any liability associated with your use of the tool for investment purposes. Always exercise caution and seek professional advice when dealing with financial matters.

'''

st.caption(disclaimer)



# st.markdown("# Page 3 🎉")
# st.sidebar.markdown("# Page 3 🎉")

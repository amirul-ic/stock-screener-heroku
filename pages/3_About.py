import streamlit as st
import streamlit.components.v1 as components



multi = ''' Hello everyone.  
In late 2021, this project was initially an assignment for a machine learning subject in postgraduate school.  
In September 2023, I decided to revive this project for the purpose of self-learning in areas such as cloud computing, data engineering, and model deployment.
'''
st.markdown(multi)



components.iframe("https://onedrive.live.com/embed?resid=87A483DE2B2856E6%21207&amp;authkey=!ADTtB6Z3YhhN9jk&amp;em=2&amp;wdAr=1.7777777777777777", height=480)




disclaimer = ''' **Disclaimer**

This stock screener tool is provided solely for personal and educational purposes. It is not intended, nor should it be considered, as a source of financial advice or a tool for making investment decisions. The information and data presented by this stock screener are for informational purposes only and should not be used as a basis for any financial actions.

Investing in financial markets carries inherent risks, and decisions related to buying, selling, or holding stocks should be made with careful consideration of your individual financial situation, risk tolerance, and investment goals. It is strongly recommended that you consult with a qualified financial advisor or conduct thorough research and analysis before making any financial decisions.

The creators and providers of this stock screener do not endorse or guarantee the accuracy, completeness, or reliability of the data and information it presents. We shall not be held responsible for any financial losses, damages, or consequences that may arise from the use of this tool for making investment decisions.

By using this stock screener, you acknowledge and agree to this disclaimer and absolve its creators and providers of any liability associated with your use of the tool for investment purposes. Always exercise caution and seek professional advice when dealing with financial matters.

'''

st.caption(disclaimer)



# st.markdown("# Page 3 🎉")
# st.sidebar.markdown("# Page 3 🎉")

import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title='Learning Style Test', layout='wide')

st.title('Learning Style Test')

st.sidebar.title('Navigation')
st.sidebar.page_link('home.py', label = 'Home', icon='🏠')
st.sidebar.page_link('pages/lst.py', label = 'Learning Style Test', icon='📖')
st.sidebar.page_link('pages/predict.py', label ='Predict Performance',  icon='📊')

st.markdown(f"""
             <div style= 'font-size: 17px; height: 50px'>
             Fill in the following survey to let us know your preferred learning style!
             </div>
             """, unsafe_allow_html=True)

if st.button('Start'):
    switch_page('page1')
    
    
    
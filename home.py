import streamlit as st

st.set_page_config(page_title='Home', layout='wide')

st.title('Welcome to SkyQuest E-Learn')

st.markdown(f"""
            <div style= 'font-size: 17px; height: 50px'>
            Welcome to SkyQuest, your one-stop platform for a variety of courses, including English, Mathematics, Science and more.<br>
            We thrive to create the best and exciting learning experiences, enpowering students for excellence and success.       
            </div>
             """, unsafe_allow_html=True)

# Sidebar for quick access
st.sidebar.title('Navigation')
st.sidebar.page_link('home.py', label = 'Home', icon='🏠')
st.sidebar.page_link('pages/lst.py', label = 'Learning Style Test', icon='📖')
st.sidebar.page_link('pages/predict.py', label ='Predict Performance',  icon='📊')


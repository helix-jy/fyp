import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title='Learning Style Test', layout='wide')
st.title('Learning Style Test')
st.markdown(f"""<div style= 'font-size: 17px; height: 50px'><strong> Page 1/4 </strong></div>
             """, unsafe_allow_html=True)

st.sidebar.title('Navigation')
st.sidebar.page_link('home.py', label = 'Home', icon='🏠')
st.sidebar.page_link('pages/lst.py', label = 'Learning Style Test', icon='📖')
st.sidebar.page_link('pages/predict.py', label ='Predict Performance',  icon='📊')

# Convert responses to 0 / 1 
def map_choice(choice):
    if '(a)' in choice:
        return 0
    elif '(b)' in choice:
        return 1

# Questions 1-11
st.session_state['q1'] = map_choice(st.radio('1. I understand something better after I', 
                                             ('(a) try it out.', '(b) think it through.')))
st.session_state['q2'] = map_choice(st.radio('2. I would rather be considered', 
                                             ('(a) realistic', '(b) innovative')))
st.session_state['q3'] = map_choice(st.radio('3. When I think about what I did yesterday, I am most likely to get', 
                                             ('(a) a picture', '(b) words')))
st.session_state['q4'] = map_choice(st.radio('4. I tend to', 
                                             ('(a) understand details of a subject but may be fuzzy about its overall structure.', 
                                              '(b) understand the overall structure but may be fuzzy about details')))
st.session_state['q5'] = map_choice(st.radio('5. When I am learning something new, it helps me to', 
                                             ('(a) talk about it.', '(b) think about it.')))
st.session_state['q6'] = map_choice(st.radio('6. If I were a teacher, I would rather teach a course', 
                                             ('(a) that deals with facts and real life situations.', '(b) that deals with ideas and theories.')))
st.session_state['q7'] = map_choice(st.radio('7. I prefer to get new information in', 
                                             ('(a) pictures, diagrams, graphs, or maps.', '(b) written directions or verbal information.')))
st.session_state['q8'] = map_choice(st.radio('8. Once I understand', 
                                             ('(a) all the parts, I understand the whole thing.', '(b) the whole thing, I see how the parts fit.')))
st.session_state['q9'] = map_choice(st.radio('9. In a study group working on difficult material, I am more likely to', 
                                             ('(a) jump in and contribute ideas.', '(b) sit back and listen.')))
st.session_state['q10'] = map_choice(st.radio('10. I find it easier', 
                                              ('(a) to learn facts.', '(b) to learn concepts.')))
st.session_state['q11'] = map_choice(st.radio('11. In a book with lots of pictures and charts, I am likely to', 
                                              ('(a) look over the pictures and charts carefully.', '(b) focus on the written text')))

if st.button('Next Page'):
    switch_page('page2')




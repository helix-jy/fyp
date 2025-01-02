import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title='Learning Style Test', layout='wide')
st.title('Learning Style Test')
st.markdown(f"""<div style= 'font-size: 17px; height: 50px'><strong> Page 2/4 </strong></div>
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

# Questions 12-22   
st.session_state['q12'] = map_choice(st.radio('12. When I solve math problems', 
                                              ('(a) I usually work my way to the solutions one step at a time.', 
                                               '(b) I often just see the solutions but then have to struggle to figure out the steps to get to them.')))
st.session_state['q13'] = map_choice(st.radio('13. In classes I have taken', 
                                              ('(a) I have usually gotten to know many of the students.', '(b) I have rarely gotten to know many of the students.')))
st.session_state['q14'] = map_choice(st.radio('14. In reading nonfiction, I prefer', 
                                              ('(a) something that teaches me new facts or tells me how to do something.', 
                                               '(b) something that gives me new ideas to think about.')))
st.session_state['q15'] = map_choice(st.radio('15. I like teachers', ('(a) who put a lot of diagrams on the board.', '(b) who spend a lot of time explaining.')))
st.session_state['q16'] = map_choice(st.radio('16. When Im analyzing a story or a novel', 
                                              ('(a) I think of the incidents and try to put them together to figure out the themes.', 
                                '(b) I just know what the themes are when I finish reading and then I have to go back and find the incidents that demonstrate them.')))
st.session_state['q17'] = map_choice(st.radio('17. When I start a homework problem, I am more likely to', 
                                              ('(a) start working on the solution immediately.', '(b) try to fully understand the problem first.')))
st.session_state['q18'] = map_choice(st.radio('18. I prefer the idea of', ('(a) certainty', '(b) theory')))
st.session_state['q19'] = map_choice(st.radio('19. I remember best', ('(a) what I see.', '(b) what I hear.')))
st.session_state['q20'] = map_choice(st.radio('20. It is more important to me that an instructor', 
                                              ('(a) lay out the material in clear sequential steps.', 
                                               '(b) give me an overall picture and relate the material to other subjects.')))
st.session_state['q21'] = map_choice(st.radio('21. I prefer to study', ('(a) in a study group.', '(b) alone.')))
st.session_state['q22'] = map_choice(st.radio('22. I am more likely to be considered', 
                                              ('(a) careful about the details of my work.', '(b) creative about how to do my work.')))

if st.button('Next Page'):
    switch_page('page3')
    

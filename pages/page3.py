import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title='Learning Style Test', layout='wide')
st.title('Learning Style Test')
st.markdown(f"""<div style= 'font-size: 17px; height: 50px'><strong> Page 3/4 </strong></div>
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

# Questions 23-33
st.session_state['q23'] = map_choice(st.radio('23. When I get directions to a new place, I prefer', 
                                              ('(a) a map.', '(b) written instructions.')))
st.session_state['q24'] = map_choice(st.radio('24. I learn', 
                                              ('(a) at a fairly regular pace. If I study hard, I`ll understand.', 
                                               '(b) in fits and starts. I`ll be totally confused and then suddenly it all makes sense.')))
st.session_state['q25'] = map_choice(st.radio('25. I would rather first', ('(a) try things out.', '(b) think about how I`m going to do it')))
st.session_state['q26'] = map_choice(st.radio('26. When I am reading for enjoyment, I like writers to', 
                                              ('(a) clearly say what they mean.', '(b) say things in creative, interesting ways.')))
st.session_state['q27'] = map_choice(st.radio('27. When I see a diagram or sketch in class, I am most likely to remember', 
                                              ('(a) the picture.', '(b) what the instructor said about it.')))
st.session_state['q28'] = map_choice(st.radio('28. When considering a body of information, I am more likely to', 
                                              ('(a) focus on details and miss the big picture.', 
                                               '(b) try to understand the big picture before getting into the details.')))
st.session_state['q29'] = map_choice(st.radio('29. I more easily remember', ('(a) something I have done.', '(b) something I have thought a lot about.')))
st.session_state['q30'] = map_choice(st.radio('30. When I have to perform a task, I prefer to', 
                                              ('(a) master one way of doing it.', '(b) come up with new ways of doing it.')))
st.session_state['q31'] = map_choice(st.radio('31. When someone is showing me data, I prefer', 
                                              ('(a) charts or graphs.', '(b) text summarizing the results.')))
st.session_state['q32'] = map_choice(st.radio('32. When writing a paper, I am more likely to', 
                                              ('(a) work on (think about or write) the beginning of the paper and progress forward', 
                                               '(b) work on (think about or write) different parts of the paper and then order them.')))
st.session_state['q33'] = map_choice(st.radio('33. When I have to work on a group project, I first want to', 
                                              ('(a) have group brainstorming where everyone contributes ideas.', 
                                               '(b) brainstorm individually and then come together as a group to compare ideas.')))

if st.button('Next Page'):
    switch_page('page4')
    
    
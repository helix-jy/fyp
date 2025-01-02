import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title='Learning Style Test', layout='wide')
st.title('Learning Style Test')
st.markdown(f"""<div style= 'font-size: 17px; height: 50px'><strong> Page 4/4 </strong></div>
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

# Questions 34-44
st.session_state['q34'] = map_choice(st.radio('34. I consider it higher praise to call someone', 
                                              ('(a) sensible', '(b) imaginative')))
st.session_state['q35'] = map_choice(st.radio('35. When I meet people at a party, I am more likely to remember', 
                                              ('(a) what they looked like.', '(b) what they said about themselves.')))
st.session_state['q36'] = map_choice(st.radio('36. When I am learning a new subject, I prefer to', 
                                              ('(a) stay focused on that subject, learning as much about it as I can.', 
                                               '(b) try to make connections between that subject and related subjects.')))
st.session_state['q37'] = map_choice(st.radio('37. I am more likely to be considered', ('(a) outgoing', '(b) reserved')))
st.session_state['q38'] = map_choice(st.radio('38. I prefer courses that emphasize', 
                                              ('(a) concrete material (facts, data).', '(b) abstract material (concepts, theories).')))
st.session_state['q39'] = map_choice(st.radio('39. For entertainment, I would rather', 
                                              ('(a) watch television', '(b) read a book.')))
st.session_state['q40'] = map_choice(st.radio('40. Some teachers start their lectures with an outline of what they will cover. Such outlines are', 
                                              ('(a) somewhat helpful to me.', '(b) very helpful to me.')))
st.session_state['q41'] = map_choice(st.radio('41. The idea of doing homework in groups, with one grade for the entire group,', 
                                              ('(a) appeals to me.', '(b) does not appeal to me.')))
st.session_state['q42'] = map_choice(st.radio('42. When I am doing long calculations,', 
                                              ('(a) I tend to repeat all my steps and check my work carefully.', 
                                               '(b) I find checking my work tiresome and have to force myself to do it.')))
st.session_state['q43'] = map_choice(st.radio('43. I tend to picture places I have been', 
                                              ('(a) easily and fairly accurately.', 
                                               '(b) with difficulty and without much detail.')))
st.session_state['q44'] = map_choice(st.radio('44. When solving problems in a group, I would be more likely to', 
                                              ('(a) think of the steps in the solution process.', 
                                               '(b) think of possible consequences or applications of the solution in a wide range of areas.')))

if st.button('Finish'):
    switch_page('results')


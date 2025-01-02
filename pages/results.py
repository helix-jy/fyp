import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title='Learning Style Test', layout='wide')

st.title('Results')

st.sidebar.title('Navigation')
st.sidebar.page_link('home.py', label = 'Home', icon='🏠')
st.sidebar.page_link('pages/lst.py', label = 'Learning Style Test', icon='📖')
st.sidebar.page_link('pages/predict.py', label ='Predict Performance',  icon='📊')

# Map questions to category
dim = {
    'q1': 'AvR', 'q2': 'SvI', 'q3': 'VvV', 'q4': 'SvG',
    'q5': 'AvR', 'q6': 'SvI', 'q7': 'VvV', 'q8': 'SvG',
    'q9': 'AvR', 'q10': 'SvI', 'q11': 'VvV', 'q12': 'SvG',
    'q13': 'AvR', 'q14': 'SvI', 'q15': 'VvV', 'q16': 'SvG',
    'q17': 'AvR', 'q18': 'SvI', 'q19': 'VvV', 'q20': 'SvG',
    'q21': 'AvR', 'q22': 'SvI', 'q23': 'VvV', 'q24': 'SvG',
    'q25': 'AvR', 'q26': 'SvI', 'q27': 'VvV', 'q28': 'SvG',
    'q29': 'AvR', 'q30': 'SvI', 'q31': 'VvV', 'q32': 'SvG',
    'q33': 'AvR', 'q34': 'SvI', 'q35': 'VvV', 'q36': 'SvG',
    'q37': 'AvR', 'q38': 'SvI', 'q39': 'VvV', 'q40': 'SvG',
    'q41': 'AvR', 'q42': 'SvI', 'q43': 'VvV', 'q44': 'SvG',
}

def tally_responses():
    tally = {
        'AvR': {'active': 0, 'reflective': 0},
        'SvI': {'sensing': 0, 'intuitive': 0},
        'VvV': {'visual': 0, 'verbal': 0},
        'SvG': {'sequential': 0, 'global': 0}
    }
    for key, category in dim.items():
        response = st.session_state.get(key, None)
        if response is not None:
            if response == 0:
                if category == 'AvR':
                    tally[category]['active'] += 1
                elif category == 'SvI':
                    tally[category]['sensing'] += 1
                elif category == 'VvV':
                    tally[category]['visual'] += 1
                elif category == 'SvG':
                    tally[category]['sequential'] += 1
            elif response == 1:
                if category == 'AvR':
                    tally[category]['reflective'] += 1
                elif category == 'SvI':
                    tally[category]['intuitive'] += 1
                elif category == 'VvV':
                    tally[category]['verbal'] += 1
                elif category == 'SvG':
                    tally[category]['global'] += 1  
    return tally

tally = tally_responses()
act_count = tally['AvR']['active']
ref_count = tally['AvR']['reflective']
sen_count = tally['SvI']['sensing']
int_count = tally['SvI']['intuitive']
vis_count = tally['VvV']['visual']
ver_count = tally['VvV']['verbal']
seq_count = tally['SvG']['sequential']
glo_count = tally['SvG']['global']

# Results
if act_count > ref_count:
    style_1 = 'Active'
    score_1 = act_count - ref_count
elif ref_count > act_count:
    style_1 = 'Reflective'
    score_1 = ref_count - act_count
if sen_count > int_count:
    style_2 = 'Sensing'
    score_2 = sen_count - int_count
elif int_count > sen_count:
    style_2 = 'Intuitive'
    score_2 = int_count - sen_count
if vis_count > ver_count:
    style_3 = 'Visual'
    score_3 = vis_count - ver_count
elif ver_count > vis_count:
    style_3 = 'Verbal'
    score_3 = ver_count - vis_count
if seq_count > glo_count:
    style_4 = 'Sequential'
    score_4 = seq_count - glo_count
elif glo_count > seq_count:
    style_4 = 'Global'
    score_4 = glo_count - seq_count
    
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)
row5 = st.columns(1)
row6 = st.columns(1)
row7 = st.columns(2)
row8 = st.columns(2)
row9 = st.columns(2)
row10 = st.columns(2)
container1 = row1[0].container()
container2 = row1[1].container()
container3 = row2[0].container()
container4 = row2[1].container()
container5 = row3[0].container()
container6 = row3[1].container()
container7 = row4[0].container()
container8 = row4[1].container()
container9 = row5[0].container()
container10 = row6[0].container()
container11 = row7[0].container()
container12 = row7[1].container()
container13 = row8[0].container()
container14 = row8[1].container()
container15 = row9[0].container()
container16 = row9[1].container()
container17 = row10[0].container()
container18 = row10[1].container()

# Score options
options_left = [11, 9, 7, 5, 3, 1, 'N']
options_right = ['N', 1, 3, 5, 7, 9, 11]
    
# Visualize results
with container1:
    st.markdown("""
    <style>
    .stRadio > div {
        display: flex;
        flex-direction: row;
    }
    </style>
    """, unsafe_allow_html=True)
    if style_1 == 'Active' and score_1 in options_left:
        selected_option = score_1
    else:
        selected_option = 'N'
    st.radio("**Active**:", options_left, index=options_left.index(selected_option), disabled=True)    
    
with container2:
    st.markdown("""<style>
    .stRadio > label {
        text-align: right;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)
    if style_1 == 'Reflective' and score_1 in options_right:
        selected_option = score_1
    else:
        selected_option = 'N'
    st.radio("**Reflective**:", options_right, index=options_right.index(selected_option), disabled=True)
    
with container3:
    st.markdown("""
    <style>
    .stRadio > div {
        display: flex;
        flex-direction: row;
    }
    </style>
    """, unsafe_allow_html=True)
    if style_2 == 'Sensing' and score_2 in options_left:
        selected_option = score_2
    else:
        selected_option = 'N'
    st.radio("**Sensing**:", options_left, index=options_left.index(selected_option), disabled=True)   
    
with container4:
    st.markdown("""<style>
    .stRadio > label {
        text-align: right;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)
    if style_2 == 'Intuitive' and score_2 in options_right:
        selected_option = score_2
    else:
        selected_option = 'N'
    st.radio("**Intuitive**:", options_right, index=options_right.index(selected_option), disabled=True)
    
with container5:
    st.markdown("""
    <style>
    .stRadio > div {
        display: flex;
        flex-direction: row;
    }
    </style>
    """, unsafe_allow_html=True)
    if style_3 == 'Visual' and score_3 in options_left:
        selected_option = score_3
    else:
        selected_option = 'N'
    st.radio("**Visual**:", options_left, index=options_left.index(selected_option), disabled=True)
         
with container6:
    st.markdown("""<style>
    .stRadio > label {
        text-align: right;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)
    if style_3 == 'Verbal' and score_1 in options_right:
        selected_option = score_3
    else:
        selected_option = 'N'
    st.radio("**Verbal**:", options_right, index=options_right.index(selected_option), disabled=True)
    
with container7:
    st.markdown("""
    <style>
    .stRadio > div {
        display: flex;
        flex-direction: row;
    }
    </style>
    """, unsafe_allow_html=True)
    if style_4 == 'Sequential' and score_4 in options_left:
        selected_option = score_4
    else:
        selected_option = 'N'
    st.radio("**Sequential**:", options_left, index=options_left.index(selected_option), disabled=True)  
      
with container8:
    st.markdown("""<style>
    .stRadio > label {
        text-align: right;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)
    if style_4 == 'Global' and score_1 in options_right:
        selected_option = score_4
    else:
        selected_option = 'N'
    st.radio("**Global**:", options_right, index=options_right.index(selected_option), disabled=True)

# Personal insights
with container9:
    st.header("Your Learning Style Profile")
    custom_css = """
    <style>
    .large-font {
        font-size: 20px;
    }
    .small-font {
        font-size: 16px;
    }
    </style>
    """
    content = f"""
    <div class="large-font"><strong>Active vs. Reflective</strong><br></div>
    <div class="small-font">Your preferred style: <strong>{style_1}</strong>  |  Score: {score_1}<br><br></div>
    <div class="large-font"><strong>Sensing vs. Intuitive</strong><br></div>
    <div class="small-font">Your preferred style: <strong>{style_2}</strong>  |  Score: {score_2}<br><br></div>
    <div class="large-font"><strong>Visual vs. Verbal</strong><br></div>
    <div class="small-font">Your preferred style: <strong>{style_3}</strong>  |  Score: {score_3}<br><br></div>
    <div class="large-font"><strong>Sequential vs. Global</strong><br></div>
    <div class="small-font">Your preferred style: <strong>{style_4}</strong>  |  Score: {score_4}<br><br></div>
    """
    st.markdown(custom_css + content, unsafe_allow_html=True)
    
# Table of Learning Styles
with container10:
    st.header("Dimensions of Learning Styles")
           
with container11:
    st.markdown(f"""
                <div style='background-color: #ffeaea; padding: 10px; border-radius: 5px; box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);'>
                <strong>ACTIVE</strong><br><br>
                Prefers engaging with information practically.<br>
                Learns best through discussions and applications.
                </div>
                """, unsafe_allow_html=True)   
with container12:
    st.markdown(f"""
                <div style='background-color: #ffeaea; padding: 10px; border-radius: 5px; box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);'>
                <strong>REFLECTIVE</strong><br><br>
                Prefers thinking and reflecting on information quietly beforehand.<br>
                Learns best through critical thinking.
                </div>
                """, unsafe_allow_html=True)
with container13:
    st.markdown(f"""
                <div style='background-color: #fffdea; padding: 10px; border-radius: 5px; box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);'>
                <strong>SENSING</strong><br><br>
                Prefers learning about facts, details, and real-world applications.<br>
                Works on problems by well-established methods.
                </div>
                """, unsafe_allow_html=True)
with container14:
    st.markdown(f"""
                <div style='background-color: #fffdea; padding: 10px; border-radius: 5px; box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);'>
                <strong>INTUITIVE</strong><br><br>
                Prefers learning abstract concepts and theories.<br>
                Enjoys exploring possibilities to innovate and discovering patterns.
                </div>
                """, unsafe_allow_html=True)   
with container15:
    st.markdown(f"""
                <div style='background-color: #f2ffea; padding: 10px; border-radius: 5px; box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);'>
                <strong>VISUAL</strong><br><br>
                Learns best from what they see. (Diagrams, pictures, videos)
                </div>
                """, unsafe_allow_html=True)
with container16:
    st.markdown(f"""
                <div style='background-color: #f2ffea; padding: 10px; border-radius: 5px; box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);'>
                <strong>VERBAL</strong><br><br>
                Learns best through words, written or spoken. (Text, reading, discussions)
                </div>
                """, unsafe_allow_html=True)
with container17:
    st.markdown(f"""
                <div style='background-color: #eafffe; padding: 10px; border-radius: 5px; box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);'>
                <strong>SEQUENTIAL</strong><br><br>
                Prefers learning in a linear, step-by-step manner.<br>
                Learns best when information is presented in a structured manner.
                </div>
                """, unsafe_allow_html=True)
with container18:
    st.markdown(f"""
                <div style='background-color: #eafffe; padding: 10px; border-radius: 5px; box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);'>
                <strong>GLOBAL</strong><br><br>
                Prefers seeing the big picture before diving into details.<br>
                Learns best from analyzing how small details fit in the overall context.
                </div>
                """, unsafe_allow_html=True)

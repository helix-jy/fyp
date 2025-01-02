import streamlit as st
import pandas as pd
import shap as sp
from joblib import load
import matplotlib.pyplot as plt

st.set_page_config(page_title='Student Performance Predictions', layout='wide')
st.title("🎓 Student Performance Prediction")

# Load the model
model = load('knn_model.joblib')    
scaler = load('scaler.joblib')
explainer = load('explainer.joblib')

# Load dataset
df = pd.read_csv('student-scores-final.csv')
X = df.drop('average_score', axis = 1)
y = df['average_score']

st.markdown(f"""
             <div style= 'font-size: 17px; height: 50px'>
             Enter details below on your demographics and examination scores to find out your future performance:
             </div>
             """, unsafe_allow_html=True)

st.sidebar.title('Navigation')
st.sidebar.page_link('home.py', label = 'Home', icon='🏠')
st.sidebar.page_link('pages/lst.py', label = 'Learning Style Test', icon='📖')
st.sidebar.page_link('pages/predict.py', label ='Predict Performance',  icon='📊')
 
col1, col2 = st.columns(2)
with col1:
    # Choice mappings
    job_map = {'No': 0, 'Yes': 1}
    ex_act_map = {'No': 0, 'Yes': 1}
    career_map = {
        'Accountant': 0, 'Artist': 1, 'Banker': 2, 'Business Owner': 3, 'Construction Worker': 4,
        'Designer': 5, 'Doctor': 6, 'Game Development': 7, 'Government Officer': 8,
        'Lawyer': 9, 'Real Estate Development': 10, 'Scientist': 11, 'Software Engineer': 12,
        'Stock Investor': 13, 'Teacher': 14, 'Unknown': 15, 'Writer': 16
    }
    
    st.markdown(f"""
             <div style= 'font-size: 20px; height: 50px'>
             <strong>Student Details</strong>
             </div>
             """, unsafe_allow_html=True)
    
    # Input fields
    days = st.selectbox('Number of Absent Days', (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    job = st.radio('Part Time Job', ('No', 'Yes'))
    job = job_map[job]
    ex_act = st.radio('Extracurricular Activities', ('No', 'Yes'))
    ex_act = ex_act_map[ex_act]
    career = st.selectbox('Career Aspiration', ('Accountant', 'Artist', 'Banker', 'Business Owner', 'Construction Worker', 'Designer',
                                                'Doctor', 'Game Development', 'Government Officer', 'Lawyer', 'Real Estate Development',
                                                'Scientist', 'Software Engineer', 'Stock Investor', 'Teacher', 'Unknown', 'Writer'))
    career = career_map[career]
    hrs = st.number_input('Weekly Self-Study Hours', min_value=0, max_value=100, step=1)

with col2:
    st.markdown(f"""
             <div style= 'font-size: 20px; height: 50px'>
             <strong>Exam Scores</strong>
             </div>
             """, unsafe_allow_html=True)
    
    # Input fields
    eng = st.number_input('English', min_value=0, max_value=100, step=1)
    geo = st.number_input('Geography', min_value=0, max_value=100, step=1)
    hist = st.number_input('History', min_value=0, max_value=100, step=1)
    math = st.number_input('Mathematics', min_value=0, max_value=100, step=1)
    phy = st.number_input('Physics', min_value=0, max_value=100, step=1)
    chem = st.number_input('Chemistry', min_value=0, max_value=100, step=1)
    bio = st.number_input('Biology', min_value=0, max_value=100, step=1)
    
    def get_input_data(job, days, ex_act, hrs, hist, phy, chem, bio, eng, geo, career, math):
        return [[job, days, ex_act, hrs, hist, phy, chem, bio, eng, geo, career, math]]
    
    def feature_contributions(explainer, data, feature_names):
        # Calculate SHAP values from explainer
        shap_values = explainer.shap_values(data)
        
        # DataFrame of features & SHAP values
        shap_df = pd.DataFrame({
            'Feature': feature_names,
            'Score': shap_values[0]
        }).sort_values(by='Score', key=abs, ascending=False, ignore_index=True)
        
        expected_value = explainer.expected_value     # Expected value
        final_pred = expected_value + shap_df['Score'].sum()     # Final prediction
        
        # Append expected value & final predicrion
        ex_value_df = pd.DataFrame({
            'Feature': ['Expected Score'],
            'Score': [expected_value]
        })
        final_pred_df = pd.DataFrame({
            'Feature': ['Final Score'],
            'Score': [final_pred]
        })
        
        shap_df = pd.concat([ex_value_df, shap_df, final_pred_df], ignore_index=True)
        return shap_df
    
    # Predict button    
    predict_button = st.button('Predict')
    
def generate_advice(shap_df, demographic_features, exam_features, advice_mapping):
    top_demographic_feature = shap_df[shap_df['Feature'].isin(demographic_features)].iloc[0]['Feature']
    top_exam_feature = shap_df[shap_df['Feature'].isin(exam_features)].iloc[0]['Feature']
    
    demo_advice = advice_mapping[top_demographic_feature]
    exam_advice = advice_mapping[top_exam_feature]
        
    return top_demographic_feature, top_exam_feature, demo_advice, exam_advice

# Define advice mapping
advice_mapping = {
    'weekly_self_study_hours': 
        """Your weekly self study hours has contributed the most among your demographics in predicting your performance.
        If this score is positive, means that your study hours has positively affected your performance, so keep it up.
        If this score is negative, means that it has negatively affected your performance, so try to study more weekly to improve your performance""",
        
    'career_aspiration_encoded': 
        """Your career aspirations has contributed the most among your demographics in predicting your performance.
        If this score is negative, consider seeking help from your teacher to clarify your aspirations, thus they can help you accordingly.""",
        
    'extracurricular_activities': 
        """Your participation in extracurricular activities has contributed the most among your demographics in predicting your performance.
        If this score is negative, it is suggested to reconsider your participation in these activities as it may have affected your academic performance.""",
        
    'part_time_job': 
        """Your part time job has contributed the most among your demographics in predicting your performance.
        If this score is negative, it is suggested to reconsider your part time job involvement as it may have affected your academic performance.""",
        
    'absence_days': 
        """Your number of days being absent to school has contributed the most among your demographics in predicting your performance.
        If this score is negative, reduce this number and attend school as this has negatively affected your academic performance.""",
        
    'english_score': 
        """Your exam score in English has contributed the most among other subjects in predicting your performance.
        Keep up your performance in English if you have scored highly, otherwise, try put more time into the subject to improve your exam score.""",
    
    'geography_score': 
        """Your exam score in Geography has contributed the most among other subjects in predicting your performance.
        Keep up your performance in Geography if you have scored highly, otherwise, try put more time into the subject to improve your exam score.""",
        
    'history_score': 
        """Your exam score in History has contributed the most among other subjects in predicting your performance.'
        Keep up your performance in History if you have scored highly, otherwise, try put more time into the subject to improve your exam score.""",
        
    'math_score': 
        """Your exam score in Mathematics has contributed the most among other subjects in predicting your performance.
        Keep up your performance in Math if you have scored highly, otherwise, try put more time into practice Math problems or seek help from teachers.""",
          
    'physics_score': 
        """Your exam score in Physics has contributed the most among other subjects in predicting your performance.
        Keep up your performance in Physics if you have scored highly, otherwise, try put more time into the subject to improve your exam score.""",
        
    'chemistry_score': 
        """Your exam score in Chemistry has contributed the most among other subjects in predicting your performance.
        Keep up your performance in Chemistry if you have scored highly, otherwise, try put more time into the subject to improve your exam score.""",
        
    'biology_score': 
        """Your exam score in Biology has contributed the most among other subjects in predicting your performance.
        Keep up your performance in Biology if you have scored highly, otherwise, try put more time into the subject to improve your exam score."""
}

if predict_button == True:
    # Rearrange the inputs in order with the predictive model
    input_data = get_input_data(job, days, ex_act, hrs, hist, phy, chem, bio, eng, geo, career, math)
        
    input_data_scaled = scaler.transform(input_data)    # Scale the input data
    prediction = model.predict(input_data_scaled)     # Obtain predictive value
    
    demographic_features = ['weekly_self_study_hours', 'career_aspiration_encoded', 
                            'extracurricular_activities', 'part_time_job', 'absence_days']
    exam_features = ['english_score', 'geography_score', 'history_score', 'math_score', 
                     'physics_score', 'chemistry_score', 'biology_score']
    
    # Display predicted score
    st.header("Prediction Analysis")
    st.markdown(f"""
                <div style='background-color: #f0f0f0; padding: 10px; box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); font-size: 18px;'>
                Your Predicted Average Score: {prediction}
                </div>
                """, unsafe_allow_html=True)
    
    # Loading analysis
    with st.spinner('Analyzing, please wait...'):
        fc = feature_contributions(explainer, input_data_scaled, X.columns.tolist())
        
        shap_values = explainer(input_data_scaled)
       
    # Containers for analysis 
    row1 = st.columns(2)
    row2 = st.columns(2)
    row3 = st.columns(1)
    row4 = st.columns(1)
    row5 = st.columns(1)
    container1 = row1[0].container()
    container2 = row2[0].container()
    container3 = row3[0].container()
    container4 = row4[0].container()
    container5 = row5[0].container()

    # Table of feature contributions (SHAP values)
    with container1:        
        st.header("Feature Contributions")
        st.table(fc)
    
    # Summary plot    
    with container2:
        st.header("Summary Plot")
        fig = plt.figure(figsize=(6,8))
        sp.summary_plot(shap_values, input_data_scaled, feature_names=X.columns.tolist(), show=False)
        st.pyplot(fig)
    
    # Info on how to read plot and SHAP values
    with container3:
        st.info("""**How to interpret:**
                    The expected score is the average predicted score of the student population.
                    Features with positive (+) score values increases your predicted average score.
                    Features with negative (-) score values decreases your predicted average score.""")
           
    # Personal insights and suggestions
    top_demo, top_exam, demo_advice, exam_advice = generate_advice(fc, demographic_features, exam_features, advice_mapping)
    
    with container4:
        st.header("Recommendations")
        st.markdown(f"""
                    <div style= 'background-color: #fffde0; padding: 10px; border-radius: 5px; box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);'>
                    <strong>👥 Top demographic feature:</strong> {top_demo}<br><br>
                    <strong>What it means:</strong> {demo_advice}
                    </div>
                    """, unsafe_allow_html=True)
        
    with container5:
        st.markdown(f"""
                    <div style= 'background-color: #f0ffe0; padding: 10px; border-radius: 5px; box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);'>
                    <strong>📝 Top exam score feature:</strong> {top_exam}<br><br>
                    <strong>What it means:</strong> {exam_advice}
                    </div>
                    """, unsafe_allow_html=True)
    

import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pickle
import bz2


def decompress_pickle(file: str):
    data = bz2.BZ2File(file, 'rb')
    data = pickle.load(data)
    return data
    
def load_data(model=None, scaler=None):
    jsonify = {}
    # loading and decompressing model
    path = './models/random_forest.pbz2'
    model = decompress_pickle(path)
    
    # load scaler data
    path = './src/helpers/scaler.pbz2'
    scaler = decompress_pickle(path)
    jsonify = {'model': model, 'scaler': scaler}
    return jsonify


def get_feature_names():
    list_of_features = []
    target = None
    with open('./src/features/feature_names.txt', 'r') as f:
        for line in f:
            list_of_features.append(line.strip())

    # getting the name of the target name 'Exited'
    if 'Exited' in list_of_features:
        target = list_of_features.pop(list_of_features.index('Exited'))
    predictor = list_of_features
    return (predictor, target)
   
   
Geography = ('France','Spain', 'Germany')
Gender = ('Male', 'Female')
Card_Type = ('DIAMOND', 'GOLD', 'PLATINUM', 'SILVER')
HasCrCard = ('Yes', 'No')
IsActiveMember = ('Yes', 'No')


def predict_page():
    st.title('Bank Customer Churn Predicton')
    st.write("""##### Fill in the following requirement to make some predictions.""")
    creditscore = st.text_input('Enter credit score')
    age = st.number_input('Enter age', 15, 200)
    tenure = st.slider('How long have you been with the bank?', 1, 10, 2)
    balance = st.number_input('What is your current balance?')
    NOP = st.slider('What is the number of products ypu have purchase from the bank?')
    hasCreditCard = st.radio('Do you have a credit card?', HasCrCard)
    isActiveMember = st.radio('Are you an active member?',IsActiveMember)
    estimatedSalary = st.number_input('What is your take home salary?', 100)
    satisfactionScore = st.slider('Select a satisfaction score', 1, 5, 3)
    pointEarned = st.slider('What is your point earned with the bank?', 100, 1000, 300)
    geography = st.selectbox('Select your geographical area', Geography)
    gender = st.radio('What is your gender?', Gender)
    cardType = st.selectbox('Select your credit card type', Card_Type)
    
    st.divider()
    button_pressed = st.button('Predict!', help='Click to make prediction')
    
    if button_pressed:
        predictor = np.array([
            creditscore,
            age,
            tenure,
            balance,
            NOP,
            hasCreditCard,
            isActiveMember,
            estimatedSalary,
            satisfactionScore,
            pointEarned,
            geography,
            gender,
            cardType
        ])
        
        json_data = load_data()
        model, scaler = json_data['model'], json_data['scaler']
        
        print('Almost done')
        # preprocess received data
        scaled_data = scaler.transform(predictor)
        result = model.predict(scaled_data)
        
        
        st.subheader(result)
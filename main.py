import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pickle
import bz2


def load_data():
    # loading and decompressing model
    path_1 = './models/random_forest.pbz2'
    data = bz2.BZ2File(path_1, 'rb')
    model = pickle.load(data) 

    # load scaler data
    path_2 = './src/helpers/scaler.pkl'
    data = open(path_2, 'rb')
    scaler = pickle.load(data) 
    return model, scaler


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
    creditscore = st.number_input('Enter credit score')
    age = st.number_input('Enter age', 15, 200)
    tenure = int(st.slider('How long have you been with the bank?', 1, 10, 2))
    balance = st.number_input('What is your current balance?')
    NOP = int(st.slider('What is the number of products you have purchase from the bank?'))
    hasCreditCard = st.radio('Do you have a credit card?', HasCrCard)
    isActiveMember = st.radio('Are you an active member?',IsActiveMember)
    estimatedSalary = st.number_input('What is your take home salary?', 100)
    satisfactionScore = st.slider('Select a satisfaction score', 1, 5, 3)
    pointEarned = st.slider('What is your point earned with the bank?', 100, 1000, 300)
    geography = st.selectbox('Select your geographical area', Geography)
    gender = st.radio('What is your gender?', Gender)
    cardType = st.selectbox('Select your credit card type', Card_Type)
    
    # converting input to desired format
    #Has Credit Card
    for item in HasCrCard:
        if item == hasCreditCard:
            hasCreditCard = 1
        elif item == hasCreditCard:
            hasCreditCard = 0
        
    #Is active member
    for item in IsActiveMember:
        if item == isActiveMember:
            isActiveMember = 1
        elif item == isActiveMember:
            isActiveMember = 0
    
    #Geographical of the user
    for item in Geography:
        if item == geography:
            geography = 1
        elif item == geography:
            geography = 2
        elif item == geography:
            geography = 3
        
    #Gender of the user
    for item in Gender:
        if item == gender:
            gender = 1
        elif item == gender:
            gender = 0
        
    #Card type of the user
    for item in Card_Type:
        if item == cardType:
            cardType = 1
        elif item == cardType:
            cardType = 0
    
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
        
        model, scaler = load_data()     
        
        
        print('Almost done')
        # preprocess received data
        scaled_data = scaler.transform(predictor)
        result = model.predict(scaled_data)
        
        
        st.subheader(result)
        
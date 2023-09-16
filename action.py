import streamlit as st
import streamlit.components.v1 as components
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


def predict_page():
    st.title('Bank Customer Churn Prediciton')
    st.write("""##### Fill in the following requirement to make some predictions.""")
   
   
   
temp =['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary',\
    'Satisfaction Score', 'Point Earned', 'Geography_France', 'Geography_Germany', 'Geography_Spain', 'Gender_Female',\
        'Gender_Male', 'Card Type_DIAMOND', 'Card Type_GOLD', 'Card Type_PLATINUM', 'Card Type_SILVER']


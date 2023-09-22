import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pickle
import bz2


def load_data():
    # loading and decompressing model
    path_1 = "./models/random_forest.pbz2"
    data = bz2.BZ2File(path_1, "rb")
    model = pickle.load(data)

    # load scaler data
    path_2 = "./src/helpers/scaler.pkl"
    data = open(path_2, "rb")
    scaler = pickle.load(data)
    return model, scaler


Geography = ("France", "Spain", "Germany")
Gender = ("Male", "Female")
Card_Type = ("DIAMOND", "GOLD", "PLATINUM", "SILVER")
HasCrCard = ("Yes", "No")
IsActiveMember = ("Yes", "No")
Complain = ("Yes", "No")


def predict_page():
    st.title("Bank Customer Churn Predicton :bank:")
    st.write("""##### Fill in the following requirement to make some predictions.""")
    creditscore = st.number_input("Enter credit score")
    age = st.number_input("Enter age", 15, 200)
    tenure = int(st.slider("How long have you been with the bank?", 1, 10, 2))
    balance = st.number_input("What is your current balance?")
    NOP = int(
        st.slider("What is the number of products you have purchase from the bank?")
    )
    hasCreditCard = st.radio("Do you have a credit card?", HasCrCard)
    isActiveMember = st.radio("Are you an active member?", IsActiveMember)
    estimatedSalary = st.number_input("What is your take home salary?", 100)
    complain = st.radio(
        "Have ever made complained to the bank's customer service before?", Complain
    )
    satisfactionScore = st.slider("Select a satisfaction score", 1, 5, 3)
    pointEarned = st.slider("What is your point earned with the bank?", 100, 1000, 300)
    geography_any = st.selectbox("Select your geographical area", Geography)
    gender_any = st.radio("What is your gender?", Gender)
    cardType_any = st.selectbox("Select your credit card type", Card_Type)

    # converting input to desired format
    # Has Credit Card
    for item in HasCrCard:
        if item == hasCreditCard:
            hasCreditCard = 1
        elif item == hasCreditCard:
            hasCreditCard = 0

    # Is active member
    for item in IsActiveMember:
        if item == isActiveMember:
            isActiveMember = 1
        elif item == isActiveMember:
            isActiveMember = 0

    # customer complains
    for item in Complain:
        if item == complain:
            complain = 1
        elif item == complain:
            complain = 0

    # Geographical of the user
    Geography_France, Geography_Germany, Geography_Spain = None, None, None
    if geography_any == "France":
        Geography_France = 1
        Geography_Germany = 0
        Geography_Spain = 0
    elif geography_any == "Germany":
        Geography_France = 0
        Geography_Germany = 1
        Geography_Spain = 0
    else:
        Geography_France = 0
        Geography_Germany = 0
        Geography_Spain = 1

    # Gender of the user
    Gender_Female, Gender_Male = None, None
    if gender_any == "Female":
        Gender_Female = 1
        Gender_Male = 0
    else:
        Gender_Female = 0
        Gender_Male = 1

    # Card type of the user
    Card_Type_DIAMOND, Card_Type_GOLD, Card_Type_PLATINUM, Card_Type_SILVER = (
        None,
        None,
        None,
        None,
    )
    if cardType_any == "DIAMOND":
        Card_Type_DIAMOND = 1
        Card_Type_GOLD = 0
        Card_Type_PLATINUM = 0
        Card_Type_SILVER = 0
    elif cardType_any == "GOLD":
        Card_Type_DIAMOND = 0
        Card_Type_GOLD = 1
        Card_Type_PLATINUM = 0
        Card_Type_SILVER = 0
    elif cardType_any == "PLATINUM":
        Card_Type_DIAMOND = 0
        Card_Type_GOLD = 0
        Card_Type_PLATINUM = 1
        Card_Type_SILVER = 0
    else:
        Card_Type_DIAMOND = 0
        Card_Type_GOLD = 0
        Card_Type_PLATINUM = 0
        Card_Type_SILVER = 1

    st.divider()
    button_pressed = st.button("Predict!", help="Click to make prediction")

    if button_pressed:
        predictor = np.array(
            [
                [
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
                    Geography_France,
                    Geography_Germany,
                    Geography_Spain,
                    Gender_Female,
                    Gender_Male,
                    Card_Type_DIAMOND,
                    Card_Type_GOLD,
                    Card_Type_PLATINUM,
                    Card_Type_SILVER,
                ]
            ]
        )

        # loading model and scler for cleannig the inputs
        model, scaler = load_data()

        # preprocess received data
        scaled_data = scaler.transform(predictor)
        result = model.predict(scaled_data)

        # if a successful prediction

        if result[0] == 1:
            message = "Customer successfully churn :thumbsdown:"
            st.subheader(message)
        else:
            message = "Customer successfully didn't churned :thumbsup:"
            st.subheader(message)


def tab():
    st.sidebar.write('Contibute to this project using the link below :arrow_down:')
    # Display the image as a clickable link
    github_repository_url = 'https://github.com/juliusmarkwei/Customer-Churn-EDA-Balancing-and-ML'

    # Create a link with the image inside it
    st.sidebar.markdown(f'<a href="{github_repository_url}">GitHub</a>', unsafe_allow_html=True)

import streamlit as st
from main import predict_page, tab
from explore import show_explore_page


def explore():
    selection = st.sidebar.selectbox(
        ":Yellow[What do you want to know about my project?]",
        ("Make predictions", "Explore Data"),
    )
    return selection


def img():
    image_object = st.sidebar.image(
        "https://cdn.analyticsvidhya.com/wp-content/uploads/2020/05/Churn-Prediction-scaled.jpg"
    )
    return image_object


if __name__ == "__main__":
    ok = explore()
    img()

    if ok == "Make predictions":
        predict_page()
    else:
        show_explore_page()

    tab()

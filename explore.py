import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importing dataframe for some exploration purposes
df = pd.read_csv("./data/raw/Customer-Churn-Records.csv")


def show_explore_page():
    st.write("""### Exploration on the Customer Churn Database""")

    global df
    fig = plt.figure(figsize=(10, 5))
    axes = fig.add_subplot()
    axes.hist(x=df[['Satisfaction Score']], density=True, align='mid')
    st.pyplot(fig)


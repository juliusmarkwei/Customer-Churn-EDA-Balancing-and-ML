import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# importing dataframe for some exploration purposes
df = pd.read_csv("./data/raw/Customer-Churn-Records.csv")


def show_explore_page():
    st.write("""### Exploration on the Customer Churn Database""")

    global df
    geo_counts = df["Geography"].value_counts()
    fig = go.Figure(data=[go.Bar(x=geo_counts.index, y=geo_counts.values)])

    # Set plot title and axis labels
    fig.update_layout(
        title="Geography Distribution of the Train/Test Data",
        xaxis_title="Geography",
        yaxis_title="Count",
    )

    # Display the plot using Streamlit
    st.plotly_chart(fig)

    # second chart
    # Group the data by "Geography" and calculate the Exited counts
    geo_Exited_counts = (
        df.groupby(["Geography", "Exited"]).size().unstack(fill_value=0).reset_index()
    )

    # Create a grouped bar chart using Plotly
    fig = go.Figure(
        data=[
            go.Bar(
                x=geo_Exited_counts["Geography"],
                y=geo_Exited_counts[1],
                name="Exiteded",
                marker_color="yellow",
            ),
            go.Bar(
                x=geo_Exited_counts["Geography"],
                y=geo_Exited_counts[0],
                name="Not Exiteded",
                marker_color="orange",
            ),
        ]
    )

    # Set plot title and axis labels
    fig.update_layout(
        title="Geography Exited Counts",
        xaxis_title="Geography",
        yaxis_title="Count",
        barmode="group",  # To create grouped bars
    )

    # Display the plot using Streamlit
    st.plotly_chart(fig)

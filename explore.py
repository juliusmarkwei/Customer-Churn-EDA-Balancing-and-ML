import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# importing dataframe for some exploration purposes
df = pd.read_csv("./data/raw/Customer-Churn-Records.csv")


def show_explore_page():
    st.write("""### Exploration on the Customer Churn Database""")

    global df
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

    # Group the data by "Card Type" and calculate the exit counts
    credit_card_exit_counts = (
        df.groupby(["Card Type", "Exited"]).size().unstack(fill_value=0).reset_index()
    )

    # Create a grouped bar chart using Plotly with cool colors
    cool_colors = [
        "#1f77b4",
        "#2ca02c",
    ]  # Blue and green colors for "Exited" and "Not Exited"

    fig = go.Figure(
        data=[
            go.Bar(
                x=credit_card_exit_counts["Card Type"],
                y=credit_card_exit_counts[1],
                name="Exited",
                marker_color=cool_colors[0],
            ),
            go.Bar(
                x=credit_card_exit_counts["Card Type"],
                y=credit_card_exit_counts[0],
                name="Not Exited",
                marker_color=cool_colors[1],
            ),
        ]
    )

    # Set plot title and axis labels
    fig.update_layout(
        title="Card Type Exit Counts",
        xaxis_title="Card Type",
        yaxis_title="Count",
        barmode="group",  # To create grouped bars
    )

    # Display the plot using Streamlit
    st.plotly_chart(fig)
    
    

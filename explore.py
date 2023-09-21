import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# importing dataframe for some exploration purposes
df = pd.read_csv("./data/raw/Customer-Churn-Records.csv")


def show_explore_page():
    st.write("""### Exploration on the Customer Churn Database""")
    st.write("Note: The train/test data combined was used for the visualization")

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
                marker_color="#bf9a40",
            ),
            go.Bar(
                x=geo_Exited_counts["Geography"],
                y=geo_Exited_counts[0],
                name="Not Exiteded",
                marker_color="#c03f77",
            ),
        ]
    )

    # Set plot title and axis labels
    fig.update_layout(
        title="Customers Churn Status based on their Location".center(150),
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

    # Create a stacked bar chart using Plotly with cool colors
    cool_colors = [
        "#5EA35C",
        "#8045ba",
    ]  # Blue and green colors for "Exited" and "Not Exited"

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=credit_card_exit_counts["Card Type"],
            y=credit_card_exit_counts[1],
            name="Customer Left",
            marker_color=cool_colors[0],
        )
    )

    fig.add_trace(
        go.Bar(
            x=credit_card_exit_counts["Card Type"],
            y=credit_card_exit_counts[0],
            name="Customer Stayed",
            marker_color=cool_colors[1],
        )
    )

    # Set plot title and axis labels
    fig.update_layout(
        title="Customer Churn Status based on their Card Type".center(150),
        xaxis_title="Card Type",
        yaxis_title="Count",
        barmode="stack",  # To create stacked bars
    )

    # Display the plot using Streamlit
    st.plotly_chart(fig)


    # Define age category bins and labels
    age_bins = [0, 30, 40, 50, float("inf")]
    age_labels = ["Under 30", "30-40", "40-50", "Over 50"]

    # Create a new column in the DataFrame with age categories
    df["Age Category"] = pd.cut(df["Age"], bins=age_bins, labels=age_labels)

    # Count the occurrences of each age category
    age_category_counts = df["Age Category"].value_counts().reset_index()

    # Rename the columns for clarity
    age_category_counts.columns = ["Age Category", "Count"]

    # Create a custom color palette
    colors = ["#3EB8C1", "#C1A33E", "#C1473E", "#53E31C"]

    # Create a Pie Chart using Plotly Express with custom styling
    fig = px.pie(
        age_category_counts,
        values="Count",
        names="Age Category",
        title="Age Category Distribution According to Catogories".center(160),
        color_discrete_sequence=colors,  # Set custom colors
        hole=0.5,
    )

    # Add labels inside the pie chart
    fig.update_traces(
        textinfo="percent+label",
        textfont_size=14,
        pull=[0.08, 0.08, 0.08, 0.08]
    )

    # Customize the layout and appearance
    fig.update_layout(
        legend=dict(
            x=0.85,
            y=0.5,  # Adjust the legend position
            bgcolor="rgba(255, 255, 255, 0.7)",
            bordercolor="gray",
            borderwidth=1,
        ),
        margin=dict(l=0, r=0, b=0, t=30),  # Adjust the chart margins
    )

    # Display the styled Pie Chart using Streamlit
    st.plotly_chart(fig)

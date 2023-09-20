import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importing dataframe for some exploration purposes
df = pd.read_csv("./data/raw/Customer-Churn-Records.csv")


def show_explore_page():
    st.write("""### Exploration on the Customer Churn Database""")

    global df
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.patches import ConnectionPatch

    # Create sample data for geography counts
    geography_counts = dict(df["Geography"].value_counts())
    labels = list(geography_counts.keys())
    counts = list(geography_counts.values())

    # make figure and assign axis objects
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 5))
    fig.subplots_adjust(wspace=0.5)

    # Pie chart parameters
    overall_ratios = [0.27, 0.56, 0.17]
    explode = [0.1, 0, 0]
    angle = -180 * overall_ratios[0]
    wedges, *_ = ax1.pie(
        overall_ratios,
        autopct="%1.1f%%",
        startangle=angle,
        labels=labels,
        explode=explode,
    )

    # Bar chart parameters
    age_ratios = [0.33, 0.54, 0.07, 0.06]
    age_labels = ["Under 35", "35-49", "50-65", "Over 65"]
    bottom = 1
    width = 0.2

    # Adding from the top matches the legend.
    for j, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):
        bottom -= height
        bc = ax2.bar(
            0,
            height,
            width,
            bottom=bottom,
            color="C0",
            label=label,
            alpha=0.1 + 0.25 * j,
        )
        ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type="center")

    ax2.set_title("Age of approvers")
    ax2.legend()
    ax2.axis("off")
    ax2.set_xlim(-2.5 * width, 2.5 * width)

    # Use ConnectionPatch to draw lines between the two plots
    theta1, theta2 = wedges[0].theta1, wedges[0].theta2
    center, r = wedges[0].center, wedges[0].r
    bar_height = sum(age_ratios)

    # Draw top connecting line
    x = r * np.cos(np.pi / 180 * theta2) + center[0]
    y = r * np.sin(np.pi / 180 * theta2) + center[1]
    con = ConnectionPatch(
        xyA=(-width / 2, bar_height),
        coordsA=ax2.transData,
        xyB=(x, y),
        coordsB=ax1.transData,
    )
    con.set_color([0, 0, 0])
    con.set_linewidth(4)
    ax2.add_artist(con)

    # Draw bottom connecting line
    x = r * np.cos(np.pi / 180 * theta1) + center[0]
    y = r * np.sin(np.pi / 180 * theta1) + center[1]
    con = ConnectionPatch(
        xyA=(-width / 2, 0), coordsA=ax2.transData, xyB=(x, y), coordsB=ax1.transData
    )
    con.set_color([0, 0, 0])
    ax2.add_artist(con)
    con.set_linewidth(4)

    # Create a pie chart subplot for geography data
    ax3.pie(counts, labels=labels, autopct="%1.1f%%", startangle=90)
    ax3.set_title("Geography Distribution")
    ax3.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
    st.pyplot(fig)


print(dict(df["Geography"].value_counts()))

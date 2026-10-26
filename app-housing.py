import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("California Housing Data (1990) by Peng Qiwei")

# Load data
df = pd.read_csv("housing.csv")

# House value slider
house_value_filter = st.slider(
    "Minimal Median House Value",
    0,
    500001,
    200000
)

# Sidebar reminder
st.subheader("See more filters in the sidebar:")

# Location type multiselect
location_filter = st.sidebar.multiselect(
    "Choose the location type",
    df["ocean_proximity"].unique(),
    df["ocean_proximity"].unique()
)

# Income level radio
income_filter = st.sidebar.radio(
    "Choose income level",
    ["Low", "Medium", "High"]
)

# Filter by house value
df = df[df["median_house_value"] >= house_value_filter]

# Filter by ocean proximity
df = df[df["ocean_proximity"].isin(location_filter)]

# Filter by income level
if income_filter == "Low":
    df = df[df["median_income"] <= 2.5]

elif income_filter == "Medium":
    df = df[
        (df["median_income"] > 2.5) &
        (df["median_income"] < 4.5)
    ]

else:
    df = df[df["median_income"] >= 4.5]

# Map
st.map(df)

# Histogram
st.subheader("Median House Value Distribution")

fig, ax = plt.subplots()

ax.hist(
    df["median_house_value"],
    bins=30
)

ax.set_xlabel("Median House Value")
ax.set_ylabel("Number of Districts")

st.pyplot(fig)

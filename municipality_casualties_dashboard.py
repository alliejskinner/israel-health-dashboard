
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_excel("total_casualties_by_municipality.xlsx")

df = load_data()

# Convert numeric columns
df["Total Casualties"] = pd.to_numeric(df["Total Casualties"], errors="coerce")
df["Total Deaths"] = pd.to_numeric(df["Total Deaths"], errors="coerce")
df["Currently Hospitalized"] = pd.to_numeric(df["Currently Hospitalized"], errors="coerce")

# Sidebar filter
top_n = st.sidebar.slider("Select number of municipalities to display:", 5, 20, 10)

# Select metric
metric = st.sidebar.selectbox(
    "Choose metric to visualize:",
    ["Total Casualties", "Total Deaths", "Currently Hospitalized"]
)

# Sort and filter data
top_data = df.sort_values(by=metric, ascending=False).head(top_n)

# Bar chart
fig = px.bar(
    top_data,
    x="Municipality",
    y=metric,
    title=f"Top {top_n} Municipalities by {metric}",
    labels={"Municipality": "Municipality", metric: metric},
    text_auto=True
)
fig.update_layout(xaxis_tickangle=-45)

st.title("Casualties Dashboard by Municipality")
st.plotly_chart(fig)


import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("health_indicators_isr_cleaned.csv")

df = load_data()

# Language dictionary for UI labels
lang_dict = {
    "title": {
        "en": "Israel Health Dashboard",
        "he": "לוח בקרה לבריאות בישראל"
    },
    "indicator_label": {
        "en": "Select Health Indicator:",
        "he": "בחר מדד בריאות:"
    },
    "sex_filter": {
        "en": "Filter by Sex (optional):",
        "he": "סינון לפי מגדר (רשות):"
    },
    "show_data": {
        "en": "Show raw data",
        "he": "הצג נתונים גולמיים"
    },
    "chart_title": {
        "en": "{} Over Time",
        "he": "{} לאורך זמן"
    }
}

# Sidebar language toggle
language = st.sidebar.radio("Language / שפה", ["English", "עברית"])
lang = "en" if language == "English" else "he"

st.title(lang_dict["title"][lang])

# Sidebar: Indicator selection
indicator_options = df['Indicator_Name'].unique()
selected_indicator = st.sidebar.selectbox(lang_dict["indicator_label"][lang], indicator_options)

# Filter by selected indicator
filtered_df = df[df['Indicator_Name'] == selected_indicator]

# Optional sex filter
if filtered_df['Sex'].notna().sum() > 0:
    sex_options = filtered_df['Sex'].dropna().unique()
    selected_sex = st.sidebar.selectbox(lang_dict["sex_filter"][lang], ['All'] + list(sex_options))
    if selected_sex != 'All':
        filtered_df = filtered_df[filtered_df['Sex'] == selected_sex]

# Plotting
fig = px.line(
    filtered_df.sort_values("Year"),
    x="Year", y="Value",
    markers=True,
    title=lang_dict["chart_title"][lang].format(selected_indicator)
)
st.plotly_chart(fig)

# Raw data
with st.expander(lang_dict["show_data"][lang]):
    st.write(filtered_df)

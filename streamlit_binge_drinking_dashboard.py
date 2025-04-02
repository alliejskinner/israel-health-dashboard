
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("alcohol_heavy_drinking_israel.csv")
    return df[df["Year"].between(2015, 2025)]

df = load_data()

# Language dictionary
lang_dict = {
    "title": {
        "en": "Heavy Episodic Drinking in Israel (Ages 15+)",
        "he": "שתיית אלכוהול מופרזת בישראל (גילאי 15+)"
    },
    "description": {
        "en": "Percentage of population engaging in heavy episodic drinking, by sex (2015–2025).",
        "he": "אחוז האוכלוסייה ששותה שתייה מופרזת לפי מגדר (2015–2025)."
    },
    "select_lang": {
        "en": "Language / שפה",
        "he": "Language / שפה"
    },
    "axis_label_y": {
        "en": "Percentage (%)",
        "he": "אחוז (%)"
    },
    "axis_label_x": {
        "en": "Year",
        "he": "שנה"
    }
}

# Language selector
language = st.sidebar.radio(lang_dict["select_lang"]["en"], ["English", "עברית"])
lang = "en" if language == "English" else "he"

# Title and description
st.title(lang_dict["title"][lang])
st.markdown(lang_dict["description"][lang])

# Plot
fig = px.line(
    df,
    x="Year",
    y="Value",
    color="Sex",
    markers=True,
    labels={
        "Value": lang_dict["axis_label_y"][lang],
        "Year": lang_dict["axis_label_x"][lang],
        "Sex": "Sex / מגדר"
    },
)

fig.update_layout(
    legend_title_text="Sex / מגדר",
    xaxis=dict(tickmode='linear'),
)

st.plotly_chart(fig)

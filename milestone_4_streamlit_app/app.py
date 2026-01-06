import streamlit as st

st.set_page_config(page_title="Skill Gap Analysis", layout="wide")

st.title("Skill Gap Analysis Dashboard")
st.write(
    "This Streamlit application analyzes the skill gap between a candidate resume "
    "and a job description."
)

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.write("Upload Files")
st.sidebar.write("Analysis")
st.sidebar.write("Download Report")


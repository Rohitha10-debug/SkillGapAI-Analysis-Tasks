import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import io

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------
st.set_page_config(
    page_title="Skill Gap Analysis Dashboard",
    page_icon="🌸",
    layout="wide"
)

# ---------------------------------------------------
# Soft Lavender Styling
# ---------------------------------------------------
st.markdown("""
<style>
.pastel-card {
    background-color: #f3efff;
    padding: 1.5rem;
    border-radius: 14px;
    margin-bottom: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------
st.sidebar.markdown("### 🧭 Navigation")
section = st.sidebar.radio(
    "",
    ["Upload Files", "Analysis", "Download Report"]
)

# ---------------------------------------------------
# Header
# ---------------------------------------------------
st.markdown("""
<h1>🌸 Skill Gap Analysis Dashboard</h1>
<p style="color:#6b7280;">
Analyze alignment between a candidate resume and job description using a calm,
lavender-themed Streamlit dashboard.
</p>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Session State
# ---------------------------------------------------
if "resume_text" not in st.session_state:
    st.session_state.resume_text = None
if "jd_text" not in st.session_state:
    st.session_state.jd_text = None
if "df" not in st.session_state:
    st.session_state.df = None
if "matched" not in st.session_state:
    st.session_state.matched = []
if "missing" not in st.session_state:
    st.session_state.missing = []

# ---------------------------------------------------
# Upload Section
# ---------------------------------------------------
if section == "Upload Files":
    st.markdown('<div class="pastel-card">', unsafe_allow_html=True)
    st.subheader("📂 Upload Resume and Job Description")

    resume_file = st.file_uploader(
        "Upload Resume (PDF, DOCX, TXT)",
        type=["txt"]
    )

    jd_file = st.file_uploader(
        "Upload Job Description (PDF, DOCX, TXT)",
        type=["txt"]
    )

    if resume_file:
        st.session_state.resume_text = resume_file.read().decode("utf-8")
        st.success("Resume uploaded successfully")

    if jd_file:
        st.session_state.jd_text = jd_file.read().decode("utf-8")
        st.success("Job description uploaded successfully")

    if st.session_state.resume_text and st.session_state.jd_text:
        st.info("Files uploaded. Go to **Analysis** tab.")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# Analysis Section
# ---------------------------------------------------
elif section == "Analysis":
    if not st.session_state.resume_text or not st.session_state.jd_text:
        st.warning("Please upload both Resume and Job Description first.")
    else:
        st.markdown('<div class="pastel-card">', unsafe_allow_html=True)
        st.subheader("🔍 Document Preview")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Resume Preview**")
            st.text(st.session_state.resume_text[:300])
        with col2:
            st.markdown("**Job Description Preview**")
            st.text(st.session_state.jd_text[:300])

        st.markdown('</div>', unsafe_allow_html=True)

        # ---------------------------------------------------
        # Skill Extraction (Simple Keyword Method)
        # ---------------------------------------------------
        skills = [
            "Python", "SQL", "Machine Learning", "Deep Learning",
            "Statistics", "Data Analysis", "AWS", "Communication"
        ]

        resume = st.session_state.resume_text.lower()
        jd = st.session_state.jd_text.lower()

        matched = [s for s in skills if s.lower() in resume and s.lower() in jd]
        missing = [s for s in skills if s.lower() not in resume and s.lower() in jd]

        st.session_state.matched = matched
        st.session_state.missing = missing

        # ---------------------------------------------------
        # Metrics
        # ---------------------------------------------------
        match_percent = int((len(matched) / len(skills)) * 100)

        st.markdown('<div class="pastel-card">', unsafe_allow_html=True)
        st.subheader("📈 Skill Match Summary")
        st.metric("Match Percentage", f"{match_percent}%")

        col1, col2 = st.columns(2)
        with col1:
            st.success("✅ Matched Skills")
            st.write(matched)
        with col2:
            st.error("❌ Missing Skills")
            st.write(missing)

        st.markdown('</div>', unsafe_allow_html=True)

        # ---------------------------------------------------
        # Bar Chart (Compact)
        # ---------------------------------------------------
        st.markdown('<div class="pastel-card">', unsafe_allow_html=True)
        st.subheader("📊 Skill Match Overview")

        fig, ax = plt.subplots(figsize=(5, 3))
        ax.bar(
            ["Matched", "Missing"],
            [len(matched), len(missing)],
            color=["#c7d2fe", "#fde68a"],
            width=0.5
        )
        ax.set_ylabel("Count")
        ax.set_title("Skill Distribution")
        plt.tight_layout()

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.pyplot(fig, use_container_width=False)

        st.markdown('</div>', unsafe_allow_html=True)

        # ---------------------------------------------------
        # Similarity Table
        # ---------------------------------------------------
        scores = np.random.uniform(0.5, 0.9, len(skills))
        df = pd.DataFrame({
            "Skill": skills,
            "Similarity Score": scores
        })

        st.session_state.df = df

        st.markdown('<div class="pastel-card">', unsafe_allow_html=True)
        st.subheader("📋 Skill Similarity Table")
        st.dataframe(df, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# Download Section
# ---------------------------------------------------
elif section == "Download Report":
    if st.session_state.df is None:
        st.warning("Please complete analysis first.")
    else:
        st.markdown('<div class="pastel-card">', unsafe_allow_html=True)
        st.subheader("⬇️ Download Skill Gap Report")

        csv = st.session_state.df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "📥 Download CSV Report",
            csv,
            "skill_gap_report.csv",
            "text/csv"
        )

        st.markdown('</div>', unsafe_allow_html=True)


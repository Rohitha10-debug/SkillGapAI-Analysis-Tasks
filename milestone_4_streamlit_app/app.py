import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Skill Gap Analysis", layout="wide")

# ---------------- UI HEADER ----------------
st.title("Skill Gap Analysis Dashboard")
st.write(
    "This Streamlit application analyzes the skill gap between a candidate resume "
    "and a job description."
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("Navigation")
st.sidebar.write("Upload Files")
st.sidebar.write("Analysis")
st.sidebar.write("Download Report")

st.divider()

# ---------------- SESSION STATE ----------------
if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

# ---------------- FILE UPLOAD ----------------
st.header("Upload Resume and Job Description")

resume_file = st.file_uploader(
    "Upload Resume (PDF, DOCX, TXT)", type=["txt", "pdf", "docx"]
)

jd_file = st.file_uploader(
    "Upload Job Description (PDF, DOCX, TXT)", type=["txt", "pdf", "docx"]
)

def read_text(file):
    try:
        return file.read().decode("utf-8", errors="ignore")
    except:
        return ""

if resume_file and jd_file:
    resume_text = read_text(resume_file)
    jd_text = read_text(jd_file)

    st.success("Files uploaded successfully")

    # ---------------- PREVIEW ----------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Resume Preview")
        st.text(resume_text[:300])

    with col2:
        st.subheader("Job Description Preview")
        st.text(jd_text[:300])

    analyze = st.button("Analyze Skill Gap")

else:
    st.warning("Please upload both Resume and Job Description.")
    analyze = False

# ---------------- ANALYSIS ----------------
if analyze:
    st.session_state.analyzed = True

    skills = [
        "Python", "SQL", "Machine Learning", "Deep Learning",
        "AWS", "Statistics", "Data Analysis", "Communication"
    ]

    resume_lower = resume_text.lower()
    jd_lower = jd_text.lower()

    matched_skills = []
    missing_skills = []
    similarity_scores = []

    for skill in skills:
        if skill.lower() in resume_lower:
            matched_skills.append(skill)
            similarity_scores.append(0.9)
        else:
            missing_skills.append(skill)
            similarity_scores.append(0.2)

    match_percentage = int((len(matched_skills) / len(skills)) * 100)

    # ---------------- METRICS ----------------
    st.subheader("Skill Match Summary")
    st.metric("Skill Match Percentage", f"{match_percentage}%")

    col1, col2 = st.columns(2)

    with col1:
        st.success("Matched Skills")
        st.write(matched_skills)

    with col2:
        st.error("Missing Skills")
        st.write(missing_skills)

    # ---------------- BAR CHART ----------------
    st.subheader("Matched vs Missing Skills")

    fig, ax = plt.subplots()
    ax.bar(["Matched Skills", "Missing Skills"],
           [len(matched_skills), len(missing_skills)])
    st.pyplot(fig)

    # ---------------- TABLE ----------------
    st.subheader("Skill Similarity Scores")

    df = pd.DataFrame({
        "Skill": skills,
        "Similarity Score": similarity_scores
    })

    st.dataframe(df)

    # ---------------- CSV DOWNLOAD ----------------
    st.subheader("Download Skill Gap Report")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download CSV Report",
        data=csv,
        file_name="skill_gap_report.csv",
        mime="text/csv"
    )

# ---------------- ERROR HANDLING ----------------
if st.session_state.analyzed and not resume_text:
    st.error("Resume text could not be read.")

if st.session_state.analyzed and not jd_text:
    st.error("Job description text could not be read.")


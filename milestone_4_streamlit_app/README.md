# Milestone 4: Streamlit Skill Gap Analysis Dashboard

## Overview
This milestone focuses on building a complete interactive Streamlit dashboard
that performs end-to-end skill gap analysis between a candidate resume and a
job description.

The application allows users to upload documents, preview content, analyze
skill matches, visualize results, and export reports.

---

## Features Implemented

### 1. Streamlit UI
- Application title and short description
- Sidebar navigation for user guidance

### 2. File Upload
- Upload Resume and Job Description
- Supported formats: PDF, DOCX, TXT
- Displays uploaded file previews (first 300 characters)

### 3. Skill Gap Analysis
- Predefined technical and soft skills list
- Skill match percentage using Streamlit metrics
- Identifies matched skills and missing skills

### 4. Visualization
- Bar chart comparing matched vs missing skills
- Table showing skills and their similarity scores

### 5. Session State & Error Handling
- Uses Streamlit session state to preserve analysis results
- Handles empty uploads and unsupported formats gracefully

### 6. Report Export
- Allows users to download skill gap results as a CSV file

---

## Technologies Used
- Python
- Streamlit
- Pandas
- Matplotlib

---

## How to Run the Application

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

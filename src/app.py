import streamlit as st
import pandas as pd
import os
import numpy as np

# --- Placeholder for the actual matching pipeline ---
def run_matching_pipeline(job_description, resume_files):
    """
    This is a placeholder function. In a real application, this function
    would call the project's core logic to process and match the resumes.
    """
    # Simulate some results
    results = []
    for resume_file in resume_files:
        results.append({
            "resume_filename": resume_file.name,
            "score": np.random.randint(70, 95),
            "matching_skills": ["Python", "Data Analysis", "Machine Learning", "FastAPI"],
            "missing_skills": ["Streamlit", "Docker"]
        })
    
    return results

# --- Streamlit UI ---

st.set_page_config(
    page_title="AI Resume Matcher",
    page_icon="🤖",
    layout="wide"
)

# --- Header ---

st.title("🤖 AI-Powered Resume Matcher")

st.markdown("""
Welcome to the future of recruiting! This tool leverages AI to instantly match candidate resumes 
against a job description, helping you find the perfect fit in seconds.
""")

# --- Sidebar ---
with st.sidebar:
    st.header("📋 Instructions")
    st.info(
        """
        1.  Paste the job description in the text area.
        2.  Upload one or more resume files (PDF, DOCX).
        3.  Click the 'Match Resumes' button.
        4.  Review the ranked results and skill analysis.
        """
    )
    st.markdown("---")
    st.markdown("Made with ❤️ using [Streamlit](https://streamlit.io/)")


# --- Main Application ---
col1, col2 = st.columns(2)

with col1:
    st.header("📝 Job Description")
    job_description = st.text_area("Paste the full job description here.", height=300)

with col2:
    st.header("📄 Candidate Resumes")
    uploaded_resumes = st.file_uploader(
        "Upload resumes here.", 
        type=['pdf', 'docx'], 
        accept_multiple_files=True
    )

# --- Match Button ---
if st.button("✨ Match Resumes", type="primary", use_container_width=True):
    if not job_description:
        st.warning("Please paste a job description first.")
    elif not uploaded_resumes:
        st.warning("Please upload at least one resume.")
    else:
        with st.spinner("🧠 Analyzing and matching resumes..."):
            
            results = run_matching_pipeline(job_description, uploaded_resumes)
            
            # Sort results by score
            results.sort(key=lambda x: x['score'], reverse=True)

            st.success(f"Found {len(results)} matches! Here are the top candidates:")

            # --- Display Results ---
            for result in results:
                with st.expander(f"**{result['resume_filename']}** - Match Score: **{result['score']}%**"):
                    st.progress(result['score'])
                    
                    m_col, mm_col = st.columns(2)
                    
                    with m_col:
                        st.subheader("✅ Matching Skills")
                        st.multiselect(
                            "Matching Skills", 
                            options=result['matching_skills'], 
                            default=result['matching_skills'],
                            label_visibility="collapsed"
                        )

                    with mm_col:
                        st.subheader("❌ Missing Skills")
                        st.multiselect(
                            "Missing Skills",
                            options=result['missing_skills'],
                            default=result['missing_skills'],
                            label_visibility="collapsed"
                        )

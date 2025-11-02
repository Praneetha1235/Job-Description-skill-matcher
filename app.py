import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Job Description Skill Matcher", layout="wide")

st.title("🧠 Job Description Skill Matcher")
st.write("Analyze skill alignment between Job Description and Resume using AI (spaCy + GPT)")

# Input areas
jd = st.text_area("📋 Paste Job Description", height=200)
resume = st.text_area("👤 Paste Resume", height=200)

if st.button("Analyze Skills"):
    if jd.strip() and resume.strip():
        with st.spinner("Analyzing with AI... Please wait."):
            try:
                response = requests.post("http://127.0.0.1:5000/analyze",
                                         json={"job_description": jd, "resume_text": resume})
                if response.status_code == 200:
                    data = response.json()

                    st.subheader("✅ Matched Skills")
                    st.write(", ".join(data["matched"]) if data["matched"] else "No matched skills found.")

                    st.subheader("⚠️ Missing Skills")
                    st.write(", ".join(data["missing"]) if data["missing"] else "No missing skills.")

                    st.subheader("💡 AI Insights")
                    st.write(data["insights"])

                    # Optional visualization
                    match_count = len(data["matched"])
                    missing_count = len(data["missing"])
                    chart_data = pd.DataFrame({
                        "Category": ["Matched", "Missing"],
                        "Count": [match_count, missing_count]
                    })
                    st.bar_chart(chart_data.set_index("Category"))

                else:
                    st.error(f"Error: {response.status_code}")
            except Exception as e:
                st.error(f"Connection failed: {e}")
    else:
        st.warning("Please fill both text boxes before analyzing.")

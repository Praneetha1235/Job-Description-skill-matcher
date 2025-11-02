An AI-driven web application that analyzes job descriptions and resumes for semantic skill matching using Python, spaCy, Flask, and Streamlit. It extracts, compares, and ranks relevant skills to identify job–resume fit.

🚀Features:
Extracts skills using NLP (spaCy)
Calculates skill match percentage
Flask API backend + Streamlit dashboard
Visualizes matching and missing skills
Optional GPT-based semantic enhancement

⚙️ Setup & Run
# 1. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# 3. Run Flask backend
python api.py

# 4. Run Streamlit frontend (in new terminal)
streamlit run app.py

Output Example
Metric           Example
Match            Score	82%
Matched Skills	 Python, Flask, NLP
Missing Skills	 AWS, Docker

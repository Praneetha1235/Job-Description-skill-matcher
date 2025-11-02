from flask import Flask, request, jsonify
from flask_cors import CORS
from skills_extractor import compare_skills

app = Flask(__name__)
CORS(app)  # Allow Streamlit to access the API

@app.route('/analyze', methods=['POST'])
def analyze():
    """Endpoint for analyzing job description and resume"""
    data = request.get_json()
    jd_text = data.get("job_description", "")
    resume_text = data.get("resume_text", "")
    
    if not jd_text or not resume_text:
        return jsonify({"error": "Missing job description or resume text"}), 400

    result = compare_skills(jd_text, resume_text)
    return jsonify(result)

if __name__ == '__main__':
    print("🚀 Flask API running on http://127.0.0.1:5000/")
    app.run(debug=True)

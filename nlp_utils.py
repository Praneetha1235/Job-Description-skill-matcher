import spacy
import os
from openai import OpenAI

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("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))

def extract_skills(text):
    """Extracts potential skills using spaCy entities and nouns"""
    doc = nlp(text)
    skills = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "PRODUCT", "SKILL"]]
    tokens = [token.text for token in doc if token.pos_ == "NOUN"]
    return list(set(skills + tokens))

def compare_skills(jd_text, resume_text):
    """Compares JD and Resume to find matched and missing skills"""
    jd_skills = extract_skills(jd_text)
    resume_skills = extract_skills(resume_text)

    matched = [s for s in jd_skills if s.lower() in [r.lower() for r in resume_skills]]
    missing = [s for s in jd_skills if s.lower() not in [r.lower() for r in resume_skills]]

    # Generate insights from GPT
    prompt = f"Job skills: {jd_skills}\nResume skills: {resume_skills}\nProvide 2-3 sentences of insights about how well they align."
    gpt_response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    insights = gpt_response.output[0].content[0].text

    return {
        "jd_skills": jd_skills,
        "resume_skills": resume_skills,
        "matched": matched,
        "missing": missing,
        "insights": insights
    }

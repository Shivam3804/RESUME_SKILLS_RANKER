from flask import Flask, render_template, request
import fitz  # PyMuPDF
import os
from werkzeug.utils import secure_filename
from collections import Counter

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Make sure 'uploads/' exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Hardcoded skill list
target_skills = {
    "python", "c++", "mysql", "mongodb", "flask", "tensorflow",
    "keras", "pandas", "matplotlib", "powerbi", "scikit-learn",
    "git", "linux", "excel", "jupyter", "communication"
}

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.lower()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        resumes = request.files.getlist('resumes')
        job_desc = request.form.get('job_description', '').lower()

        if not resumes or not job_desc:
            return "Please upload resumes and paste job description."

        # Convert job description into skill words
        job_words = set(job_desc.split())

        results = []

        for resume in resumes:
            if resume and resume.filename.endswith('.pdf'):
                filename = secure_filename(resume.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                resume.save(filepath)

                resume_text = extract_text_from_pdf(filepath)
                resume_words = set(resume_text.split())

                # Skills matched with predefined list
                matched_skills = {skill for skill in target_skills if skill in resume_text}

                # Skills matched with job description
                job_skill_overlap = job_words & resume_words

                # Calculate scores
                skill_score = len(matched_skills)
                job_score = len(job_skill_overlap)

                total_score = skill_score + job_score  # Simple formula

                results.append({
                    'filename': filename,
                    'matched_skills': sorted(matched_skills),
                    'job_overlap': sorted(job_skill_overlap),
                    'skill_score': skill_score,
                    'job_score': job_score,
                    'total_score': total_score
                })

        # Sort by total score descending
        results.sort(key=lambda x: x['total_score'], reverse=True)

        return render_template('result.html',
                               results=results,
                               job_desc=job_desc)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
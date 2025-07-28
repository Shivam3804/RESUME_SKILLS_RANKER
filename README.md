# Resume Skill Extractor & Ranker

A simple Flask-based web app that allows HRs or hiring managers to upload multiple PDF resumes and paste a job description. The system extracts relevant skills from each resume, compares them with the job description, scores each resume based on relevance, and ranks them accordingly.

---

## Features

- Upload **multiple PDF resumes**
- Paste a job description for comparison
- Extracts and highlights **matching skills**
- Calculates a **relevance score** based on overlap
- Displays results in **ranked order**
- Clean, responsive Bootstrap UI

---

## Tech Stack

| Category            | Tools/Libraries Used                        |
|---------------------|---------------------------------------------|
| **Backend**         | Python, Flask, PyMuPDF (`fitz`)             |
| **Frontend**        | HTML, Bootstrap                             |
| **Skill Matching**  | Python sets & string matching logic         |
| **Deployment-Ready**| GitHub, Flask framework                     |

---

## Project Structure
resume-skill-matcher<br>
│<br>
├── app.py # Main Flask application<br>
├── uploads/ # Folder to store uploaded resumes<br>
├── templates/<br>
│ ├── index.html # Input form (upload + job desc)<br>
│ └── result.html # Ranked results display<br>
└── README.md <br>

## How to Run Locally

1. **Clone the repo:**

   ```bash
   git clone https://github.com/Shivam3804/RESUME_SKILLS_RANKER
   cd RESUME_SKILLS_RANKER
2. Install library
   ```bash
   pip install flask pymupdf
   
3. Run file
   ```bash
   python app.py
4. Run in browser
   http://127.0.0.1:5000/


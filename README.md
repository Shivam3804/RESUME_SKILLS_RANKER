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
resume-skill-matcher/
│
├── app.py # Main Flask application
├── uploads/ # Folder to store uploaded resumes
├── templates/
│ ├── index.html # Input form (upload + job desc)
│ └── result.html # Ranked results display
└── README.md 

## 🧪 How to Run Locally

1. **Clone the repo:**

   ```bash
   git clone https://github.com/Shivam3804/RESUME_SKILLS_RANKER
   cd RESUME_SKILLS_RANKER

   pip install flask pymupdf

   python app.py

   http://127.0.0.1:5000/


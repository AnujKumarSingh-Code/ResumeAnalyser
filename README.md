AI-Powered Resume Analyzer & Job Matcher

A Flask-based web application designed to help job seekers improve their resumes by analyzing resume content and matching it to relevant job descriptions using Natural Language Processing (NLP) and Machine Learning (ML).

🚀 Features

Resume Upload & Parsing: Upload resumes in PDF or DOCX formats.

Job Description Analysis: Input or paste any job description.

Resume-Job Matching Score: NLP-driven similarity scoring between resume and job descriptions.

Keyword Recommendations: Highlight critical skills and suggest missing keywords.

Interactive User Interface: Simple, intuitive, and responsive UI built with Bootstrap.

🛠 Technology Stack

Backend: Flask, Python

NLP & ML Libraries: spaCy, scikit-learn, nltk

File Processing: PyMuPDF, pdfplumber, python-docx

Frontend: HTML, CSS, Bootstrap

⚙️ Installation

Clone the Repository

git clone https://github.com/your-username/resume-job-matcher.git
cd resume-job-matcher

Set Up Virtual Environment

python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

Install Dependencies

pip install --upgrade pip
pip install -r requirements.txt
python -m spacy download en_core_web_md

🎯 Usage

Run the Flask Application

python app.py

Open your browser and visit:

http://localhost:5000

🖥️ Project Structure

resume-job-matcher/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── results.html
└── uploads/

🚧 Future Improvements

Integrate user authentication and dashboard.

Automate job postings scraping.

Real-time feedback using advanced NLP models like GPT.

Deployment optimizations with Docker and cloud services.




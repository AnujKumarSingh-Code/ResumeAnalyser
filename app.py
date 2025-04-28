import os
from flask import Flask, request, render_template, redirect, url_for
import fitz  # PyMuPDF
import pdfplumber
import docx
import spacy
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

nlp = spacy.load("en_core_web_md")

def extract_text(filepath):
    text = ""
    if filepath.endswith(".pdf"):
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
    elif filepath.endswith(".docx"):
        doc = docx.Document(filepath)
        text = "\n".join([para.text for para in doc.paragraphs])
    return text

def calculate_similarity(resume, job_description):
    documents = [resume, job_description]
    cv = CountVectorizer().fit_transform(documents)
    similarity = cosine_similarity(cv[0], cv[1])
    return round(similarity[0][0] * 100, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        resume_file = request.files['resume']
        job_desc = request.form['job_desc']

        if resume_file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
            resume_file.save(filepath)
            resume_text = extract_text(filepath)

            similarity_score = calculate_similarity(resume_text, job_desc)

            # Keywords extraction (basic)
            doc_resume = nlp(resume_text)
            doc_job = nlp(job_desc)

            resume_keywords = {chunk.text.lower() for chunk in doc_resume.noun_chunks}
            job_keywords = {chunk.text.lower() for chunk in doc_job.noun_chunks}
            missing_keywords = job_keywords - resume_keywords

            return render_template('results.html', score=similarity_score, missing_keywords=missing_keywords)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

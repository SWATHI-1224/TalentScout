📌 1. Project Overview

TalentScout is an AI-powered Hiring Assistant Chatbot designed to streamline the initial candidate screening process for a technology recruitment agency.

The chatbot:

Greets candidates professionally
Collects essential candidate information
Asks tech-stack–specific technical questions
Maintains conversation context
Handles unexpected inputs gracefully
Ends conversation professionally
The system uses a Large Language Model (LLM) to dynamically generate relevant technical questions based on the candidate’s declared tech stack.

This project demonstrates practical implementation of:
Prompt Engineering
Context-aware AI conversations
LLM integration
Secure handling of user input

instalation process

1️⃣ Activate Virtual Environment (Windows)
python -m venv venv
venv\Scripts\Activate

If error:

Set-ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\Activate
2️⃣ Install Required Libraries

Inside activated venv:

pip install streamlit python-dotenv google-generativeai pypdf openai
3️⃣ Run Streamlit App
streamlit run app.py

OR

.\venv\Scripts\python.exe -m streamlit run app.py
4️⃣ Libraries You Need
Purpose Library
UI streamlit
API Key Handling python-dotenv
LLM (Gemini) google-generativeai
LLM (OpenAI) openai

Resume PDF Reading pypdf
5️⃣ Add Resume PDF Upload (Short Code)
import streamlit as st
import pypdf

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
reader = pypdf.PdfReader(uploaded_file)
text = ""
for page in reader.pages:
text += page.extract_text()
st.session_state["resume_text"] = text
st.success("Resume uploaded successfully!")

6️⃣ Add to requirements.txt
streamlit
python-dotenv
google-generativeai
openai
pypdf

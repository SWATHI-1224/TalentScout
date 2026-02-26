import streamlit as st
import os
from pathlib import Path
from dotenv import load_dotenv

# 1. FIX: Absolute path to .env
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

from core.engine import TalentScoutEngine

st.set_page_config(page_title="TalentScout AI", layout="wide")

# 2. Get the key and verify it
api_key = os.getenv("GEMINI_API_KEY")

# 3. Initialize Engine ONLY IF we have a key
if "engine" not in st.session_state:
    if api_key:
        # Pass the key directly to the engine
        st.session_state.engine = TalentScoutEngine(api_key=api_key)
    else:
        st.error("❌ GEMINI_API_KEY not found! Please check your .env file.")
        st.stop()

# --- REST OF YOUR APP.PY CODE ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "stage" not in st.session_state:
    st.session_state.stage = "GREETING"
if "candidate_profile" not in st.session_state:
    st.session_state.candidate_profile = {
        "full_name": None, "email": None, "phone": None,
        "experience_years": None, "desired_position": None,
        "location": None, "tech_stack": None
    }

st.title("🤖 TalentScout Hiring Assistant")

with st.sidebar:
    st.header("📋 Candidate Profile")
    st.info(f"Stage: {st.session_state.stage}")
    st.json(st.session_state.candidate_profile)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Start by saying Hi"):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    response = st.session_state.engine.process_message(prompt, st.session_state)
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.rerun()
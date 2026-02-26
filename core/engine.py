import json
from core.s import SYSTEM_PERSONA, INFO_GATHERING_PROMPT, TECH_QUESTION_PROMPT
from services.llm_service import LLMService

class TalentScoutEngine:
    def __init__(self, api_key):
        # Receive the key from app.py
        self.llm = LLMService(api_key=api_key)

    def process_message(self, user_input: str, state):
        state.messages.append({"role": "user", "content": user_input})

        # Extraction logic
        extract_prompt = f"Extract Name and Tech Stack as JSON from: {user_input}. Return only JSON."
        raw_extra = self.llm.get_chat_response(extract_prompt, [])
        try:
            start = raw_extra.find('{')
            end = raw_extra.rfind('}') + 1
            data = json.loads(raw_extra[start:end])
            for key in ["full_name", "tech_stack"]:
                if data.get(key) and str(data[key]).lower() != "null":
                    state.candidate_profile[key] = data[key]
        except:
            pass

        # Stage logic
        if state.candidate_profile.get("tech_stack"):
            state.stage = "TECHNICAL_SCREEN"
            prompt = TECH_QUESTION_PROMPT.format(tech_stack=state.candidate_profile["tech_stack"])
        else:
            prompt = INFO_GATHERING_PROMPT.format(candidate_data=state.candidate_profile)

        response = self.llm.get_chat_response(SYSTEM_PERSONA + "\n" + prompt, state.messages)
        state.messages.append({"role": "assistant", "content": response})
        return response
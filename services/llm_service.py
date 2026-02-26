import requests
import json

class LLMService:
    def __init__(self, api_key):
        # 1. Clean the key received from the engine
        self.api_key = api_key.strip().replace('"', '').replace("'", "")
        self.model_id = "gemini-2.5-flash"
        self.url = f"https://generativelanguage.googleapis.com/v1/models/{self.model_id}:generateContent"

    def get_chat_response(self, system_prompt: str, history: list):
        try:
            formatted_contents = []
            for i, msg in enumerate(history):
                role = "user" if msg["role"] == "user" else "model"
                text = msg["content"]
                if i == 0:
                    text = f"INSTRUCTIONS: {system_prompt}\n\nUSER: {text}"
                formatted_contents.append({"role": role, "parts": [{"text": text}]})

            payload = {"contents": formatted_contents}
            
            # 2. Key is injected directly into the URL
            response = requests.post(
                f"{self.url}?key={self.api_key}",
                headers={'Content-Type': 'application/json'},
                data=json.dumps(payload),
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json()['candidates'][0]['content']['parts'][0]['text']
            else:
                error = response.json().get('error', {}).get('message', 'Unknown Error')
                return f"Gemini Error ({response.status_code}): {error}"
        except Exception as e:
            return f"System Error: {str(e)}"
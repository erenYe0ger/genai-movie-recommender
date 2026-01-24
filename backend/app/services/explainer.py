import requests
import os

HF_API_KEY = os.getenv("HF_API_KEY")

# Pick a lightweight instruct model
HF_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"


def generate_explanation(user_prompt: str, title: str, overview: str):
    if not HF_API_KEY:
        return "Explanation unavailable (no HF_API_KEY set)."

    prompt = f"""
User preference: {user_prompt}

Movie: {title}
Overview: {overview}

Explain in 2 short, simple sentences why this movie matches the user's taste.
"""

    api_url = f"https://api-inference.huggingface.co/models/{HF_MODEL}"

    headers = {"Authorization": f"Bearer {HF_API_KEY}"}

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 60,
            "temperature": 0.4,
        }
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload, timeout=20)
        result = response.json()

        # HF returns a list of dicts
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"].strip()

        return "Explanation unavailable."
    except Exception:
        return "Explanation unavailable."

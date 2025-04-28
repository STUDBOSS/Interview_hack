# responder/gpt_responder.py

import openai
from utils.config import client

# Set the API key
openai.api_key = client

def ask_gpt(prompt):
    """Send a prompt to GPT and return the response text."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or use "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You're a helpful assistant answering interview questions."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[ERROR] GPT request failed: {e}"

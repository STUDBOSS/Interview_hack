# Uses Gemini 2.0 Flash API for generating interview answers based on resume

import requests
import PyPDF2
import caption_reader

# Replace with your actual Gemini API key
GEMINI_API_KEY = ""
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

# Send prompt to Gemini API
def ask_gemini(prompt):
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(GEMINI_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        # Extract the actual response text
        reply = data["candidates"][0]["content"]["parts"][0]["text"]
        return reply

    except Exception as e:
        print(f"❌ Error communicating with Gemini: {e}")
        return None

# Read the resume from the provided file path (PDF only)
def read_resume(file_path):
    text = ""
    if file_path.lower().endswith(".pdf"):
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text()
    return text

# Callback function to process new captions
def process_caption(caption_text, resume_text):
    print(f"🗣️ Question: {caption_text}")
    prompt = (
        f"You are preparing interview answers based on the following resume:\n\n"
        f"{resume_text}\n\n"
        f"Now answer this interview question:\n{caption_text}"
    )
    response = ask_gemini(prompt)
    if response:
        print(f"\n🤖 Gemini's Answer: {response}\n")
    else:
        print("⚠️ No response from Gemini.")

# MAIN function
def main():
    resume_path = r"Your/resume/path"

    print("📚 Reading resume...")
    resume_text = read_resume(resume_path)
    if not resume_text:
        print("⚠️ Failed to read resume text.")
        return
    print("✅ Resume processed. Ready for interview questions!\n")

    # Start listening to Windows 11 Live Captions
    caption_reader.live_caption_listener(lambda caption: process_caption(caption, resume_text))

if __name__ == "__main__":
    main()

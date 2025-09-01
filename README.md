🎤 AI-Powered Interview Assistant

An AI-driven interview practice assistant that listens to spoken questions, understands the context of a candidate’s resume, and generates smart answers using ChatGPT or Google Gemini AI.

This project extracts text from a PDF resume, captures your voice input, and provides context-aware interview responses in real time.

🚀 Features

📄 Extracts resume text from PDF

🎤 Captures real-time voice questions

🤖 Generates AI-powered interview answers using ChatGPT or Gemini

🔁 Continuous question-answer loop

🧩 Resume-aware prompt engineering

📦 Installation

Clone this repo and install dependencies:

git clone https://github.com/yourusername/ai-interview-assistant.git
cd ai-interview-assistant
pip install -r requirements.txt

🔑 Get Free API Keys
1️⃣ For ChatGPT (via RapidAPI)

Go to RapidAPI

Create a free account

Search for OpenAI ChatGPT API

Subscribe to the free tier

Copy your X-RapidAPI-Key

2️⃣ For Gemini AI

Go to Google AI Studio

Sign in with your Google account

Create a New API Key under "Get API Key"

Copy your key (GEMINI_API_KEY)

⚡ Usage
▶️ Using Gemini (main.py)
export GEMINI_API_KEY=your_gemini_api_key_here
python main.py

▶️ Using ChatGPT via RapidAPI (main1.py)
export RAPIDAPI_KEY=your_rapidapi_key_here
python main1.py

📂 Project Structure
ai-interview-assistant/
│── main.py        # Gemini AI version
│── main1.py       # ChatGPT (RapidAPI) version
│── requirements.txt
│── README.md

🛠️ Tech Stack

Python

Google Gemini API

ChatGPT via RapidAPI

SpeechRecognition (voice capture)

PyPDF2 (resume parsing)

Requests (API calls)

✨ Future Improvements

Add GUI (Streamlit/Flask)

Support multiple resume formats (DOCX, TXT)

Enhance interview feedback scoring

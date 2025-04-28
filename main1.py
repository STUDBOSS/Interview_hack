import time
import requests
import PyPDF2
import docx
from caption_reader import live_caption_listener

# RapidAPI setup
RAPIDAPI_KEY = "2da17ffaa1mshc9f9e89ffaad466p1514d5jsn230922b2d57c"
RAPIDAPI_URL = "https://chatgpt-42.p.rapidapi.com/chat"

# Function to ask GPT for answers
def ask_gpt(prompt):
    url = RAPIDAPI_URL
    payload = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "model": "gpt-4o-mini"
    }
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get('result') or data
    except Exception as e:
        print(f"❌ Error communicating with GPT: {e}")
        return None

# Function to extract text from PDF using PyPDF2
def extract_resume_from_pdf(pdf_path):
    resume_text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            resume_text += page.extract_text()
    return resume_text

# Function to extract text from DOCX file
def extract_resume_from_docx(docx_path):
    doc = docx.Document(docx_path)
    resume_text = []
    for para in doc.paragraphs:
        resume_text.append(para.text)
    return "\n".join(resume_text)

def main():
    # Step 1: Extract resume text
    resume_path = r"C:\VS Code\Interview\interview-hack-gpt\Mohit-Paradkar-B.E.-ArtificialIntelligence&MachineLearning-2025-03-16-06-58-00-916258.pdf"
    file_type = resume_path.split('.')[-1].lower()

    if file_type == "pdf":
        resume = extract_resume_from_pdf(resume_path)
    elif file_type == "docx":
        resume = extract_resume_from_docx(resume_path)
    else:
        print("Unsupported file type. Please provide a PDF or DOCX file.")
        return

    print("\nResume successfully extracted!")
    print("\nYour resume:\n", resume)

    # Step 2: Define caption handler
    def handle_caption(caption_text):
        print(f"\n🗣️ Question Heard: {caption_text}")
        prompt = f"You are preparing interview answers based on the following resume: {resume}\n\nQuestion: {caption_text}"
        response = ask_gpt(prompt)
        if response:
            print(f"\n🤖 GPT Suggests: {response}")
        else:
            print("⚠️ No response received from GPT.")
        print("\nListening for next question...\n")

    # Step 3: Start live caption listener
    print("\nStarting live caption capture from Windows Live Caption...\n")
    live_caption_listener(handle_caption)

if __name__ == "__main__":
    main()

import pytesseract
from PIL import ImageGrab
import time
import requests
import PyPDF2
# import docx

# Tesseract installation path (update with your installation path)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

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

# Function to handle the caption and send it to GPT
def handle_caption(caption_text, resume):
    print(f"\n🗣️ Question Heard: {caption_text}")
    
    # Send the caption to GPT for processing with the resume
    prompt = f"You are preparing interview answers based on the following resume: {resume}\n\nQuestion: {caption_text}"
    response = ask_gpt(prompt)
    
    if response:
        print(f"\n🤖 GPT Suggests: {response}")
    else:
        print("⚠️ No response received from GPT.")
    print("\nListening for next question...\n")

# Function to capture and extract text using OCR
def capture_captions(region=None):
    screenshot = ImageGrab.grab(bbox=region)  # Capture a region of the screen
    text = pytesseract.image_to_string(screenshot)  # Extract text using OCR
    return text.strip()

# Function to extract text from PDF using PyPDF2
def extract_resume_from_pdf(pdf_path):
    resume_text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            resume_text += page.extract_text()
    return resume_text

# Function to extract text from DOCX file
def extract_resume_from_docx(docx_path):
    doc = docx.Document(docx_path)
    resume_text = []
    for para in doc.paragraphs:
        resume_text.append(para.text)
    return "\n".join(resume_text)

# Main function to start the process
def main():
    # Step 1: Ask the user for the resume file path and file type
    resume_path = r"C:\VS Code\Interview\interview-hack-gpt\Mohit-Paradkar-B.E.-ArtificialIntelligence&MachineLearning-2025-03-16-06-58-00-916258.pdf"
    file_type = resume_path.split('.')[-1].lower()

    # Extract resume text based on file type (PDF or DOCX)
    if file_type == "pdf":
        resume = extract_resume_from_pdf(resume_path)
    # elif file_type == "docx":
    #     resume = extract_resume_from_docx(resume_path)
    # else:
    #     print("Unsupported file type. Please provide a PDF or DOCX file.")
    #     return
    
    print("\nResume successfully extracted!")
    print("\nYour resume:\n", resume)  # You can display or store the resume if needed
    
    # Step 2: Define the region to capture the captions (update as needed)
    caption_region = (100, 1000, 1800, 1080)  # Example values, change according to your screen
    
    print("\nStarting caption capture...\n")
    
    # Step 3: Continuously capture captions and process them
    while True:
        caption = capture_captions(caption_region)
        
        if caption:
            print(f"\n🗣️ Caption Captured: {caption}")
            # Include the resume as context when asking GPT
            handle_caption(caption, resume)
        else:
            print("No captions detected. Waiting for the next frame...")
        
        time.sleep(1)  # Capture every 1 second (adjust as needed)

# Start the process
main()

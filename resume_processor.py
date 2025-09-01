# import pdfplumber
# import requests

# class ResumeAssistant:
#     def __init__(self, resume_path):
#         # Extract resume data once
#         self.resume_data = self.extract_resume_data(resume_path)
        
#         # Initialize conversation history with the resume as system prompt
#         self.conversation_history = [
#             {
#                 "role": "system",
#                 "content": f"You are an interview assistant helping the candidate answer interview questions. The candidate's resume is:\n\n{self.resume_data}\n\nAlways base your responses on this resume."
#             }
#         ]
        
#         # API details
#         self.url = "https://chatgpt-42.p.rapidapi.com/chat"
#         self.headers = {
#             "x-rapidapi-key": "your-rapidapi-key",
#             "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
#             "Content-Type": "application/json"
#         }

#     def extract_resume_data(self, resume_path):
#         """
#         Extract text from a resume PDF.
#         """
#         with pdfplumber.open(resume_path) as pdf:
#             text = ""
#             for page in pdf.pages:
#                 text += page.extract_text()
#         return text

#     def ask_question(self, question_text):
#         """
#         Add user's new question to conversation history and get GPT's response.
#         """
#         # Add the user's new question
#         self.conversation_history.append({
#             "role": "user",
#             "content": question_text
#         })
        
#         payload = {
#             "messages": self.conversation_history,
#             "model": "gpt-4o-mini"
#         }
        
#         response = requests.post(self.url, json=payload, headers=self.headers)
        
#         if response.status_code == 200:
#             response_json = response.json()
#             gpt_reply = response_json['choices'][0]['message']['content']
            
#             # Add assistant's reply to conversation history
#             self.conversation_history.append({
#                 "role": "assistant",
#                 "content": gpt_reply
#             })
            
#             return gpt_reply
#         else:
#             return f"Error: {response.status_code}"

# import requests
# from PyPDF2 import PdfReader


# RAPIDAPI_URL = "https://chatgpt-42.p.rapidapi.com/chat"

# class ResumeAssistant:
#     def __init__(self, resume_path):
#         self.resume_text = self._extract_resume(resume_path)

#     def _extract_resume(self, path):
#         try:
#             reader = PdfReader(path)
#             text = ""
#             for page in reader.pages:
#                 text += page.extract_text()
#             return text.strip()
#         except Exception as e:
#             print(f"⚠️ Failed to read resume: {e}")
#             return ""

#     def ask_question(self, question):
#         if not self.resume_text:
#             prompt = question
#         else:
#             prompt = f"""You are preparing interview answers based on the following resume:\n\n{self.resume_text}\n\nQuestion: {question}"""

#         payload = {
#             "messages": [
#                 {"role": "user", "content": prompt}
#             ],
#             "model": "gpt-4o-mini"
#         }
#         headers = {
#             "x-rapidapi-key": RAPIDAPI_KEY,
#             "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
#             "Content-Type": "application/json"
#         }

#         try:
#             response = requests.post(RAPIDAPI_URL, json=payload, headers=headers)
#             response.raise_for_status()
#             data = response.json()

#             return data.get('result') or data  # flexible based on API response
#         except Exception as e:
#             print(f"❌ Error communicating with GPT: {e}")
#             return None


import PyPDF2
import docx

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

# Example usage
resume_text = extract_text_from_pdf("Mohit-Paradkar-B.E.-ArtificialIntelligence&MachineLearning-2025-03-16-06-58-00-916258.pdf")
# or
# resume_text = extract_text_from_docx("resume.docx")

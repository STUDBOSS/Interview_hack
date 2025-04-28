import pytesseract
import pyautogui
import time


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def get_captions(region):
    screenshot = pyautogui.screenshot(region=region)  # region=(left, top, width, height)
    text = pytesseract.image_to_string(screenshot)
    return text.strip()

def live_caption_listener(callback, region=(100, 800, 1200, 200)):
    print("🧠 Listening to live captions...")
    while True:
        caption_text = get_captions(region)
        if caption_text:
            print(f"📝 Heard: {caption_text}")
            callback(caption_text)  # send text to GPT or your logic
        time.sleep(1)  # Adjust speed if needed

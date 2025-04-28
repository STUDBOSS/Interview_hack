import time
from pywinauto import Desktop

def get_live_caption_text():
    """
    Attempts to find the Windows 11 Live Caption window and extract its text content.
    Returns the caption text if found, else returns an empty string.
    """
    try:
        # The Live Caption window class name is "Windows.UI.Core.CoreWindow"
        # The window title usually contains "Live Caption"
        windows = Desktop(backend="uia").windows()
        for w in windows:
            if "Live Caption" in w.window_text():
                # Get the text element inside the Live Caption window
                texts = w.descendants(control_type="Text")
                caption_texts = [t.window_text() for t in texts if t.window_text().strip()]
                return " ".join(caption_texts).strip()
        return ""
    except Exception as e:
        print(f"Error accessing Live Caption window: {e}")
        return ""

def live_caption_listener(callback, poll_interval=1.0):
    print("🧠 Listening to Windows 11 Live Captions...")
    last_caption = ""
    while True:
        caption_text = get_live_caption_text()
        if caption_text and caption_text != last_caption:
            print(f"📝 New Caption: {caption_text}")
            callback(caption_text)
            last_caption = caption_text
        time.sleep(poll_interval)

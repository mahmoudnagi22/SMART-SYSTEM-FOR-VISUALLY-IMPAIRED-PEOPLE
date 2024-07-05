import cv2
import pytesseract
from gtts import gTTS
from playsound import playsound
import os
import time
import tempfile

# Connect pytesseract to Tesseract path
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Function to convert text to speech
def text_to_speech(text):
    if text.strip():  # Check if the text is not empty
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_audio_file:
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save(temp_audio_file.name)
            temp_audio_file_path = temp_audio_file.name
        
        playsound(temp_audio_file_path)
        os.remove(temp_audio_file_path)  # Remove the file after playing
    else:
        print("No text to convert to speech.")

# Function to start the video feed from the webcam
def start_video_feed():
    video = cv2.VideoCapture("http://172.20.10.5:8080/video")  # Adjust the IP to match your webcam
    video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Frame width
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Frame height

    if not video.isOpened():
        print("Failed to open video feed. Check the URL.")
        return

    print("Press 's' to scan for text and 'q' to quit.")
    
    while True:
        ret, frame = video.read()
        if not ret:
            print("Failed to read frame from webcam")
            break
        
        # Resize the frame to the desired size (640x480)
        resized_frame = cv2.resize(frame, (640, 480))
        
        # Display the current frame
        cv2.imshow('OCR', resized_frame)
        
        # Check for key press
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            print("Scanning for text...")
            # Extract text from the frame
            extracted_text = pytesseract.image_to_string(resized_frame)
            print("Extracted text:\n", extracted_text)
            
            # Convert the text to speech
            text_to_speech(extracted_text)
        elif key == ord('q'):
            print("Quitting...")
            break

    video.release()
    cv2.destroyAllWindows()

# Start the video feed
start_video_feed()
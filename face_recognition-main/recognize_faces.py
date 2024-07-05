from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2
from gtts import gTTS
import pygame
import os

# Initialize 'currentname' to trigger only when a new person is identified.
currentname = "unknown"
# Path to the encodings pickle file created by train_model.py
encodingsP = "E:\\SMART SYSTEM FOR VISUALLY IMPAIRED PEOPLE\\face_recognition-main\\encodings.pickle"

# Load the known faces and embeddings
print("[INFO] loading encodings + face detector...")
data = pickle.loads(open(encodingsP, "rb").read())

# Initialize pygame mixer
pygame.mixer.init()

# Function to play the text-to-speech audio
def play_audio(text):
    tts = gTTS(text=text, lang='en')
    tts.save('output.mp3')
    pygame.mixer.music.load('output.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.music.unload()  # Unload the current music
    time.sleep(0.1)  # Add a small delay to ensure the file is released
    os.remove('output.mp3')

# Convert the phrase "Face recognition is ready" to speech and play it
play_audio("Face recognition is ready")

# IP Webcam URL
url = "http://10.170.240.61:8080/video"

# Initialize the video stream from IP Webcam and allow the camera sensor to warm up
vs = cv2.VideoCapture(0)
time.sleep(2.0)

# Start the FPS counter
fps = FPS().start()

# Loop over frames from the video stream
while True:
    # Grab the frame from the video stream and resize it to 500px (to speed up processing)
    ret, frame = vs.read()
    if not ret:
        break
    frame = imutils.resize(frame, width=500)

    # Detect the face locations
    boxes = face_recognition.face_locations(frame)
    # Compute the facial embeddings for each face bounding box
    encodings = face_recognition.face_encodings(frame, boxes)
    names = []

    # Loop over the facial embeddings
    for encoding in encodings:
        # Attempt to match each face in the input image to our known encodings
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        name = "Unknown"  # If face is not recognized, then print Unknown

        # Check to see if we have found a match
        if True in matches:
            # Find the indexes of all matched faces then initialize a dictionary to count the total number of times each face was matched
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            # Loop over the matched indexes and maintain a count for each recognized face
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1

            # Determine the recognized face with the largest number of votes
            name = max(counts, key=counts.get)

            # If someone in your dataset is identified, print their name on the screen
            if currentname != name:
                currentname = name
                play_audio(currentname)
                print(currentname)

        # Update the list of names
        names.append(name)

    # Loop over the recognized faces
    for ((top, right, bottom, left), name) in zip(boxes, names):
        # Draw the predicted face name on the image - color is in BGR
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 225), 2)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    # Display the image to our screen
    cv2.imshow("Facial Recognition is Running", frame)
    key = cv2.waitKey(1) & 0xFF

    # Quit when 'q' key is pressed
    if key == ord('q'):
        break

    # Update the FPS counter
    fps.update()

# Stop the timer and display FPS information
fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# Do a bit of cleanup
cv2.destroyAllWindows()
vs.release()

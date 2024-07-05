import cv2
import numpy as np
import keyboard  # Library for detecting keyboard presses
import pyttsx3  # Library for text-to-speech

# Known width of the marker (in meters)
KNOWN_WIDTH = 0.3  # Example: 30 cm

# Focal length of the camera (in pixels)
# This can be found using a calibration process or using a known distance
KNOWN_DISTANCE = 2.0  # Example: 2 meters away from the camera
FOCAL_LENGTH = 800  # Example value, needs to be calibrated

def find_marker(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur to the image
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    # Use Canny edge detection
    edged = cv2.Canny(gray, 35, 125)
    # Find contours in the edged image
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # Assume the largest contour is the marker
    c = max(contours, key=cv2.contourArea)
    return cv2.minAreaRect(c)

def distance_to_camera(knownWidth, focalLength, perWidth):
    # Compute and return the distance from the marker to the camera
    return (knownWidth * focalLength) / perWidth

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the camera
ip_camera_url = "http://10.170.240.61:8080/video"  # IP camera address
cap = cv2.VideoCapture(ip_camera_url)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        break

    # Resize the frame to the desired size (e.g., 640x480)
    resized_frame = cv2.resize(frame, (640, 480))

    # Display the resulting frame
    cv2.imshow('frame', resized_frame)
    
    # Check if the "s" key is pressed
    if keyboard.is_pressed('s'):
        # Find the marker in the image
        try:
            marker = find_marker(resized_frame)
            # Calculate the distance
            distance = distance_to_camera(KNOWN_WIDTH, FOCAL_LENGTH, marker[1][0])
            
            # Draw the bounding box and display the distance
            box = cv2.boxPoints(marker)
            box = np.int0(box)
            cv2.drawContours(resized_frame, [box], -1, (0, 255, 0), 2)
            cv2.putText(resized_frame, f"{distance:.2f} meters", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
            
            # Display the resulting frame with distance
            cv2.imshow('frame', resized_frame)
            
            # Announce the distance
            engine.say(f"The distance is {distance:.2f} meters")
            engine.runAndWait()
            
            # Wait for a short period to avoid multiple captures
            cv2.waitKey(2000)
        except Exception as e:
            print(f"Error: {e}")
            continue
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()

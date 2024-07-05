
# Smart System for the Visually Impaired

## Project Overview

The **Smart System for the Visually Impaired** is an innovative solution designed to assist visually impaired individuals by providing functionalities such as object recognition, currency recognition, face recognition, and converting text from images to audible speech. This project aims to enhance the independence and quality of life for visually impaired people through the use of smart glasses and a wearable system.

### Team Members
- Mohamed Nasser Mohamed Khodary
- Mahmoud Mohamed Nagi
- Ziad Abdelmohsen Mohamed
- Yasser Ramdan

### Supervisors
- Dr. Nagwa 
- Dr. Esraa

## Introduction

In Egypt, there are at least 800,000 blind individuals and 3 million visually impaired people who require assistance in their daily lives. Our project aims to provide a safe, independent, and effective mobility solution for visually impaired persons, enabling continuous contact with their families.

## Project Components

The project is divided into two main parts: Smart Glasses and a Wearable Smart System.

### 1. Smart Glasses

**Features:**
- **Object Recognition:** Identifies objects in the surrounding environment.
- **Currency Recognition:** Recognizes different denominations of currency.
- **Face Recognition:** Identifies known faces to assist in social interactions.
- **Text to Speech (OCR):** Converts text in images to audible speech.

**Components:**
- Raspberry Pi 4 Model B
- Raspberry Pi Camera V2
- Headphones
- Buttons, Wires, SD Card, Glasses, Battery

### 2. Wearable Smart System

**Features:**
- **Obstacle Detection:** Alerts the user when an obstacle is detected.
- **Emergency Assistance:** Sends an SMS and makes a phone call with the user's current location in case of an emergency.
- **Navigation Assistance:** Uses GPS to help the user navigate.

**Components:**
- ATmega128 Kit
- Ultrasonic Sensor
- Accelerometer
- Buzzer, Vibration Motor, GSM & GPS modules

## How to Run the Project

To run the Smart System for the Visually Impaired, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/smart-system-for-visually-impaired.git
   cd smart-system-for-visually-impaired
   ```

2. **Install Required Libraries:**
   Ensure you have all the required libraries installed. You can install them using the following commands:
   ```bash
   pip install opencv-python
   pip install pytesseract
   pip install picamera
   pip install gtts
   pip install RPi.GPIO
   pip install face_recognition
   ```

3. **Change the File Paths:**
   Modify the paths in the code to point to the correct locations of your files. Open the code files and adjust the paths as necessary.

4. **Run the Code:**
   Execute the main program to start the system.
   ```bash
   python main.py
   ```

**Note:** Make sure your Raspberry Pi is properly set up with all the required hardware components connected.

## Future Plans

We have identified areas for future improvement, such as dealing with potholes and stairs. Proposed solutions include creating a glove with small distance sensors and incorporating a sensor in headgear for better orientation detection.
# SMART-SYSTEM-FOR-VISUALLY-IMPAIRED-PEOPLE

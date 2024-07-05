import geocoder
from geopy.geocoders import Nominatim
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox
import os

def get_location_by_gps():
    try:
        g = geocoder.ip('me')
        latlng = g.latlng

        if latlng:
            latitude, longitude = latlng
            print(f"Latitude: {latitude}, Longitude: {longitude}")

            geolocator = Nominatim(user_agent="geoapiExercises")
            try:
                location = geolocator.reverse((latitude, longitude), exactly_one=True)
                address = location.address if location else "Address not found"
            except Exception as e:
                print(f"Failed to get address. Error: {e}")
                address = "Address not found"
            
            return {
                "latitude": latitude,
                "longitude": longitude,
                "address": address
            }
        else:
            return {
                "error": "Could not determine location"
            }
    except Exception as e:
        return {
            "error": f"An error occurred: {e}"
        }

def send_email(receiver_email, subject, body):
    sender_email = os.getenv("mahmoudsvu1@gmail.com")
    sender_password = os.getenv("123456")

    if not sender_email or not sender_password:
        print("Email credentials are not set.")
        return

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            print("Connecting to server...")
            server.login(sender_email, sender_password)
            print("Login successful.")
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully.")
    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Error: {e}")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

def show_location_info():
    location_info = get_location_by_gps()
    print(location_info)

    if "error" in location_info:
        print(location_info["error"])
        messagebox.showerror("Error", location_info["error"])
        return

    # Print the location information in the terminal
    print(f"Latitude: {location_info['latitude']}")
    print(f"Longitude: {location_info['longitude']}")
    print(f"Address: {location_info['address']}")

    receiver_email = "email2002@gmail.com"
    subject = "Current Location Information"
    body = f"Latitude: {location_info['latitude']}\nLongitude: {location_info['longitude']}\nAddress: {location_info['address']}"

    send_email(receiver_email, subject, body)

    root = tk.Tk()
    root.title("Current Location Information")

    tk.Label(root, text="Current Location Information", font=("Arial", 14)).pack(pady=10)
    tk.Label(root, text=f"Latitude: {location_info['latitude']}", font=("Arial", 12)).pack(anchor="w", padx=20)
    tk.Label(root, text=f"Longitude: {location_info['longitude']}", font=("Arial", 12)).pack(anchor="w", padx=20)
    tk.Label(root, text=f"Address: {location_info['address']}", font=("Arial", 12)).pack(anchor="w", padx=20, pady=10)

    root.mainloop()

if __name__ == "__main__":
    show_location_info()

import tkinter as tk
from tkinter import font as tkfont
import subprocess  # لتشغيل ملفات خارجية

def run_function_1():
    subprocess.Popen(['python', 'E:\\SMART SYSTEM FOR VISUALLY IMPAIRED PEOPLE\\coine detection\\coine_detection.py'])  # تشغيل ملف final_project.py

def run_function_2():
    subprocess.Popen(['python', 'E:\\SMART SYSTEM FOR VISUALLY IMPAIRED PEOPLE\\object detection\\Real-time-Object-Detection-with-OpenCV-Using-YOLO-main\\Real-time Object Detection.py'])  # تشغيل ملف Real-time Object Detection.py

def run_function_3():
    subprocess.Popen(['python', 'E:\\SMART SYSTEM FOR VISUALLY IMPAIRED PEOPLE\\OCR\\ocr.py'])  # تشغيل ملف Real-time Object Detection.py

def run_function_4():
    subprocess.Popen(['python', 'E:\\SMART SYSTEM FOR VISUALLY IMPAIRED PEOPLE\\camera mat\\cam.py'])  # تشغيل ملف Real-time Object Detection.py

def run_function_5():
    subprocess.Popen(['python', 'E:\\SMART SYSTEM FOR VISUALLY IMPAIRED PEOPLE\\location\\location.py'])  # تشغيل ملف Real-time Object Detection.py

def run_function_6():
    subprocess.Popen(['python', 'E:\\SMART SYSTEM FOR VISUALLY IMPAIRED PEOPLE\\face_recognition-main\\recognize_faces.py'])  # تشغيل ملف Real-time Object Detection.py

def main():
    root = tk.Tk()
    root.title("SSVIP")
    root.geometry("600x800")  # تغيير حجم النافذة

    # تغيير شكل الخطوط
    default_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
    button_font = tkfont.Font(family="Helvetica", size=14, weight="bold")
    
    # إعداد العنوان
    title_label = tk.Label(root, text="SSVIP ", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=20)

    # إطار للأزرار
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)


        # Object detection
    function2_button = tk.Button(button_frame, text="Object Detection", command=run_function_2, font=button_font, bg="green", fg="white", width=20, height=2)
    function2_button.pack(pady=10)

        #OCR
    function6_button = tk.Button(button_frame, text="face  recognition", command=run_function_6, font=button_font, bg="orange", fg="white", width=20, height=2)
    function6_button.pack(pady=10)
    
        #OCR
    function3_button = tk.Button(button_frame, text="OCR", command=run_function_3, font=button_font, bg="grey", fg="white", width=20, height=2)
    function3_button.pack(pady=10)
    
    # Coin Detection
    function1_button = tk.Button(button_frame, text="Coin Detection", command=run_function_1, font=button_font, bg="blue", fg="white", width=20, height=2)
    function1_button.pack(pady=10)




    # زر الكشف عن العملات
    function4_button = tk.Button(button_frame, text="Measuring distances", command=run_function_4, font=button_font, bg="brown", fg="white", width=20, height=2)
    function4_button.pack(pady=10)




    function5_button = tk.Button(button_frame, text="Location", command=run_function_5, font=button_font, bg="black", fg="white", width=20, height=2)
    function5_button.pack(pady=10)
    

    # زر الخروج
    exit_button = tk.Button(root, text="Exit", command=root.quit, font=button_font, bg="red", fg="white", width=20, height=2)
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

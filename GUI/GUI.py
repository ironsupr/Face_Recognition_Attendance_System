import threading
import cv2
from PIL import Image, ImageTk
import face_recognition
from face_module import train_face_recognition, recognize_faces
from customtkinter import *
from datetime import datetime
import os
from save_image import capture_and_save_images

# Initialize GUI
root = CTk()
set_default_color_theme("dark-blue")
set_appearance_mode("dark")
root.geometry("1000x900")
root.iconbitmap("icons.ico")

# bg = CTkImage("bg.jpg")

# Left panel
frame = CTkFrame(root, width=200)
frame.pack(fill="y", side="left")

label = CTkLabel(frame, text="Face Recognition", font=("Arial", 20))
label.pack(padx=20, pady=50, fill="x")

# Video Label (empty initially)
video_label = CTkLabel(root, text="")
video_label.pack(pady=20)

# Global variables
video_capture = None  # Webcam stream
is_running = False  # To track camera state

def remove_widgets():
    """Removes all widgets from the root window except for frame1."""
    for widget in root.winfo_children():
        if widget not in [frame]:
            widget.destroy()

def start_recognition_thread():
    """Starts the face recognition process only when button is clicked."""
    global video_capture, is_running

    if is_running:
        return  # If already running, do nothing

    is_running = True
    video_label.configure(text="")

    # Load model once (Lazy initialization)
    dataset_path = "images"
    known_faces, known_names, known_ids = train_face_recognition(dataset_path)

    # Open camera
    video_capture = cv2.VideoCapture(0)
    attendance_file = f"attendance_{datetime.now().strftime('%Y-%m-%d')}.csv"
    marked_attendance = set()

    def update_camera():
        """Continuously capture frames and update the GUI label."""
        if not is_running:
            return  # Stop updating if recognition is turned off

        ret, frame = video_capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = recognize_faces(known_faces, known_names, known_ids, frame, marked_attendance, attendance_file)

            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            video_label.imgtk = imgtk
            video_label.configure(image=imgtk)

        root.after(10, update_camera)

    threading.Thread(target=update_camera, daemon=True).start()

button_face = CTkButton(frame, text="Face Attendance", command=start_recognition_thread)
button_face.pack(padx=20, pady=20, fill="x")

def save_img():
    remove_widgets()

    label_name = CTkLabel(root, text="Enter Name:", font=("Arial", 20))
    label_name.place(relx=0.4, rely=0.3, anchor="center")

    entry_name = CTkEntry(root, font=("Arial", 20))
    entry_name.place(relx=0.6, rely=0.3, anchor="center")

    label_roll_no = CTkLabel(root, text="Enter Roll No.:", font=("Arial", 20))
    label_roll_no.place(relx=0.4, rely=0.4, anchor="center")

    entry_roll_no = CTkEntry(root, font=("Arial", 20))
    entry_roll_no.place(relx=0.6, rely=0.4, anchor="center")

    def save_images():
        name = entry_name.get()
        roll_no = entry_roll_no.get()
        num_images_to_capture = 10
        capture_and_save_images(name, roll_no, num_images_to_capture)
    
    button_save = CTkButton(root, text="Save Images", command=save_images)
    button_save.place(relx=0.5, rely=0.55, anchor="center")

    confirm_label = CTkLabel(root, text="Images will be saved in the 'images' folder.", font=("Arial", 20))
    confirm_label.place(relx=0.5, rely=0.8, anchor="center")

button_save_image = CTkButton(frame, text="Save Image to Dataset", command=save_img)
button_save_image.pack(padx=20, pady=20, fill="x")

def enter_data_student():
    remove_widgets()
    def save_data():
        name = entry_name.get()
        roll_no = entry_roll_no.get()
        with open("student_data.csv", "a") as file:
            file.write(f"{name},{roll_no}\n")
        label_saved = CTkLabel(root, text="Data saved successfully.", font=("Arial", 20))
        label_saved.place(relx=0.5, rely=0.7, anchor="center")
    entry_name = CTkEntry(root, font=("Arial", 20))
    entry_name.place(relx=0.5, rely=0.3, anchor="center")

    entry_roll_no = CTkEntry(root, font=("Arial", 20))
    entry_roll_no.place(relx=0.5, rely=0.4, anchor="center")

    label_name = CTkLabel(root, text="Enter Name:", font=("Arial", 20))
    label_name.place(relx=0.3, rely=0.3, anchor="center")

    label_roll_no = CTkLabel(root, text="Enter Roll No.:", font=("Arial", 20))
    label_roll_no.place(relx=0.3, rely=0.4, anchor="center")

    button_save_data = CTkButton(root, text="Save Data", command=save_data)

button_save_std_data = CTkButton(frame, text="Save Student Data", command=enter_data_student)
button_save_std_data.pack(padx=20, pady=20, fill="x")

# Make Improvements here
def show_student_data():
    remove_widgets()
    with open("student_data.csv", "r") as file:
        data = file.read()
    label_data = CTkLabel(root, text=data, font=("Arial", 20))
    label_data.place(relx=0.5, rely=0.5, anchor="center")

button_show_student_data = CTkButton(frame, text="Show Student Data")
button_show_student_data.pack(padx=20, pady=20, fill="x")

def open_csv():
    remove_widgets()
    """Opens today's attendance CSV file."""
    filename = f"attendance_{datetime.now().strftime('%Y-%m-%d')}.csv"
    if os.path.exists(filename):
        os.system(f"start {filename}")  # Open file
        label_csv = CTkLabel(root, text="TODAY'S ATTENDANCE OPENED", font=("Arial", 20))
        label_csv.place(relx=0.55, rely=0.5, anchor="center")
    else:
        label_csv = CTkLabel(root, text="TODAY'S ATTENDANCE NOT FOUND", font=("Arial", 20))
        label_csv.place(relx=0.55, rely=0.5, anchor="center")

button_csv = CTkButton(frame, text="Open CSV", command=open_csv)
button_csv.pack(padx=20, pady=20, fill="x")

def open_test_data():
    remove_widgets()
    """Opens the test_data.csv file."""
    # os.startfile(r"images")
    filename = r"images"
    if os.path.exists(filename):
        os.system(f"start {filename}")  # Open file
        label_csv = CTkLabel(root, text="TEST DATA OPENED", font=("Arial", 20))
        label_csv.place(relx=0.55, rely=0.5, anchor="center")
    else:
        label_csv = CTkLabel(root, text="TEST DATA NOT CREATED", font=("Arial", 20))
        label_csv.place(relx=0.55, rely=0.5, anchor="center")

button_test_data = CTkButton(frame, text="Test Data", command=open_test_data)
button_test_data.pack(padx=20, pady=20, fill="x")

def help_command():
    """Displays help information."""
    remove_widgets()
    help_text = """
    Face Recognition Attendance System

    1. Click 'Face Attendance' to start recognizing faces.
    2. Click 'Open CSV' to view today's attendance.
    3. Click 'Test Data' to view the test data folder.
    """
    label_help = CTkLabel(root, text=help_text, font=("Arial", 26), justify="left")
    label_help.place(relx=0.55, rely=0.3, anchor="center")

button_help = CTkButton(frame, text="Help", command=help_command)   
button_help.pack(padx=20, pady=20, fill="x")

def contact_us():
    """Displays contact information."""
    remove_widgets()
    contact_text = """
    Contact Us

    Email: yourgmail@gmail.com
    Numer: +1234567890"""
    label_contact = CTkLabel(root, text=contact_text, font=("Arial", 26), justify="left")
    label_contact.place(relx=0.55, rely=0.5, anchor="center")

button_contact = CTkButton(frame, text="Contact", command=contact_us)
button_contact.pack(padx=20, pady=20, fill="x")

root.mainloop()

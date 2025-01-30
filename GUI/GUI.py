from face_module import start_recognition
from customtkinter import *

root = CTk()
set_default_color_theme("green")
set_appearance_mode("dark")

frame = CTkFrame(root, width=200)
frame.pack()

button = CTkButton(frame, text = "Face Attendance", command=start_recognition)
button.place(relx = 0.1, rely = 0.3)

root.mainloop()
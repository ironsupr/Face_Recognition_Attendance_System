from pymongo import MongoClient
from customtkinter import *
try:
    # MONGO_URI = ""# Your MongoDB URI
    
    client = MongoClient(MONGO_URI)

    client.admin.command("ping")
    print("Connected successfully")

    db = client["student_data"]
    collection = db["students"]

    root = CTk()
    root.title("Student Data")
    root.geometry("1200x800")

    label_title = CTkLabel(root, text="Student Data", font=("Arial", 30))
    label_title.place(x=10, y = 1)

    label_name = CTkLabel(root, text = "Enter Name", font=("Arial", 20))
    label_name.place(x=400, y=200)

    root.mainloop()

    client.close()
except Exception as e:
    raise Exception(
        "The following error occurred: ", e)

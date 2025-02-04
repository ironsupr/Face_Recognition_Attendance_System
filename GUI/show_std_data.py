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
    root.geometry("1000x1200")

    label_title = CTkLabel(root, text="Student Data", font=("Arial", 30))
    label_title.place(x=10, y = 1)

    root.mainloop()

    client.close()
except Exception as e:
    raise Exception(
        "The following error occurred: ", e)

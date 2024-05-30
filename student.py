from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
# from Project import FaceRecognitionSystem
import pymysql
import os
import cv2
import subprocess
class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x790+0+0")
        self.root.title("Face Identification System")

        bg_img = Image.open("images/background.jpg")
        bg_img = bg_img.resize((1530, 790), Image.BILINEAR)
        self.bg_photoimg = ImageTk.PhotoImage(bg_img)

        background_label = Label(self.root, image=self.bg_photoimg)
        background_label.place(x=0, y=0, width=1530, height=790)

        # ************************************variables********************************************************
        self.var_Department = StringVar()
        self.var_Qualification = StringVar()
        self.var_Year = StringVar()
        self.var_Expereince = StringVar()
        self.var_Employee_id = StringVar()
        self.var_Name = StringVar()
        self.var_div = StringVar()
        self.var_Blood = StringVar()
        self.var_Gender = StringVar()
        self.var_Date_of_Birth = StringVar()
        self.var_E_mail = StringVar()
        self.var_Phone = StringVar()
        self.var_address = StringVar()
        self.var_Salary = StringVar()
        self.var_photo=StringVar()
        

        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=10, y=50, width=1500, height=700)

        title_lbl = Label(self.root, text="Employee Details", font=("times new roman", 35, "bold"),
                          bg="black", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=55)

        L_frame = LabelFrame(main_frame, bd=3,text="Employee Details",
                             font=("times new roman", 12, "bold"))
        L_frame.place(x=10, y=10, width=730, height=650)

        # course frame
        course_frame = LabelFrame(L_frame, bd=3, relief=RIDGE, text="General Information",
                                  font=("times new roman", 12, "bold"))
        course_frame.place(x=5, y=20, width=700, height=150)

        branch_label = Label(course_frame, bd=3, relief=RIDGE, text="Department",font=("times new roman", 12, "bold"))
        branch_label.grid(row=0, column=0, padx=(10, 5), pady=5, sticky="e")

        branch_box = ttk.Combobox(course_frame,font=("times new roman", 12, "bold"),textvariable=self.var_Department,state="readonly")
        branch_box["values"] = ("Select Department", "Management", "Human Resources", "Finance", "Controlling", "Marketing", "Research & Development",
                                "Security", "General Staff")
        branch_box.current(0)
        branch_box.grid(row=0, column=1, padx=5, pady=5)

        course1_label = Label(course_frame, bd=3, relief=RIDGE, text="Qualification Details",
                              font=("times new roman", 12, "bold"))
        course1_label.grid(row=0, column=2, padx=(10, 5), pady=5, sticky="e")
        
        branch1_box = ttk.Combobox(course_frame, textvariable=self.var_Qualification, font=("times new roman", 12, "bold"),
                                   state="readonly")
        branch1_box["values"] = ("Select", "10th & 12th","B-TECH", "BE", "Integrated M-TECH", "MBA", "BCA", "B.COM","MS & OTHER")
        branch1_box.current(0)
        branch1_box.grid(row=0, column=3, padx=5, pady=5)

        year_label = Label(course_frame, bd=3, relief=RIDGE, text="Year of Join",
                           font=("times new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="e")

        year_box = ttk.Combobox(course_frame, textvariable=self.var_Year, font=("times new roman", 12, "bold"),
                                state="readonly")
        year_box["values"] = ("Select Year","2020","2021", "2022" , "2023","2024")
        year_box.current(0)
        year_box.grid(row=1, column=1, padx=5, pady=5)

        semester_label = Label(course_frame, bd=3, relief=RIDGE,text="Experience",
                               font=("times new roman", 12, "bold"))
        semester_label.grid(row=1, column=2, padx=(10, 5), pady=5, sticky="e")

        semester_box = ttk.Combobox(course_frame, textvariable=self.var_Expereince, font=("times new roman", 12, "bold"),
                                    state="readonly")
        semester_box["values"] = ("Select Experience", "Fresh Candidate" , "2 or 3 years Experience", " 5 or above ")
        semester_box.current(0)
        semester_box.grid(row=1, column=3, padx=5, pady=5)

        student_frame = LabelFrame(L_frame, bd=3, relief=SUNKEN, text="Employee Information",
                                   font=("times new roman", 12, "bold"))
        student_frame.place(x=5, y=205, width=700, height=400)

        studentinf_label = Label(student_frame, bd=5, text="Employee ID :",
                                 font=("times new roman", 12, "bold"))
        studentinf_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        studentid_entry = ttk.Entry(student_frame, textvariable=self.var_Employee_id, width=20, font=("times new roman", 12, "bold"))
        studentid_entry.grid(row=0, column=1, padx=10)

        name_label = Label(student_frame, bd=5,  text="Name :-",
                           font=("times new roman", 12, "bold"))
        name_label.grid(row=0, column=2, padx=5, pady=5, sticky="e")

        nameid_entry = ttk.Entry(student_frame, textvariable=self.var_Name, width=20, font=("times new roman", 12, "bold"))
        nameid_entry.grid(row=0, column=3, padx=10)

        slot_label = Label(student_frame, bd=5,  text="Working Hours :-",
                                 font=("times new roman", 12, "bold"))
        slot_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        slot_entry = ttk.Entry(student_frame, textvariable=self.var_div, width=20, font=("times new roman", 12, "bold"))
        slot_entry.grid(row=1, column=1, padx=10)

        Registration_label = Label(student_frame, bd=5,  text="Blood Group :-",
                                 font=("times new roman", 12, "bold"))
        Registration_label.grid(row=1, column=2, padx=5, pady=5, sticky="e")

        Registration_entry = ttk.Entry(student_frame, textvariable=self.var_Blood, width=20, font=("times new roman", 12, "bold"))
        Registration_entry.grid(row=1, column=3, padx=10)

        gender_label = Label(student_frame, bd=5,  text="Gender:-",
                             font=("times new roman", 12, "bold"))
        gender_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        gender_box = ttk.Combobox(student_frame, textvariable=self.var_Gender,font=("times new roman", 12, "bold"), state="readonly",width=18)
        gender_box["values"] = ("Select gender", "Male", "Female", "Other")
        gender_box.current(0)
        gender_box.grid(row=2, column=1, padx=5, pady=5)

        DOB_label = Label(student_frame, bd=5,  text="DOB :- ",
                          font=("times new roman", 12, "bold"))
        DOB_label.grid(row=2, column=2, padx=5, pady=5, sticky="e")

        DOB_entry = ttk.Entry(student_frame, textvariable=self.var_Date_of_Birth, width=20, font=("times new roman", 12, "bold"))
        DOB_entry.grid(row=2, column=3, padx=10)

        email_label = Label(student_frame, bd=5, text="E-mail:-",
                            font=("times new roman", 12, "bold"))
        email_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")

        email_entry = ttk.Entry(student_frame, textvariable=self.var_E_mail, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10)

        phone_label = Label(student_frame, bd=5, text="PHONE NO:-",
                            font=("times new roman", 12, "bold"))
        phone_label.grid(row=3, column=2, padx=5, pady=5, sticky="e")

        phone_entry = ttk.Entry(student_frame, textvariable=self.var_Phone, width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10)

        address_label = Label(student_frame, bd=5, text="Address:-",
                              font=("times new roman", 12, "bold"))
        address_label.grid(row=4, column=0, padx= 5, pady=5, sticky="e")
        address_entry = ttk.Entry(student_frame, textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10)

        Salary_label = Label(student_frame, bd=5, text="Salary :-",
                              font=("times new roman", 12, "bold"))
        Salary_label.grid(row=4, column=2, padx= 5, pady=5, sticky="e")
        Salary_entry = ttk.Entry(student_frame, textvariable=self.var_Salary, width=20, font=("times new roman", 12, "bold"))
        Salary_entry.grid(row=4, column=3, padx=10)

        # self.var_radiobtn1 = StringVar()
        # radiobtn1 = ttk.Radiobutton(student_frame, text="Take photo sample", variable=self.var_radiobtn1, value="Yes")
        # radiobtn1.grid(row=5, column=0)
        # radiobtn2 = ttk.Radiobutton(student_frame, text="No photo sample", variable=self.var_radiobtn1, value="No")
        # radiobtn2.grid(row=5, column=1)

        btn_frame = LabelFrame(L_frame, bd=3, relief=SUNKEN )
        btn_frame.place(x=5, y=500, width=700, height=35)

        save_btn = Button(btn_frame, command=self.add_data, text="Save", width=17, font=("times new roman ", 13, "bold"), bg="blue", activebackground="orange", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame,command=self.update_function, text="Update", width=17, font=("times new roman ", 13, "bold"), bg="blue", activebackground="orange", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame,command=self.delete_data,text="Delete", width=15, font=("times new roman ", 13, "bold"), bg="blue", activebackground="orange", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame,command=self.reset, text="Reset", width=17, font=("times new roman ", 13, "bold"), bg="blue", activebackground="orange", fg="white")
        reset_btn.grid(row=0, column=3)

        btn1_frame = LabelFrame(L_frame, bd=3, relief=SUNKEN )
        btn1_frame.place(x=5, y=535, width=700, height=35)

        save_btn = Button(btn1_frame, text="Take Photo Sample",width=34, font=("times new roman ", 13, "bold"), bg="blue", activebackground="orange",command=self.open_photo_capture, fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn1_frame, text="Update Photo", width=34, font=("times new roman ", 13, "bold"), bg="blue", activebackground="orange", fg="white")
        update_btn.grid(row=0, column=1)

        R_frame = LabelFrame(main_frame, bd=3, text="Employee Details",
                             font=("times new roman", 12, "bold"))
        R_frame.place(x=750, y=10, width=730, height=650)

        Search_frame = LabelFrame(R_frame, bd=3, relief=SUNKEN, text="Search System",
                                  font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=20, width=720, height=70)

        Search_label = Label(Search_frame, text="Search By : ", font=("times new roman", 15, "bold"), bg="red", fg="white")
        Search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

       
        self.Search_box = ttk.Combobox(Search_frame, font=("times new roman", 12, "bold"), state="readonly", width=15)
        self.Search_box["values"] = ("Select ", "Roll_No", "Phone_No")
        self.Search_box.current(0)
        self.Search_box.grid(row=0, column=1, padx=5, pady=5)

        self.Search_entry = ttk.Entry(Search_frame, width=15, font=("times new roman", 12, "bold"))
        self.Search_entry.grid(row=0, column=2, padx=10)
        Search_btn = Button(Search_frame, text="Search", width=12,command=self.search_data, font=("times new roman ", 13, "bold"), bg="blue", activebackground="orange", fg="white")
        Search_btn.grid(row=0, column=3, padx=5, pady=5)

        ShowAll_btn = Button(Search_frame, text="Show All", width=12, command=self.fetch_data,font=("times new roman ", 13, "bold"), bg="blue", activebackground="orange", fg="white")
        ShowAll_btn.grid(row=0, column=4, padx=5, pady=5)

        # **********************************************Scrooling frame******************************************************************************

        Table_frame = Frame(R_frame, bd=3, relief=SUNKEN)
        Table_frame.place(x=5, y=100, width=720, height=400)

        Scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.student_Table = ttk.Treeview(Table_frame, column=("Department", "Qualification", "Year",
                                                               "Expereince", "Employee_id", 
                                                               "Name", "Timing", "Blood_grp",
                                                               "Gender", "Date_of_Birth", "E-mail", "Phone no", "Address", "Salary", "photo"), xscrollcommand=Scroll_x, yscrollcommand=Scroll_y)

        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)
        Scroll_x.config(command=self.student_Table.xview)
        Scroll_y.config(command=self.student_Table.yview)

        self.student_Table.heading("Department", text="Department")
        self.student_Table.heading("Qualification", text="Qualification")
        self.student_Table.heading("Year", text="Year")
        self.student_Table.heading("Expereince", text="Expereince")
        self.student_Table.heading("Employee_id", text="Employee_ID")
        self.student_Table.heading("Name", text="Name")
        self.student_Table.heading("Timing", text="Timing")
        self.student_Table.heading("Blood_grp", text="Blood_grp")
        self.student_Table.heading("Gender", text="Gender")
        self.student_Table.heading("Date_of_Birth", text="Date_of_Birth")
        self.student_Table.heading("E-mail", text="E-mail")
        self.student_Table.heading("Phone no", text="Phone no")
        self.student_Table.heading("Address", text="Address")
        self.student_Table.heading("Salary", text="Salary")
        self.student_Table.heading("photo", text="Photo Sample Status")
        self.student_Table["show"] = "headings"

        self.student_Table.column("Department", width=100)
        self.student_Table.column("Qualification", width=100)
        self.student_Table.column("Year", width=100)
        self.student_Table.column("Expereince", width=100)
        self.student_Table.column("Employee_id", width=100)
        self.student_Table.column("Name", width=100)
        self.student_Table.column("Timing", width=100)
        self.student_Table.column("Blood_grp", width=100)
        self.student_Table.column("Gender", width=100)
        self.student_Table.column("Date_of_Birth", width=100)
        self.student_Table.column("E-mail", width=100)
        self.student_Table.column("Phone no", width=100)
        self.student_Table.column("Address", width=100)
        self.student_Table.column("Salary", width=100)
        self.student_Table.column("photo", width=150)
        self.student_Table.pack(fill=BOTH, expand=1)
        self.student_Table.bind("<ButtonRelease>",self.get_cursor)
        # self.fetch_data()

        # ******************************************************function declaration****************************************

    def add_data(self):
        if (self.var_Department.get() == "Select Department" or self.var_Name.get() == "" or self.var_Employee_id.get() == ""):
            messagebox.showerror("Error", "All fields are Required", parent=self.root)
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="Abhiash#1234")
                cursor = conn.cursor()

                # Create the database if it doesn't exist
                create_database_query = 'CREATE DATABASE IF NOT EXISTS studentinfo'
                cursor.execute(create_database_query)

                # Use the studentinfo database
                cursor.execute('USE studentinfo')

                # Create the studentdetails table if it doesn't exist
                create_table_query = '''
                    CREATE TABLE IF NOT EXISTS studentdetails (
                    Department VARCHAR(50),
                    Qualification VARCHAR(50),
                    Year INT,
                    Expereince VARCHAR(50),
                    Employee_Id VARCHAR(45) PRIMARY KEY,
                    Name CHAR(100),
                    Timing CHAR(50),
                    Blood_grp varchar(3),
                    Gender varchar(255),
                    Date_of_birth DATE,
                    E_mail VARCHAR(100),
                    Phone_no INT,
                    Address VARCHAR(100),
                    Salary int(10),
                    Photo BIT
                    )
                '''
                cursor.execute(create_table_query)

                insert_query = '''
                INSERT INTO studentdetails (Department,Qualification,Year,Expereince,Employee_Id,Name,Timing,Blood_grp,Gender,Date_of_birth,E_mail,Phone_no,Address,Salary,Photo)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                '''
                values = (
                    self.var_Department.get(), self.var_Qualification.get(), self.var_Year.get(),
                    self.var_Expereince.get(), self.var_Employee_id.get(), self.var_Name.get(),
                    self.var_div.get(), self.var_Blood.get(), self.var_Gender.get(), self.var_Date_of_Birth.get(),
                    self.var_E_mail.get(), self.var_Phone.get(), self.var_address.get(),
                    self.var_Salary.get(), self.var_photo.get()
                )
                cursor.execute(insert_query, values)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Employee details have been added successfully", parent=self.root)
                self.fetch_data()
            except pymysql.Error as e:
                messagebox.showerror("Error", "Connection not established properly: " + str(e), parent=self.root)


#-----------------------fetch data------------
    def fetch_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="Abhiash#1234", database="studentinfo")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from studentdetails")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_Table.delete(*self.student_Table.get_children())
            for row in data:
                self.student_Table.insert("", END, values=row)
            conn.commit()
        conn.close()
    #------------update---------
    def search_data(self):
        selected_value = self.Search_box.get()
        search_value = self.Search_entry.get()

        if selected_value == "Select ":
            messagebox.showerror("Error", "Please select a search criteria", parent=self.root)
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="Abhiash#1234", database="studentinfo")
                my_cursor = conn.cursor()

                if selected_value == "Roll_No":
                    my_cursor.execute(f"SELECT * FROM studentdetails WHERE Employee_Id = '{search_value}'")
                elif selected_value == "Phone_No":
                    my_cursor.execute(f"SELECT * FROM studentdetails WHERE Phone_no = '{search_value}'")

                data = my_cursor.fetchall()

                if len(data) != 0:
                    self.student_Table.delete(*self.student_Table.get_children())
                    for row in data:
                        self.student_Table.insert("", END, values=row)
                else:
                    messagebox.showinfo("No Data", "No matching records found", parent=self.root)

                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error during search: {str(es)}", parent=self.root)

    def get_cursor(self,event=""):
        cursorf=self.student_Table.focus()
        content=self.student_Table.item(cursorf)
        data=content["values"]
        self.var_Department.set(data[0]),
        self.var_Qualification.set(data[1]),
        self.var_Year.set(data[3]), 
        self.var_Expereince.set(data[2]),
        self.var_Employee_id.set(data[4]), 
        self.var_Name.set(data[5]), 
        self.var_div.set(data[6]), 
        self.var_Blood.set(data[7]), 
        self.var_Gender.set(data[8]), 
        self.var_Date_of_Birth.set(data[9]), 
        self.var_E_mail.set(data[10]),
        self.var_Phone.set(data[11]), 
        self.var_address.set(data[12]),
        self.var_Salary.set(data[13]), 
        self.var_photo.set(data[14])

        # ------update----------
    def update_function(self):
        if (self.var_Department.get() == "Select Department" or self.var_Name.get() == "" or self.var_Employee_id.get() == ""):
            messagebox.showerror("Error", "All fields are Required", parent=self.root)
        else:
            try:
                up = messagebox.askyesno("Update", "Want to update details", parent=self.root)
                if up:
                    conn = pymysql.connect(host="localhost", user="root", password="Abhiash#1234", database='studentinfo')
                    my_cursor = conn.cursor()
                    my_cursor.execute("update studentdetails set Department=%s, Qualification=%s, Year=%s, Expereince=%s, "
                                  "Name=%s, Timing=%s, Blood_grp=%s, Gender=%s, Date_of_birth=%s, E_mail=%s, "
                                  "Phone_no=%s, Address=%s, Salary=%s, Photo=%s "
                                  "where Employee_Id=%s",
                                  (self.var_Department.get(), self.var_Qualification.get(), self.var_Year.get(),
                                   self.var_Expereince.get(), self.var_Name.get(), self.var_div.get(),
                                   self.var_Blood.get(), self.var_Gender.get(), self.var_Date_of_Birth.get(), self.var_E_mail.get(),
                                   self.var_Phone.get(), self.var_address.get(), self.var_Salary.get(),
                                   self.var_photo.get(), self.var_Employee_id.get()))
                    messagebox.showinfo("Success", "Employee Details Updated", parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_Employee_id.get()=="":
            messagebox.showerror("Error","EmployeeId required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Employee Delete Page","Want to delete employee info",parent=self.root)
                if delete>0:
                    conn = pymysql.connect(host="localhost", user="root", password="Abhiash#1234",database='studentinfo')
                    my_cursor = conn.cursor()
                    my_cursor.execute("delete from studentdetails where Employee_Id=%s",(self.var_Employee_id.get()))
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"error due to:{str(es)}",parent=self.root)

    def open_photo_capture(self):
        self.photo_window = tk.Toplevel(self.root)
        #self.image_app = FaceRecognitionSystem(self.photo_window)

    def reset(self):
        self.var_Department.set("Select Department")
        self.var_Qualification.set("Select Qualification") 
        self.var_Year.set("Select Year") 
        self.var_Expereince.set("Select Semester") 
        self.var_Employee_id.set("")  
        self.var_Name.set("") 
        self.var_div.set("Select Slot")
        self.var_Blood.set("") 
        self.var_Gender.set("Male") 
        self.var_Date_of_Birth.set("") 
        self.var_E_mail.set("")
        self.var_Phone.set("") 
        self.var_address.set("") 
        self.var_Salary.set("") 
        self.var_photo.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

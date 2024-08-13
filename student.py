from ast import main
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import RIDGE
import mysql.connector
import cv2
import os

class Student:
   def __init__(self,root):
       self.root=root
       self.root.geometry("1530x790+0+0")
       # self.root.resizable(False,False)
       self.root.title("Face Recognition Attendance System")

       #variables
       self.var_dep=StringVar()
       self.var_course=StringVar()
       self.var_year=StringVar()
       self.var_sem=StringVar()
       self.var_id=StringVar()
       self.var_name=StringVar()
       self.var_div=StringVar()
       self.var_roll=StringVar()
       self.var_gender=StringVar()
       self.var_dob=StringVar()
       self.var_email=StringVar()
       self.var_phone=StringVar()
       self.var_address=StringVar()
       self.var_teacher=StringVar()
       self.usertype = StringVar()


       #background image
       img2 = Image.open("images/student_details.jpg")
       img2 = img2.resize((1600, 710), Image.BILINEAR)
       self.photoImg2 = ImageTk.PhotoImage(img2)
       bg_label = Label(self.root, image=self.photoImg2)
       bg_label.place(x=0, y=0, width=1600, height=710)

       #college logo
       img1 = Image.open("images/logo.png")
       img1 = img1.resize((130, 130), Image.BILINEAR)
       self.photoImg1 = ImageTk.PhotoImage(img1)
       logo_label = Label(self.root, image=self.photoImg1, bg="white")  
       logo_label.place(x=620, y=0, width=130, height=130)

       #title
       title=Label(bg_label,text="STUDENT DETAILS",font=("Courier New",30,"bold"),bg="white",fg="maroon")
       title.place(x=0,y=130,width=1400,height=45)

       #mainframe
       main_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white", borderwidth=10)
       main_frame.place(x=15,y=190,width=1335,height=510)

       #leftframe for student information
       left_frame=LabelFrame(main_frame,bd=4,padx=2,relief=RIDGE,fg="crimson",bg="white",font=("Courier New",12,"bold"),text="Course and Student Information ", borderwidth=5)
       left_frame.place(x=10,y=10,width=680,height=475)

       #couse information frame
       course_frame=LabelFrame(left_frame,bd=4,padx=2,relief=RIDGE,fg="green",bg="white",font=("Courier New",11,"bold"),text="Course Information ", borderwidth=5)
       course_frame.place(x=8,y=1,width=640,height=100)

       #department label entries
       dep_label=Label(course_frame,font=("Courier New",10,"bold"),text="Department:",bg="white")
       dep_label.grid(row=0,column=0,sticky=W,padx=2,pady=10)
       com_dep=ttk.Combobox(course_frame,textvariable=self.var_dep,state="readonly",font=("Courier New",10,"bold"),width=17)
       com_dep['value']=("Select Department","Computer Science","Commerce")
       com_dep.current(0)
       com_dep.grid(row=0,column=1,sticky=W,padx=2)

       #course label entries
       course_label=Label(course_frame,font=("Courier New",10,"bold"),text="Course:",bg="white")
       course_label.grid(row=0,column=2,sticky=W,padx=2,pady=10)
       com_course=ttk.Combobox(course_frame,textvariable=self.var_course,state="readonly",font=("Courier New",10,"bold"),width=17)
       com_course['value']=("Select Course","PUC","BCA","BCom")
       com_course.current(0)
       com_course.grid(row=0,column=3,sticky=W,padx=2,pady=10)

       #year label entries
       year_label=Label(course_frame,font=("Courier New",10,"bold"),text="Year:",bg="white")
       year_label.grid(row=1,column=0,sticky=W,padx=2,pady=10)
       com_year=ttk.Combobox(course_frame,textvariable=self.var_year,state="readonly",font=("Courier New",10,"bold"),width=17)
       com_year['value']=("Select Year","2020-2021","2021-2020","2020-2023","2023-2024")
       com_year.current(0)
       com_year.grid(row=1,column=1,sticky=W,padx=2)

       #semster label entries
       sem_label=Label(course_frame,font=("Courier New",10,"bold"),text="Semester:",bg="white")
       sem_label.grid(row=1,column=2,sticky=W,padx=2,pady=10)
       com_sem=ttk.Combobox(course_frame,textvariable=self.var_sem,state="readonly",font=("Courier New",10,"bold"),width=17)
       com_sem['value']=("Select Semester","Semster-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6")
       com_sem.current(0)
       com_sem.grid(row=1,column=3,sticky=W,padx=2,pady=10)

       #student information frame
       student_info_frame=LabelFrame(left_frame,bd=4,padx=2,relief=RIDGE,fg="green",bg="white",font=("Courier New",11,"bold"),text="Student Information ", borderwidth=5)
       student_info_frame.place(x=10,y=100,width=640,height=260)

       #student id 
       id_label=Label(student_info_frame,font=("Courier New",10,"bold"),text="Student ID:",bg="white")
       id_label.grid(row=0,column=0,sticky=W,padx=2,pady=7)

       id_entry=ttk.Entry(student_info_frame,textvariable=self.var_id,width=20,font=("Courier New",10,"bold"))
       id_entry.grid(row=0,column=1,padx=2,pady=7)

       #student name 
       name_label=Label(student_info_frame,font=("Courier New",10,"bold"),text="Student Name:",bg="white")
       name_label.grid(row=0,column=2,sticky=W,padx=2,pady=7)

       name_entry=ttk.Entry(student_info_frame,textvariable=self.var_name,width=20,font=("Courier New",10,"bold"))
       name_entry.grid(row=0,column=3,padx=2,pady=7)

       #Class Division
       div_label=Label(student_info_frame,font=("Courier New",10,"bold"),text="Class Division:",bg="white")
       div_label.grid(row=1,column=0,sticky=W,padx=2,pady=7)
       com_div=ttk.Combobox(student_info_frame,textvariable=self.var_div,state="readonly",font=("Courier New",10,"bold"),width=18)
       com_div['value']=("Select Division","A","B","C")
       com_div.current(0)
       com_div.grid(row=1,column=1,sticky=W,padx=2,pady=7)

       #roll number
       roll_num_label=Label(student_info_frame,font=("Courier New",10,"bold"),text="Roll No:",bg="white")
       roll_num_label.grid(row=1,column=2,sticky=W,padx=2,pady=7)
       roll_num_entry=ttk.Entry(student_info_frame,textvariable=self.var_roll,width=20,font=("Courier New",10,"bold"))
       roll_num_entry.grid(row=1,column=3,padx=2,pady=7)

       #gender
       gender_label=Label(student_info_frame,font=("Courier New",10,"bold"),text="Gender:",bg="white")
       gender_label.grid(row=2,column=0,sticky=W,padx=2,pady=7)
       com_gender=ttk.Combobox(student_info_frame,textvariable=self.var_gender,state="readonly",font=("Courier New",10,"bold"),width=18)
       com_gender['value']=("Select Gender","Male","Female","Other")
       com_gender.current(0)
       com_gender.grid(row=2,column=1,sticky=W,padx=2,pady=7)

       #DOB
       dob_label=Label(student_info_frame,font=("Courier New",10,"bold"),text="DOB:",bg="white")
       dob_label.grid(row=2,column=2,sticky=W,padx=2,pady=7)
       dob_entry=ttk.Entry(student_info_frame,textvariable=self.var_dob,width=20,font=("Courier New",10,"bold"))
       dob_entry.grid(row=2,column=3,padx=2,pady=7)

       #email
       email_label=Label(student_info_frame,font=("Courier New",10,"bold"),text="Email:",bg="white")
       email_label.grid(row=3,column=0,sticky=W,padx=2,pady=7)
       email_entry=ttk.Entry(student_info_frame,textvariable=self.var_email,width=20,font=("Courier New",10,"bold"))
       email_entry.grid(row=3,column=1,padx=2,pady=7)

       #phone
       phone_label=Label(student_info_frame,font=("Courier New",10,"bold"),text="Phone No:",bg="white")
       phone_label.grid(row=3,column=2,sticky=W,padx=2,pady=7)
       phone_entry=ttk.Entry(student_info_frame,textvariable=self.var_phone,width=20,font=("Courier New",10,"bold"))
       phone_entry.grid(row=3,column=3,padx=2,pady=7)

       #address
       address_label=Label(student_info_frame,font=("Courier New",10,"bold"),text="Address:",bg="white")
       address_label.grid(row=4,column=0,sticky=W,padx=2,pady=7)
       address_entry=ttk.Entry(student_info_frame,textvariable=self.var_address,width=20,font=("Courier New",10,"bold"))
       address_entry.grid(row=4,column=1,padx=2,pady=7)

       #teacher
       teacher_id_label=Label(student_info_frame,font=("Courier New",10,"bold"),text="Teacher ID:",bg="white")
       teacher_id_label.grid(row=4,column=2,sticky=W,padx=2,pady=7)
       teacher_id_entry=ttk.Entry(student_info_frame,textvariable=self.var_teacher,width=20,font=("Courier New",10,"bold"))
       teacher_id_entry.grid(row=4,column=3,padx=2,pady=7)
       
       #style
       style = ttk.Style()
       style.configure("Custom.TRadiobutton", font=("Courier New", 10, "bold"))

       #radio buttons
       #take photo sample
       radiobtn1=ttk.Radiobutton(student_info_frame,variable=self.usertype, text="Take Photo Sample",style="Custom.TRadiobutton", value="Yes")
       radiobtn1.grid(row=5, column=0,pady=10)

       #no photo sample
       radiobtn2=ttk.Radiobutton(student_info_frame,variable=self.usertype, text="No Photo Sample",style="Custom.TRadiobutton", value="No")
       radiobtn2.grid(row=5, column=1,pady=10)

       #buttonframes
       ButtonFrame1=Frame(left_frame,bd=3,relief=RIDGE)
       ButtonFrame1.place(x=0,y=380,width=650,height=38)

       ButtonFrame2=Frame(left_frame,bd=3,relief=RIDGE)
       ButtonFrame2.place(x=0,y=415,width=650,height=38)

       #buttons
       btnPhoto=Button(ButtonFrame1,text="SAVE STUDENT INFO/ADD PHOTO SAMPLE",command=self.generate_dataset,font=("Courier New",10,"bold"),width=85,bg="darkblue",fg="white")
       btnPhoto.grid(row=1,column=0,padx=1)

       btnAddData=Button(ButtonFrame2,text="UPDATE",command=self.save_or_update_student,font=("Courier New",10,"bold"),width=26,bg="darkblue",fg="white")
       btnAddData.grid(row=0,column=0,padx=1)

       btnUpdate=Button(ButtonFrame2,text="DELETE",command=self.delete_data,font=("Courier New",10,"bold"),width=26,bg="darkblue",fg="white")
       btnUpdate.grid(row=0,column=1,padx=1)

       btnDelete=Button(ButtonFrame2,text="RESET",command=self.reset_data,font=("Courier New",10,"bold"),width=26,bg="darkblue",fg="white")
       btnDelete.grid(row=0,column=2,padx=1)
       
       #rightframe for student details
       right_frame = LabelFrame(main_frame, bd=4, padx=2, relief=RIDGE, fg="crimson", bg="white",
                         font=("Courier New", 12, "bold"), text="Student Details ", borderwidth=5)
       right_frame.place(x=700, y=10, width=600, height=475)


       #tableframe
       scroll_Table_frame = Frame(right_frame, bd=3, relief=RIDGE, bg="white")
       scroll_Table_frame.place(x=5, y=5, width=580, height=440)

       # Scrollbars
       scroll_x = ttk.Scrollbar(scroll_Table_frame, orient=HORIZONTAL)
       scroll_y = ttk.Scrollbar(scroll_Table_frame, orient=VERTICAL)

       # Table
       self.student_table = ttk.Treeview(scroll_Table_frame, columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
       scroll_x.pack(side=BOTTOM, fill=X)
       scroll_y.pack(side=RIGHT, fill=Y)

       scroll_x.config(command=self.student_table.xview)
       scroll_y.config(command=self.student_table.yview)

       # Table headings
       self.student_table.heading("dep", text="Department")
       self.student_table.heading("course", text="Course")
       self.student_table.heading("year", text="Year")
       self.student_table.heading("sem", text="Semester")
       self.student_table.heading("id", text="StudentID")
       self.student_table.heading("name", text="Student Name")
       self.student_table.heading("div", text="Class Div")
       self.student_table.heading("roll", text="Roll No")
       self.student_table.heading("gender", text="Gender")
       self.student_table.heading("dob", text="DOB")
       self.student_table.heading("email", text="Email")
       self.student_table.heading("phone", text="Phone No")
       self.student_table.heading("address", text="Address")
       self.student_table.heading("teacher", text="Teacher ID")
       self.student_table.heading("photo", text="PhotoSampleStatus")


       self.student_table["show"] = "headings"

       self.student_table.column("dep", width=100)
       self.student_table.column("course", width=100)
       self.student_table.column("year", width=100)
       self.student_table.column("sem", width=100)
       self.student_table.column("id", width=100)
       self.student_table.column("name", width=100)
       self.student_table.column("div", width=100)
       self.student_table.column("roll", width=100)
       self.student_table.column("gender", width=100)
       self.student_table.column("dob", width=100)
       self.student_table.column("email", width=100)
       self.student_table.column("phone", width=100)
       self.student_table.column("address", width=100)
       self.student_table.column("teacher", width=100)
       self.student_table.column("photo", width=100)
       self.student_table.pack(fill=BOTH, expand=1)
       self.student_table.bind("<ButtonRelease>",self.get_cursor)
       self.fetch_data()
       # Changed to pack for consistency with scrollbars
       
       #exit
       exit_button = Button(title, text="Back", font=("Courier New", 10, "bold"), bg="darkblue", fg="white", bd=0, command=self.root.destroy)
       exit_button.place(relx=0.95, rely=0.95, anchor=SE, width=60, height=40)

        
   def save_or_update_student(self):
    if self.validate_input():
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Mansa@2088", database="face_recognizer")
            my_cursor = conn.cursor()
            
            # Check if student already exists
            my_cursor.execute("SELECT * FROM student WHERE id=%s", (self.var_id.get(),))
            result = my_cursor.fetchone()
            
            if result:
                # Update existing student
                update_query = """
                UPDATE student 
                SET dep=%s, course=%s, year=%s, sem=%s, name=%s, `div`=%s, roll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photosample=%s 
                WHERE id=%s
                """
                values = (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_sem.get(), self.var_name.get(), 
                          self.var_div.get(), self.var_roll.get(), self.var_gender.get(), self.var_dob.get(), self.var_email.get(), 
                          self.var_phone.get(), self.var_address.get(), self.var_teacher.get(), self.usertype.get(), self.var_id.get())
                my_cursor.execute(update_query, values)
                messagebox.showinfo("Success", "Student record updated successfully", parent=self.root)
            else:
                # Insert new student
                insert_query = """
                INSERT INTO student (dep, course, year, sem, id, name, `div`, roll, gender, dob, email, phone, address, teacher, photosample)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_sem.get(), self.var_id.get(), 
                          self.var_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(), self.var_dob.get(), 
                          self.var_email.get(), self.var_phone.get(), self.var_address.get(), self.var_teacher.get(), self.usertype.get())
                my_cursor.execute(insert_query, values)
                messagebox.showinfo("Success", "New student record added successfully", parent=self.root)
            
            conn.commit()
            self.fetch_data()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    else:
        messagebox.showerror("Validation Error", "Please fill all required fields", parent=self.root)

   def validate_input(self):
    if (self.var_dep.get() == "Select Department" or self.var_id.get() == "" or self.var_name.get() == "" or
        self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or
        self.var_div.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "" or
        self.var_dob.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or
        self.var_address.get() == "" or self.var_teacher.get() == ""):
        return False
    return True

   def capture_photo_samples(self):
    if self.validate_input() and self.usertype.get() == "Yes":
        try:
            # Your existing photo capture logic here
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, h, w) in faces:
                    face_cropped = img[y:y+h, x:x+w]
                    return face_cropped
            
            cap = cv2.VideoCapture(0)
            self.img_id = 0
            while True:
                ret, frame = cap.read()
                if face_cropped(frame) is not None:
                    self.img_id += 1
                    face = cv2.resize(face_cropped(frame), (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = f"data/user.{self.var_id.get()}.{self.img_id}.jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(self.img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)

                if cv2.waitKey(1) == 13 or int(self.img_id) == 100:
                    break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Generating datasets completed!!!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

   #function
   def add_data(self):
       if (self.var_dep.get()=="Select Department" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_name.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_teacher.get()==""):
           messagebox.showerror("Error","All Fields Are Required",parent=self.root)
       else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="Mansa@2088", database="face_recognizer")
                my_cursor= conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_dep.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_sem.get(),
                                                                                                    self.var_id.get(),
                                                                                                    self.var_name.get(),
                                                                                                    self.var_div.get(),
                                                                                                    self.var_roll.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_teacher.get(),
                                                                                                    self.usertype.get()
                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Suceess",f"Student Details has been added...!!!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #fetch data from database
   def fetch_data(self):
       conn=mysql.connector.connect(host="localhost", username="root", password="Mansa@2088", database="face_recognizer")
       my_cursor= conn.cursor()
       my_cursor.execute("select * from student")
       data=my_cursor.fetchall()
       
       if len(data)!=0:
           self.student_table.delete(*self.student_table.get_children())
           for i in data:
               self.student_table.insert("",END,values=i)
           conn.commit()
       conn.close()

    #get cursor data
   def get_cursor(self, event=""):
       cursor_focus=self.student_table.focus()
       content=self.student_table.item(cursor_focus)
       data=content["values"]

       self.var_course.set(data[1]),
       self.var_dep.set(data[0]),
       self.var_year.set(data[2]),
       self.var_sem.set(data[3]),
       self.var_id.set(data[4]),
       self.var_name.set(data[5]),
       self.var_div.set(data[6]),
       self.var_roll.set(data[7]),
       self.var_gender.set(data[8]),
       self.var_dob.set(data[9]),
       self.var_email.set(data[10]),
       self.var_phone.set(data[11]),
       self.var_address.set(data[12]),
       self.var_teacher.set(data[13]),
       self.usertype.set(data[14])

   #update function
   def update_data(self):
    if (self.var_dep.get() == "Select Department" or self.var_id.get() == "" or self.var_name.get() == "" or
        self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or
        self.var_div.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "" or
        self.var_dob.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or
        self.var_address.get() == "" or self.var_teacher.get() == ""):
        messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
    else:
        try:
            Update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)
            if Update > 0:
                conn = mysql.connector.connect(host="localhost", username="root", password="Mansa@2088", database="face_recognizer")
                my_cursor = conn.cursor()
                update_query = """
                UPDATE student 
                SET dep=%s, course=%s, year=%s, sem=%s, name=%s, `div`=%s, roll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photosample=%s 
                WHERE id=%s
                """
                my_cursor.execute(update_query, (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.usertype.get(),
                    self.var_id.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
            else:
                if not Update:
                    return
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


   def delete_data(self):
       if self.var_id.get()=="":
           messagebox.showerror("Error","Student ID is required to delete the record",parent=self.root)
       else:
           try:
               delete=messagebox.askyesno("Delete","Are you sure you want to delete this record?",parent=self.root)
               if delete>0:
                   conn=mysql.connector.connect(host="localhost", username="root", password="Mansa@2088", database="face_recognizer")
                   my_cursor=conn.cursor()
                   sql="delete from student where id=%s"
                   val=(self.var_id.get(),)
                   my_cursor.execute(sql,val)
               else:
                   if not delete:
                       return
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("Delete","Student record has been deleted",parent=self.root)
           except Exception as es:
               messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

   #reset function
   def reset_data(self):
       self.var_dep.set("Select Department")
       self.var_course.set("Select Course")
       self.var_year.set("Select Year")
       self.var_sem.set("Select Semester")
       self.var_id.set("")
       self.var_name.set("")
       self.var_div.set("Select Division")
       self.var_roll.set("")
       self.var_gender.set("Select Gender")
       self.var_dob.set("")
       self.var_email.set("")
       self.var_phone.set("")
       self.var_address.set("")
       self.var_teacher.set("")
       self.usertype.set("")

  #generate dataset and take photo sample
   def generate_dataset(self):
    self.save_or_update_student()
    self.capture_photo_samples()
if __name__ == '__main__':
    root = Tk()
    obj = Student(root)
    root.mainloop()
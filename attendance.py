from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import RIDGE
import mysql.connector
import cv2
import csv
import os
from tkinter import filedialog


myData=[]
class Attendance:
   def __init__(self,root):
       self.root=root
       self.root.geometry("1530x790+0+0")
       # self.root.resizable(False,False)
       self.root.title("Attendance")

       #variables
       self.var_atten_id=StringVar()
       self.var_atten_roll=StringVar()
       self.var_atten_name=StringVar()
       self.var_atten_dep=StringVar()
       self.var_atten_time=StringVar()
       self.var_atten_date=StringVar()
       self.var_atten_attendance=StringVar()

       #background image
       img2 = Image.open("images/projects.jpg")
       img2 = img2.resize((1600, 710), Image.BILINEAR)
       self.photoImg2 = ImageTk.PhotoImage(img2)
       bg_label = Label(self.root, image=self.photoImg2)
       bg_label.place(x=0, y=0, width=1600, height=710)

       #college logo
       img1 = Image.open("images/logo.png")
       img1 = img1.resize((130, 130), Image.BILINEAR)
       self.photoImg1 = ImageTk.PhotoImage(img1)
       logo_label = Label(self.root, image=self.photoImg1, bg="white")  # Optional: bg color for contrast
       logo_label.place(x=630, y=0, width=130, height=130)

       #title
       title=Label(bg_label,text="ATTENDANCE",font=("Courier New",30,"bold"),bg="white",fg="maroon")
       title.place(x=0,y=130,width=1400,height=45)
       
       exit_button = Button(title, text="Back", font=("Courier New", 10, "bold"), bg="darkblue", fg="white", bd=0, command=self.root.destroy)
       exit_button.place(relx=0.95, rely=0.95, anchor=SE, width=60, height=40)

       #mainframe
       main_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white", borderwidth=10)
       main_frame.place(x=15,y=190,width=1335,height=510)

       #leftframe for student information
       left_frame=LabelFrame(main_frame,bd=4,padx=2,relief=RIDGE,fg="darkblue",bg="white",font=("Courier New",10,"bold"),text="Student Attendance Details", borderwidth=5)
       left_frame.place(x=10,y=10,width=680,height=475)

       info_frame=LabelFrame(left_frame,bd=4,padx=2,relief=RIDGE,fg="green",bg="white",font=("Courier New",10,"bold"),text="Attendance Information ", borderwidth=5)
       info_frame.place(x=8,y=1,width=640,height=240)

       #attendance id 
       id_label=Label(info_frame,font=("Courier New",10,"bold"),text="Attendance ID:",bg="white")
       id_label.grid(row=0,column=0,sticky=W,padx=2,pady=7)

       id_entry=ttk.Entry(info_frame,width=20,textvariable=self.var_atten_id,font=("Courier New",10,"bold"))
       id_entry.grid(row=0,column=1,padx=2,pady=7)

       #Roll
       roll_label=Label(info_frame,font=("Courier New",10,"bold"),text="Roll No.:",bg="white")
       roll_label.grid(row=0,column=2,sticky=W,padx=2,pady=7)

       roll_entry=ttk.Entry(info_frame,width=20,textvariable=self.var_atten_roll,font=("Courier New",10,"bold"))
       roll_entry.grid(row=0,column=3,padx=2,pady=7)

       #Name
       name_label=Label(info_frame,font=("Courier New",10,"bold"),text="Name:",bg="white")
       name_label.grid(row=1,column=0,sticky=W,padx=2,pady=7)

       name_entry=ttk.Entry(info_frame,width=20,textvariable=self.var_atten_name,font=("Courier New",10,"bold"))
       name_entry.grid(row=1,column=1,padx=2,pady=7)

       #department
       dep_label=Label(info_frame,font=("Courier New",10,"bold"),text="Department:",bg="white")
       dep_label.grid(row=1,column=2,sticky=W,padx=2,pady=7)

       dep_entry=ttk.Entry(info_frame,width=20,textvariable=self.var_atten_dep,font=("Courier New",10,"bold"))
       dep_entry.grid(row=1,column=3,padx=2,pady=7)

       #time
       time_label=Label(info_frame,font=("Courier New",10,"bold"),text="Time:",bg="white")
       time_label.grid(row=2,column=0,sticky=W,padx=2,pady=7)

       time_entry=ttk.Entry(info_frame,width=20,textvariable=self.var_atten_time,font=("Courier New",10,"bold"))
       time_entry.grid(row=2,column=1,padx=2,pady=7)

       #date
       date_label=Label(info_frame,font=("Courier New",10,"bold"),text="Date:",bg="white")
       date_label.grid(row=2,column=2,sticky=W,padx=2,pady=7)

       date_entry=ttk.Entry(info_frame,width=20,textvariable=self.var_atten_date,font=("Courier New",10,"bold"))
       date_entry.grid(row=2,column=3,padx=2,pady=7)

       #attendance status
       att_label=Label(info_frame,font=("Courier New",10,"bold"),text="Attendance Status",bg="white")
       att_label.grid(row=3,column=0,sticky=W,padx=2,pady=10)
       com_att=ttk.Combobox(info_frame,state="readonly",textvariable=self.var_atten_attendance,font=("Courier New",10,"bold"),width=17)
       com_att['value']=("Select ","Present","Absent")
       com_att.current(0)
       com_att.grid(row=3,column=1,sticky=W,padx=2)

       ButtonFrame2=Frame(left_frame,bd=3,relief=RIDGE)
       ButtonFrame2.place(x=0,y=280,width=650,height=40)

       #buttons
       btnPhoto=Button(ButtonFrame2,text="Import CSV",command=self.importCsv,font=("Courier New",12,"bold"),width=31,bg="darkblue",fg="white")
       btnPhoto.grid(row=0,column=0,padx=1)

       btnAddData=Button(ButtonFrame2,text="Export CSV",command=self.exportCsv,font=("Courier New",12,"bold"),width=31,bg="darkblue",fg="white")
       btnAddData.grid(row=0,column=1,padx=1)


       #rightframe for student details
       right_frame = LabelFrame(main_frame, bd=4, padx=2, relief=RIDGE, fg="darkblue", bg="white",
                         font=("Courier New", 12, "bold"), text="Student Details ", borderwidth=5)
       right_frame.place(x=700, y=10, width=600, height=475)

       Table_frame=LabelFrame(right_frame,text="View Student Details",font=("Courier New",12,"bold"),bg="white",bd=3,relief=RIDGE)
       Table_frame.place(x=5,y=5,width=580,height=430)

       # Scrollbars
       scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
       scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

       self.AttendanceReportTable=ttk.Treeview(Table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)

       scroll_x.config(command=self.AttendanceReportTable.xview)
       scroll_y.config(command=self.AttendanceReportTable.yview)

       self.AttendanceReportTable.heading("id",text="Student ID")
       self.AttendanceReportTable.heading("roll",text="Roll")
       self.AttendanceReportTable.heading("name",text="Name")
       self.AttendanceReportTable.heading("department",text="Department")
       self.AttendanceReportTable.heading("time",text="Time")
       self.AttendanceReportTable.heading("date",text="Date")
       self.AttendanceReportTable.heading("attendance",text="Attendance")
       self.AttendanceReportTable["show"]="headings"
    
       self.AttendanceReportTable.column("id",width=100)
       self.AttendanceReportTable.column("roll",width=100)
       self.AttendanceReportTable.column("name",width=100)
       self.AttendanceReportTable.column("department",width=100)
       self.AttendanceReportTable.column("time",width=100)
       self.AttendanceReportTable.column("date",width=100)
       self.AttendanceReportTable.column("attendance",width=100)
       self.AttendanceReportTable.pack(fill=BOTH,expand=1)

       self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

   def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mansa@2088",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student_attendance")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in data:
                self.AttendanceReportTable.insert("",END,values=i)
            conn.commit()
        conn.close()

   def importCsv(self):
    global myData
    myData.clear()
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
    if fln:
        print(f"Selected file: {fln}")
        with open(fln, newline='') as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for row in csvread:
                print(row)  # Debugging print to see the rows being read
                myData.append(row)
        self.fetchData(myData)

   def fetchData(self, data):
    if len(data) != 0:
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in data:
            self.AttendanceReportTable.insert("", END, values=i)
        print("Data inserted into Treeview")  # Debugging print
    else:
        print("No data found")  # Debugging print

   def exportCsv(self):
        try:
            if len (myData) <1:
                messagebox.showerror("No Data","No Data to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open (fln,mode="w",newline="") as myfile:
                exp_writer=csv.writer(myfile,delimiter=",")
                for i in myData:
                        exp_writer.writerow(i)
                messagebox.showinfo("Data Exported","Your data exported to " +os.path.basename(fln)+ " Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

   def get_cursor(self, event=""):
    cursor_rows = self.AttendanceReportTable.focus()
    if cursor_rows:
        content = self.AttendanceReportTable.item(cursor_rows)
        row = content["values"]
        if row:
            self.var_atten_id.set(row[0])
            self.var_atten_roll.set(row[1])
            self.var_atten_name.set(row[2])
            self.var_atten_dep.set(row[3])
            self.var_atten_time.set(row[4])
            self.var_atten_date.set(row[5])
            self.var_atten_attendance.set(row[6])
        else:
            print("No data found in selected row")
    else:
        print("No row selected")

   def action(self):
        id=self.var_atten_id.get()
        roll=self.var_atten_roll.get()
        name=self.var_atten_name.get()
        dep=self.var_atten_dep.get()
        time=self.var_atten_time.get()
        date=self.var_atten_date.get()
        attendn=self.var_atten_attendance.get()

        # write to csv file
        try:
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="a",newline="\n") as f:
                dict_writer=csv.DictWriter(f,fieldnames=(["ID","Roll","Name","Department","Time","Date","Attendance"]))
                dict_writer.writeheader()
                dict_writer.writerow({
                "ID":id,
                "Roll":roll,
                "Name":name,
                "Department":dep,
                "Time":time,
                "Date":date,
                "Attendance":attendn 
                    })
            messagebox.showinfo("Data Exported","Your data exported to " +os.path.basename(fln)+ " Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

   def clear(self):
    self.var_atten_id.set("")
    self.var_atten_roll.set("")
    self.var_atten_name.set("")
    self.var_atten_dep.set("")
    self.var_atten_time.set("")
    self.var_atten_date.set("")
    self.var_atten_attendance.set("")
    # Remove the following line, as `self.atten_id` is not defined
    # self.atten_id.focus()



if __name__ == '__main__':
    root = Tk()
    obj = Attendance(root)
    root.mainloop()

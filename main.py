from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
from recognize import Recognize
from attendance import Attendance
from project import Project
import os

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        # Background image
        img2 = Image.open("images/background.jpg").resize((1600, 710), Image.BILINEAR)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        bg_label = Label(self.root, image=self.photoImg2)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # College logo
        img1 = Image.open("images/logo.png").resize((100, 100), Image.BILINEAR)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        logo_label = Label(self.root, image=self.photoImg1, bg="white")
        logo_label.place(x=630, y=0, width=130, height=130)

        # Title
        title_text = "FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE"
        title_font = ("Courier New", 30, "bold")
        title_label = Label(self.root, text=title_text, font=title_font, bg="white", fg="maroon")
        title_label.place(relx=0.5, rely=0.20, anchor=CENTER)

        # Button frame
        btn_frame = Frame(bg_label, bg="white")
        btn_frame.place(relx=0.5, rely=0.6, anchor=CENTER, width=900, height=500)

        # Define buttons and their images
        buttons = [
            ("images/student_details.jpg", "Student Details", self.student_details),
            ("images/train_data.jpeg", "Train Data", self.train_data),
            ("images/face_recog.png", "Face Recognition", self.recognize),
            ("images/attendance.png", "Attendance", self.attendance),
            ("images/photos.jpg", "Photos", self.open_img),
            ("images/projects.jpg", "Project Details", self.project)
        ]

        # Create buttons dynamically
        for i, (img_path, text, command) in enumerate(buttons):
            img = Image.open(img_path).resize((200, 150), Image.BILINEAR)
            photo_img = ImageTk.PhotoImage(img)
            
            button = Button(btn_frame, image=photo_img, command=command, cursor="hand2", bd=0, highlightthickness=0)
            button.image = photo_img  # Keep a reference to avoid garbage collection
            button.grid(row=i // 3 * 2, column=i % 3, padx=40, pady=(20, 5), ipadx=10, ipady=10)

            label = Label(btn_frame, text=text, font=("Courier New", 18, "bold"), bg="white", fg="darkblue")
            label.grid(row=(i // 3) * 2 + 1, column=i % 3, padx=20, pady=(5, 20))

            # Adding hover effect
            button.bind("<Enter>", lambda e, b=button: b.config(bg="lightblue"))
            button.bind("<Leave>", lambda e, b=button: b.config(bg="SystemButtonFace"))
            
        #exit
        exit_button = Button(self.root, text="Exit", font=("Courier New", 10, "bold"), bg="red", fg="white", bd=0, command=self.root.destroy)
        exit_button.place(relx=0.95, rely=0.95, anchor=SE, width=60, height=30)


    # Functions
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def recognize(self):
        self.new_window = Toplevel(self.root)
        self.app = Recognize(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def project(self):
        self.new_window = Toplevel(self.root)
        self.app = Project(self.new_window)

    def open_img(self):
        os.startfile("data")

if __name__ == '__main__':
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()

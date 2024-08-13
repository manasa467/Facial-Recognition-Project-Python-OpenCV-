from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
from datetime import datetime

class Recognize:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        # Background image
        self.set_background_image("images/photos.jpg", 1600, 710)

        # College logo
        self.set_logo("images/logo.png", 130, 130)

        # Title with Back button
        self.set_title_with_back_button()

        # Detect Face button
        self.set_detect_face_button()

        self.attendance_taken = False  # Flag to track if attendance has been taken

    def set_background_image(self, image_path, width, height):
        img = Image.open(image_path)
        img = img.resize((width, height), Image.BILINEAR)
        self.photoImg = ImageTk.PhotoImage(img)
        bg_label = Label(self.root, image=self.photoImg)
        bg_label.place(x=0, y=0, width=width, height=height)

    def set_logo(self, image_path, width, height):
        img = Image.open(image_path)
        img = img.resize((130,130), Image.BILINEAR)
        self.photoImg1 = ImageTk.PhotoImage(img)
        logo_label = Label(self.root, image=self.photoImg1, bg="white")
        logo_label.place(x=620, y=0, width=130, height=130)

    def set_title_with_back_button(self):
        title=Label(self.root,text="DETECT FACE",font=("Courier New",30,"bold"),bg="white",fg="maroon")
        title.place(x=0,y=130,width=1400,height=45)

        exit_button = Button(title, text="Back", font=("Courier New", 10, "bold"), bg="darkblue", fg="white", bd=0, command=self.root.destroy)
        exit_button.place(relx=0.95, rely=0.95, anchor=SE, width=60, height=40)

    def set_detect_face_button(self):
        detect_button = Button(self.root, text="Detect Face", command=self.detect_face, borderwidth=5, cursor="hand2",
                               font=("Courier New", 10, "bold"), fg="white", bg="darkblue")
        detect_button.place(x=580, y=400, width=230, height=50)

    def mark_attendance(self, d, k, s, i):
        file_path = os.path.join(os.getcwd(), "present.csv")

        # Check if the file exists; if not, create it with headers
        if not os.path.isfile(file_path):
            with open(file_path, "w", newline="\n") as f:
                f.write("ID, Roll No, Name, Department, Time, Date, Status\n")

        # Append new attendance record
        with open(file_path, "a", newline="\n") as f:
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")
            f.write(f"{d}, {k}, {i}, {s}, {dtString}, {d1}, Present\n")

    # Face recognition
    def detect_face(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coords = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, pred = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - pred / 300)))

                conn = mysql.connector.connect(host='localhost', username='root', password='Mansa@2088', database='face_recognizer')
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT name, dep, roll, id FROM student WHERE id=%s", (id,))
                record = my_cursor.fetchone()
                if record:
                    name, dep, roll, student_id = record
                else:
                    name, dep, roll, student_id = '', '', '', ''

                if confidence > 77:
                    cv2.putText(img, f"Department: {dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                    cv2.putText(img, f"Name: {name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                    cv2.putText(img, f"Roll No: {roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                    cv2.putText(img, f"Student Id: {student_id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 2)
                    if not self.attendance_taken:
                        self.mark_attendance(student_id, roll, dep, name)
                        self.attendance_taken = True
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                coords = [x, y, w, h]
            return coords

        def recognize(img, clf, faceCascade):
            coords = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        Video_Capture = cv2.VideoCapture(0)
        self.attendance_taken = False  # Reset flag before starting face detection loop

        while True:
            ret, img = Video_Capture.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Detector", img)
            if cv2.waitKey(1) == 13:  # Press Enter to break the loop
                break

        Video_Capture.release()
        messagebox.showinfo("Attendance Report", "Attendance Saved in CSV file", parent=self.root)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    root = Tk()
    obj = Recognize(root)
    root.mainloop()

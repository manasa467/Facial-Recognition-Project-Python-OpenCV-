from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        # Background image
        self.set_background_image("images/projects.jpg", 1600, 710)
        
        # College logo
        self.set_logo("images/logo.png", 130, 130)

        # Title with Back button
        self.set_title_with_back_button()

        # Train button
        self.set_train_button()

    def set_background_image(self, image_path, width, height):
        img = Image.open(image_path)
        img = img.resize((1600,700), Image.BILINEAR)
        self.photoImg = ImageTk.PhotoImage(img)
        bg_label = Label(self.root, image=self.photoImg)
        bg_label.place(x=0, y=0, width=1600, height=700)

    def set_logo(self, image_path, width, height):
        img = Image.open(image_path)
        img = img.resize((width, height), Image.BILINEAR)
        self.photoImg1 = ImageTk.PhotoImage(img)
        logo_label = Label(self.root, image=self.photoImg1, bg="white")
        logo_label.place(x=620, y=0, width=width, height=height)

    def set_title_with_back_button(self):
        title_frame = Frame(self.root, bg="white")
        title_frame.place(x=0, y=130, width=1400, height=45)

        title_label = Label(title_frame, text="TRAIN DATA", font=("Courier New", 30, "bold"), bg="white", fg="maroon")
        title_label.pack(side=LEFT, padx=560)

        exit_button = Button(title_frame, text="Back", font=("Courier New", 10, "bold"), bg="darkblue", fg="white", bd=0, command=self.root.destroy)
        exit_button.place(relx=0.95, rely=0.95, anchor=SE, width=60, height=40)

    def set_train_button(self):
        train_button = Button(self.root, text="Train Data", borderwidth=5, command=self.train_classifier, cursor="hand2",
                              font=("Courier New", 10, "bold"), fg="white", bg="darkblue")
        train_button.place(x=550, y=400, width=230, height=50)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith('.jpg')]

        faces = []
        ids = []
        for image_path in path:
            img = Image.open(image_path).convert('L')  # Convert to grayscale
            image_np = np.array(img, 'uint8')
            id = int(os.path.split(image_path)[1].split(".")[1])

            faces.append(image_np)
            ids.append(id)
            cv2.imshow("Training", image_np)
            if cv2.waitKey(1) == 13:
                break
        ids = np.array(ids)

        # Train classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!!", parent=self.root)

if __name__ == '__main__':
    root = Tk()
    obj = Train(root)
    root.mainloop()

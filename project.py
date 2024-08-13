from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import RIDGE
from PIL import Image, ImageTk
import shutil

class Project:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Project Details")

        # Background image
        img2 = Image.open("images/projects.jpg")
        img2 = img2.resize((1600, 710), Image.BILINEAR)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        bg_label = Label(self.root, image=self.photoImg2)
        bg_label.place(x=0, y=0, width=1600, height=710)

        # College logo
        img1 = Image.open("images/logo.png")
        img1 = img1.resize((130, 130), Image.BILINEAR)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        logo_label = Label(self.root, image=self.photoImg1, bg="white")
        logo_label.place(x=630, y=0, width=130, height=130)

        # Title
        title = Label(bg_label, text="PROJECT DETAILS", font=("Courier New", 30, "bold"), bg="white", fg="maroon")
        title.place(x=0, y=130, width=1400, height=45)
        
        exit_button = Button(title, text="Back", font=("Courier New", 10, "bold"), bg="darkblue", fg="white", bd=0, command=self.root.destroy)
        exit_button.place(relx=0.95, rely=0.95, anchor=SE, width=60, height=40)

        # Calculate center position
        button_frame_width = 650
        bg_label_width = 1600
        x_center = (bg_label_width - button_frame_width) // 2

        # Button frame
        ButtonFrame1 = Frame(bg_label, relief=RIDGE)
        ButtonFrame1.place(x=x_center, y=380, width=440, height=30)

        # Download report button
        btnDownloadReport = Button(ButtonFrame1, text="Download Report", font=("Courier New", 11, "bold"), width=23, bg="darkblue", fg="white", command=self.download_report)
        btnDownloadReport.grid(row=0, column=0, padx=1)

        # Download PPT button
        btnDownloadPPT = Button(ButtonFrame1, text="Download PPT", font=("Courier New", 11, "bold"), width=23, bg="darkblue", fg="white", command=self.download_ppt)
        btnDownloadPPT.grid(row=0, column=1, padx=1)

    def download_report(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            try:
                shutil.copy("C:/Users/Manasa/Desktop/Final Project/additionals/report.docx", file_path)
                messagebox.showinfo("Success", "Report downloaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to download report: {e}")

    def download_ppt(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".pptx", filetypes=[("PPTX files", "*.pptx")])
        if file_path:
            try:
                shutil.copy("C:/Users/Manasa/Desktop/Final Project/additionals/ppt.pptx", file_path)
                messagebox.showinfo("Success", "Presentation downloaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to download presentation: {e}")

if __name__ == '__main__':
    root = Tk()
    obj = Project(root)
    root.mainloop()

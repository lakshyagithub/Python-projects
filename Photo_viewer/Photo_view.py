from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.geometry("500x500")
root.configure(background="sky blue")
root_icon = PhotoImage(file="Logo.png")
root.iconphoto(False, root_icon)
root.title("Photo viewer by Lakshya")

label_image = Label(root, bg="yellow", highlightthickness=5)
label_image.place(relx=0.5, rely=0.5, anchor=CENTER)

def open_image():
    img_path = filedialog.askopenfile(title="open image", filetypes=[(
        "Image files",
        "*.png; *.jpg; *.jpeg; *.gif; *.txt"
        )])
    print("Image path: ", img_path)

open_file_btn = Button(root, text="Open file", command=open_image, bg="light green", fg="white", bd=0, font=("Comic Sans MS", 12, "bold"))
open_file_btn.place(relx=0.5, rely=0.7, anchor=CENTER)

rotate_file_btn = Button(root, text="Rotate image", command=open_image, bg="light green", fg="white", bd=0, font=("Comic Sans MS", 12, "bold"))
rotate_file_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()
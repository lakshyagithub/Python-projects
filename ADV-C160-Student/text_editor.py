from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import os

root = Tk()
root.minsize(600, 500)
root.maxsize(600, 500)

save_img = ImageTk.PhotoImage(Image.open("save.png"))
open_file_img = ImageTk.PhotoImage(Image.open("open.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))

label_file_name = Label(root, text="File name: ")
label_file_name.place(relx=0.6,rely=0.1,anchor= CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.8,rely=0.1, anchor= CENTER)

my_text= Text(root, height=20, width=60)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)

name1 = ""
def open_file():
    global name1
    input_file_name.delete(0, END)
    my_text.delete(1.0, END)
    text_file = filedialog.askopenfilename(title="Select a text file (.txt)",
                                           filetypes=(("Text documents", "*.txt"),))
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split(".")[0]
    print()

def save_file():
    print("not yet")

def exit_file():
    input_file_name.delete(0, END)
    my_text.delete(1.0, END)


open_button=Button(root, image=open_file_img, command=open_file)
open_button.place(relx=0.05,rely=0.1,anchor=CENTER)
save_button=Button(root, image=save_img, command=save_file)
save_button.place(relx=0.11,rely=0.1,anchor= CENTER)
exit_button=Button(root, image=exit_img, command=exit_file)
exit_button.place(relx=0.17,rely=0.1,anchor= CENTER)

root.mainloop()


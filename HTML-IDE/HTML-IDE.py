from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import os

root = Tk()
root.title("HTML editor - No file open")
root.config(background="sky blue")
root.minsize(600, 500)
root.maxsize(600, 500)

save_img = ImageTk.PhotoImage(Image.open("save1.png"))
open_file_img = ImageTk.PhotoImage(Image.open("open1.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit1.jpg"))

label_file_name = Label(root, text="File name: ")
label_file_name.place(relx=0.6, rely=0.1, anchor=CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.8, rely=0.1, anchor=CENTER)

my_text = Text(root, height=20, width=60, background="grey", fg="white")
my_text.place(relx=0.5, rely=0.55, anchor=CENTER)

name1 = ""


def open_file():
  global name1
  input_file_name.delete(0, END)
  my_text.delete(1.0, END)
  text_file = filedialog.askopenfilename(title="Select a html file (.html)",
                                         filetypes=(("HTML documents",
                                                     "*.html"), ))
  print(text_file)
  name = os.path.basename(text_file)
  formated_name = name.split(".")[0]
  input_file_name.insert(END, formated_name)
  root.title("HTML editor - " + formated_name)
  text_file = open(name1, 'r')
  paragraph = text_file.read()
  text_file.insert(END, paragraph)
  text_file.close()


def save_file():
  print("not yet")


def exit_file():
  input_file_name.delete(0, END)
  my_text.delete(1.0, END)
  root.title("HTML editor - No file open")


open_button = Button(root, image=open_file_img, command=open_file)
open_button.place(relx=0.05, rely=0.1, anchor=CENTER)
save_button = Button(root, image=save_img, command=save_file)
save_button.place(relx=0.11, rely=0.1, anchor=CENTER)
exit_button = Button(root, image=exit_img, command=exit_file)
exit_button.place(relx=0.17, rely=0.1, anchor=CENTER)

root.mainloop()

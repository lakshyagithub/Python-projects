from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root_icon = PhotoImage(file="start_point1.png")
root.iconphoto(False, root_icon)
root.title("Canvas")
root.geometry("600x600")

color_label = Label(root, text="Pen-down Color: ", font=("comic sans ms", 12))
color_label.place(relx=0.6, rely=0.9, anchor=CENTER)

input_box = Entry(root)
input_box.insert(0, "black")
input_box.place(relx=0.8, rely=0.9, anchor=CENTER)

canvas1 = Canvas(root, width=590, height=510, bg="white", highlightbackground="lightgray")
canvas1.pack()

root.mainloop()

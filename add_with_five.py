from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x400")
root.title("Add any number with five")

label1 = Label(root)
input_box = Entry(root)

def add():
	try:
		input_box_data = int(input_box.get())
		result1 = input_box_data + 5
		label1["text"] = result1
	except ValueError:
		messagebox.showerror("Error!", "Please put a valid number")

btn = Button(root, text="Click me to add!", command=add)
input_box.pack()
btn.pack()
label1.pack()

root.mainloop()

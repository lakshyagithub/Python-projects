from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Add any number with five")

label1 = Label(root)
input_box = Entry(root)

def add():
	input_box_data = int(input_box.get())

	try:
		result1 = input_box_data + '5'
		label1["text"] = result1
		label1 = Label(root, fg="blue").pack()
	except (TypeError):
		label1["text"] = "Please put a valid number"
		label1 = Label(root, fg="red").pack()

btn = Button(root, text="Click me to add!", command=add)
input_box.pack()
btn.pack()

root.mainloop()
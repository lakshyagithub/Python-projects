from tkinter import *
from Password_genarator import generate_password
from dict import dict1

lol1 = Tk()
lol1.geometry("600x400")
lol1.title("Add with five")

inputbox = Entry(lol1)

def add1():
    inputbox_value = inputbox.get()
    five5 = 5
	try:
			int_inputbox_data = int(inputbox_value)
			print("Answer: ", five5 + int_inputbox_data)
			print(dict1["LOL"])

	except ValueError:
			print("Please put a valid number")
	

btn = Button(lol1, text="Click me!", command=add1)
btn2 = Button(lol1, text="Generate password", command=generate_password)

inputbox.pack()
btn.pack()
btn2.pack()

lol1.mainloop()
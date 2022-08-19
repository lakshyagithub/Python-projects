from tkinter import *

root = Tk()
root.geometry("400x400")

list1 = []

input_box = Entry(root)
label1 = Label(root)

def add_to_list1():
    input_box_data = input_box.get()
    list1.append(input_box_data)

def update_label():
    label1["text"] = str(list1)

btn1 = Button(root, text="Add To The List", command=add_to_list1)
btn2 = Button(root, text="Show List", command=update_label)

input_box.pack()
label1.pack()
btn1.pack()
btn2.pack()

root.mainloop()
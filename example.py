from tkinter import *
import random

root = Tk()
root.geometry("400x400")

list1 = []
list2 = []

input1 = Entry(root)
input2 = Entry(root)
list1_label = Label(root)
list2_label = Label(root)
random_list1_label = Label(root)
random_list2_label = Label(root)

def dosomthing():
    input1_data = input1.get()
    input2_data = input2.get()
    list1.append(input1_data)
    list2.append(input2_data)
    list1_label["text"] = "Text Box 1" + str(list1)
    list2_label["text"] = "Text Box 2: " + str(list2)

def dosomthing2():
    random_number1 = random.randint(0, (len(list1)-1))
    random_number2 = random.randint(0, (len(list2)-1))
    text1 = list1[random_number1]
    text2 = list2[random_number2]
    random_list1_label["text"] = "Random 1: " + str(text1)
    random_list2_label["text"] = "Random 2: " + str(text2)

btn = Button(root, text="Ok", command=dosomthing)
btn1 = Button(root, text="Show Random", command=dosomthing2)
input1.pack()
input2.pack()
list1_label.pack()
list2_label.pack()
btn.pack()
random_list1_label.pack()
random_list2_label.pack()
btn1.pack()

root.mainloop()
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

root = Tk()
root.title("About planets")
root.geometry("500x500")
icon1 = PhotoImage(file="Logo.png")
root.iconphoto(False, icon1)
root.configure(background="sky blue")

label_planet = Label(root, bg="sky blue", font=("Comic Sans MS", 12, "bold"), text="Planet: ")
label_planet_name = Label(root, bg="sky blue", font=("Comic Sans MS", 12, "bold"), text="")
label_planet_gravity = Label(root, bg="sky blue", font=("Comic Sans MS", 12, "bold"), text="gravity: ")
label_planet_info = Label(root, bg="sky blue", font=("Comic Sans MS", 12, "bold"))


def showinfoplanets():
    print("Complete this function.")


btn = Button(root, text="Show planet info", command=showinfoplanets, bd=0, bg="light green", font=("Comic Sans MS", 12, "bold"))

label_planet.place(relx=0.2, rely=0.1, anchor=CENTER)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)
label_planet_name.place(relx=0.5, rely=0.25, anchor=CENTER)
label_planet_gravity.place(relx=0.5, rely=0.8, anchor=CENTER)
label_planet_info.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()

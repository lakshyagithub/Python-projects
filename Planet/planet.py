from tkinter import *

root = Tk()
root.title("About planets")
root.geometry("500x500")
icon1 = PhotoImage(file="Logo.png")
root.iconphoto(False, icon1)
root.configure(background="sky blue")

label_planet = Label(root, bg="sky blue", font="Comic San MS", text="Planet: ")
label_planet_name = Label(root, bg="sky blue", font="Comic San MS", text="")
label_planet_gravity = Label(root, bg="sky blue", font="Comic San MS", text="gravity: ")
label_planet_info = Label(root, bg="sky blue", font="Comic San MS")

def showinfoplanets():
    print("Complete this function.")
    
label_planet.pack()
label_planet_name.pack()
label_planet_gravity.pack()
label_planet_info.pack()

root.mainloop()
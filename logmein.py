from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("log me in")

#User name
label_user = Label(root, text="Username:")
label_user.place(relx=0.3, rely=0.1, anchor=CENTER)
username_textbox = Entry(root)
username_textbox.place(relx=0.5, rely=0.1, anchor=CENTER)

label_password = Label(root, text="Password: ")

root.mainloop()

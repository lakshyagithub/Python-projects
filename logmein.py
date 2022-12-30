from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("log me in")

#Username
label_user = Label(root, text="Username:")
label_user.place(relx=0.2, rely=0.1, anchor=CENTER)
username_textbox = Entry(root)
username_textbox.place(relx=0.5, rely=0.1, anchor=CENTER)

#Password
label_password = Label(root, text="Password:")
label_password.place(relx=0.2, rely=0.2, anchor=CENTER)
password_textbox = Entry(root)
password_textbox.place(relx=0.5, rely=0.2, anchor=CENTER)

#Captcha
label_captcha = Label(root, text="Captcha:")
label_captcha.place(relx=0.2, rely=0.3, anchor=CENTER)
captcha_textbox = Entry(root)
captcha_textbox.place(relx=0.5, rely=0.3, anchor=CENTER)

#Main code

#Buttons - Update_login_details
username_textbox = Button()
username_textbox.place(relx=0.5, rely=0.1, anchor=CENTER)

root.mainloop()

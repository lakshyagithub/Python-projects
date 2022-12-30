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

#Private elements
name_private = Label(root, text="Name: ")
name_private.place(relx=0.2, rely=0.6, anchor=CENTER)
password_private = Label(root, text="Password: ")
password_private.place(relx=0.2, rely=0.7, anchor=CENTER)
captcha_private = Label(root, text="Captcha: ")
captcha_private.place(relx=0.2, rely=0.8, anchor=CENTER)

#Main code

#Buttons - Update_login_details
update_login_details = Button(root, text="Update login details")
update_login_details.place(relx=0.2, rely=0.5, anchor=CENTER)

#Buttons - Show_profile
show_profile = Button(root, text="Show profile")
show_profile.place(relx=0.8, rely=0.5, anchor=CENTER)

root.mainloop()

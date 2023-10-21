from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image as PIL
import os
import hashlib

root = Tk()
root.geometry("600x400")
root.title("Image Hasher")
root.config(background="sky blue")

filename = "your_image.jpg" 
label_image = Label(root)
label_image.place(relx=0.5, rely=0.2, anchor=CENTER)
label_hash = Label(root)
label_hash.place(relx=0.5, rely=0.8, anchor=CENTER)

def open_files():
    global filename
    filename_raw = filedialog.askopenfilename(title="Open a file", filetypes=[("Photos", "*.png")])
    print(filename_raw)
    filename = os.path.basename(filename_raw)
    image = PIL.Image.open(rf"{filename_raw}")
    img = ImageTk.PhotoImage(image)
    l = Label(image=img)
    l.pack()
    label_image["image"]=img2

    try:
        with open(filename, 'rb') as f:
            file_data = f.read()
        sha256_hash = hashlib.sha256(file_data)
    
        image_hash = sha256_hash.hexdigest()
    
        print("SHA-256 Hash of the image:", image_hash)
        label_hash["text"] = "SHA-256 Hash:", image_hash
    
    except FileNotFoundError:
        print("Image file not found. Make sure the file is in the specified folder.")
    except Exception as e:
        print("An error occurred:", e)

open_file_button = Button(root, text="Open png file", command=open_files, bg="light green", fg="white", bd=0)
open_file_button.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
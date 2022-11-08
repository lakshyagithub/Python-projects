from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Canvas")
root.geometry("900x600")

canvas1 = Canvas(root, width=880, height=520, bg="white", highlightbackground="lightgray")
canvas1.pack()

choose_color_label = Label(root, text="Choose color")
startx_label = Label(root, text="startx")
starty_label = Label(root, text="starty")
endx_label = Label(root, text="endx")
endy_label = Label(root, text="endy")

choose_color_label.place(relx=0.1, rely=0.9, anchor=CENTER)

d1 = ttk.Combobox(root, state="readonly", values=values1, width=10)
values1 = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900]

d2 = ttk.Combobox(root, state="readonly", values=values2, width=10)
values2 = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900]

d3 = ttk.Combobox(root, state="readonly", values=values3, width=10)
values3 = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900]

d4 = ttk.Combobox(root, state="readonly", values=values4, width=10)
values4 = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900]

root.mainloop()
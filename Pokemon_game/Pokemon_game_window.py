from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Pokemon game")
root.geometry("600x400")
root.configure(background="sky blue")

#Labels
player1 = Label(root, text="Player 1")
player2 = Label(root, text="Player 2")
player1_score = Label(root)
player2_score = Label(root)
score_of_player = Label(root, bg="Orangered", fg="white")

#Placing
player1.place(relx=0.2, rely=0.3, anchor=CENTER)
player2.place(relx=0.8, rely=0.3, anchor=CENTER)
player1_score.place(relx=0.2, rely=0.4, anchor=CENTER)
player2_score.place(relx=0.8, rely=0.4, anchor=CENTER)
score_of_player.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
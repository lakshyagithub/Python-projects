#Librarys
from tkinter import *
from PIL import Image, ImageTk

#Make the window
root = Tk()
root.title("Pokemon game")
root.geometry("600x400")
root.configure(background="sky blue")

#Images
abra = ImageTk.PhotoImage(Image.open ("abra.jpg"))
bulbasour = ImageTk.PhotoImage(Image.open ("bulbasour.jpg"))
button = ImageTk.PhotoImage(Image.open ("button.jpg"))
pikachu = ImageTk.PhotoImage(Image.open ("pikachu.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
Iyvasour = ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
charmender = ImageTk.PhotoImage(Image.open("charmender.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
meowth = ImageTk.PhotoImage(Image.open("meowth.jpg"))
persion = ImageTk.PhotoImage(Image.open ("persion.jpg"))
ratata = ImageTk.PhotoImage(Image.open("ratata.jpg"))
squirtle = ImageTk.PhotoImage(Image.open("squirtle.jpg"))
nidoking = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
paras = ImageTk.PhotoImage(Image.open ("paras.jpg"))

#Powers and cards
pokemon_list = ["Pikachu", "Bulbasor", "jigglypuff", "Iyvasour", "charmender", "kadabra", "meowth", "persion", "ratata", "squirtle", "nidoking", "paras"]
Power_pokemon = [200, 60, 70, 100, 50, 70, 60, 70, 40, 50, 90, 40]

#Other
player1_score_data = 0
def player1_s_function():
	global player1_score_data
	random_number_player1 = random.randint(0, 13)
	pokemon_list[random_number_player1]

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
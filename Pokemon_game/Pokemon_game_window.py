#Librarys
import random
from tkinter import *

from PIL import Image, ImageTk

#Make the window
root = Tk()
root.title("Pokemon game")
root.geometry("600x400")
root.configure(background="sky blue")

#Images
abra = ImageTk.PhotoImage(Image.open("images/abra.jpg"))
bulbasour = ImageTk.PhotoImage(Image.open("images/bulbasour.jpg"))
button = ImageTk.PhotoImage(Image.open("images/button.jpg"))
pikachu = ImageTk.PhotoImage(Image.open("images/pikachu.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open("images/jigglypuff.jpg"))
Iyvasour = ImageTk.PhotoImage(Image.open("images/Iyvasour.jpg"))
charmender = ImageTk.PhotoImage(Image.open("images/charmender.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("images/kadabra.jpg"))
meowth = ImageTk.PhotoImage(Image.open("images/meowth.jpg"))
persion = ImageTk.PhotoImage(Image.open ("images/persion.jpg"))
ratata = ImageTk.PhotoImage(Image.open("images/ratata.jpg"))
squirtle = ImageTk.PhotoImage(Image.open("images/squirtle.jpg"))
nidoking = ImageTk.PhotoImage(Image.open("images/nidoking.jpg"))
paras = ImageTk.PhotoImage(Image.open ("images/paras.jpg"))

#Powers and cards
pokemon_list = ["pikachu", "bulbasor", "jigglypuff", "Iyvasour", "charmender", "kadabra", "meowth", "persion", "ratata", "squirtle", "nidoking", "paras"]
Power_pokemon = [200, 60, 70, 100, 50, 70, 60, 70, 40, 50, 90, 40]

#Other
player1_score_data = 0
def player1_s_function():
	global player1_score_data
	random_number_player1 = random.randint(0, 13)
	random_pokemon = pokemon_list[random_number_player1]
	score_of_player["image"] = random_pokemon
	random_power_list = Power_pokemon[random_number_player1]
	player1_score_data = player1_score_data + random_power_list
	player1_score["text"] = player1_score_data

player2_score_data = 0
def player2_s_function():
	global player2_score_data
	random_number_player2 = random.randint(0, 13)
	random_pokemon = pokemon_list[random_number_player2]
	score_of_player["image"] = random_pokemon
	random_power_list = Power_pokemon[random_number_player2]
	player2_score_data = player2_score_data + random_power_list
	player2_score["text"] = player2_score_data

#Labels
player1 = Label(root, text="Player 1")
player2 = Label(root, text="Player 2")
player1_score = Label(root)
player2_score = Label(root)
score_of_player = Label(root)

#Buttons
btn1 = Button(root, image=button, command=player1_s_function, bd=0)
btn2 = Button(root, image=button, command=player2_s_function, bd=0)

#Placing
player1.place(relx=0.2, rely=0.3, anchor=CENTER)
player2.place(relx=0.8, rely=0.3, anchor=CENTER)
player1_score.place(relx=0.2, rely=0.4, anchor=CENTER)
btn1.place(relx=0.2, rely=0.6, anchor=CENTER)
player2_score.place(relx=0.8, rely=0.4, anchor=CENTER)
btn2.place(relx=0.8, rely=0.6, anchor=CENTER)
score_of_player.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()

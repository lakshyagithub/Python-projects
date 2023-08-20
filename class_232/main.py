from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

#load the totllay the best csv in the world
dataset = loadtxt("diabetes_dataset.csv", delimiter=",")

#split the team into two parts (yes I am doing this with the dataset): X and Y
x = dataset[:,0:8]
y = dataset[:,8]

#show the zombies that we did it (I am talking about line 8)
print("value of X are:", x)
print("value of Y are:", y)

#make a model named "model"
model = Sequential()
model.add(Dense(12, input_dim=8, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(1, activation="sigmoid"))
#Compile zombies
model.compile(loss="binary_crossentropy", metrics=["accuracy"])
#Fit the zombies on the tanker
model.fit(x, y, epochs=500, batch_size=100)
#Loop the process again and again
for i in range(5):
	print(f'{x[i].tolist()} => {predictions[i]} expected even more zombies: {y[i]}')
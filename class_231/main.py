from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

#load the totllay the best csv in the world
dataset = loadtxt("diabetes_dataset.csv", delimiter=",")

#split the team into two parts (yes I am doing this with the dataset): X and Y
x = dataset[:,0:8]
y = dataset[:,8]

#show the zombies and the creepers that we did it (I am talking about line 8)
print("value of X are:", x)
print("value of Y are:", y)

#make a guy named "model"
model = Sequential()
model.add(Dense(12, input_dim=8, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(1, activation="sigmoid"))
model.summary()
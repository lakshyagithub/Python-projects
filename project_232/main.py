from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

dataset = pd.read_csv("pokemon.csv", delimiter=",")
x = dataset.iloc[:, 1:7]
y = dataset.iloc[:, 8]

model = Sequential()
model.add(Dense(12, input_dim=8, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(1, activation="sigmoid"))
model.compile(loss="binary_crossentropy", metrics=["accuracy"])
model.fit(x, y, epochs=500, batch_size=100)
for i in range(785,800):
	print(f'{x[i].tolist()} => {predictions[i]} expected: {y[i]}')
import pandas as pd
import pickle
from keras.models import model_from_json
from sklearn.neural_network import MLPClassifier

dataset = pd.read_csv('THE_CSV.csv')

x = dataset.iloc[:, [2, 4]].values # input
  
y = dataset.iloc[:, 5].values # output

#CNN model
model = MLPClassifier(hidden_layer_sizes= (20), 
						random_state=5, 
						activation='relu', 
						batch_size=200, 
						learning_rate_init=0.03) 
model.fit(x, y)

#prediction
predictions = model.predict(x)

file = open("THE_CSV.pkl", "wb")
pickle.dump(model, file)

saved_the_day_file = open("THE_CSV.pkl", "rb")
saved_the_day = pickle.load(saved_the_day_file)

car_data = {
	'throttle': [0.34],
	'distance': [60.79483795]
}

data = pd.DataFrame(car_data, columns=["throttle", "distance"])
prediction_data = saved_the_day.predict(data)
print("The answer is simply :", prediction_data)
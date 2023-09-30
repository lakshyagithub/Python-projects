import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

# Read the CSV file and store it in the "dataset" variable
dataset = pd.read_csv("projectC234_EPL.csv")

# Collect the data of column 'club' and count the values
Football_club = dataset['Club'].value_counts().head(20)

# Print the data of the top 20 clubs with maximum penalty accuracy
print(Football_club)

# Create a PIE chart using plotly.graph_objects
club_fig = go.Figure(data=[go.Pie(labels=Football_club.index, values=Football_club.values, hole=0.5)])

# Show the PIE chart
club_fig.show()

import pandas as pd

dataset = pd.read_csv('premier_league_goals.csv')

goal_column = dataset['Goals']

sorted_club_data_by_ascending_order = goal_column.groupby(dataset['Club'])

sum_of_goal_by_each_club = sorted_club_data_by_ascending_order.sum()

sorted_goal_values = sum_of_goal_by_each_club.sort_values(ascending=False)

print("Task 1: Premier League Goals of Each Club")
print(sorted_goal_values)

epl_top_goals = dataset.sort_values(by='Goals', ascending=False)[:10]

print("\nTask 2: Top Goal Scorers in the Premier League")
print(epl_top_goals)
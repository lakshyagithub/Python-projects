import pandas as pd

# Task 01: Calculate Total Marks
df = pd.read_csv('student_data.csv')
subject_columns = df.iloc[:, [2, 3, 4]]
total_marks = subject_columns.sum(axis=1)
df['Total_marks_obtained'] = total_marks

# Save the updated DataFrame to a new CSV file
df.to_csv('new_student_data.csv', index=False)

# Task 02: Assign Grades
df.loc[df['Total_marks_obtained'] > 250, 'Grade'] = 'A'
df.loc[df['Total_marks_obtained'] <= 250, 'Grade'] = 'B'

# Task 03: Calculate Percentage
df['Percentage'] = (df['Total_marks_obtained'] / df['Overall_Total']) * 100

# Save the updated DataFrame with grades and percentage
df.to_csv('new_new_data.csv', index=False)

# Print the DataFrame to see the overall student report
print(df)

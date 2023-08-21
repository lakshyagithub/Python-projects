import pandas as pd

df = pd.read_csv("student_promoted.csv")

df.loc[df["Attendence"] > 75, "student_promoted"] = "Promoted"
df.loc[df["Attendence"] < 75, "student_promoted"] = "Not Promoted"

print(df)
import pandas as pd

df = pd.read_csv("radar_data.csv")

df.loc[df["distance"] <= 17, "action"] = "1"
df.loc[df["steer"] < 0, "action"] = "0"
df.loc[df["distance"] > 17, "action"] = "2"
df.to_csv("new_radar_data.csv", index=False)

print(df)
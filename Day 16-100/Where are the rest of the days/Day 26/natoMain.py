import pandas as pd

df = pd.read_csv("nato.csv")
nato_dict = dict(zip(df["letter"], df["word"]))

name = "daniel"

nato_list = [nato_dict[letter.upper()] for letter in name]
print(nato_list)

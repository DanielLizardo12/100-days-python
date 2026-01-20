import pandas as pd

df = pd.read_csv("nato.csv")
nato_dict = dict(zip(df["letter"], df["word"]))

name = "asd"

try:
    nato_list = [nato_dict[letter.upper()] for letter in name]
    print(nato_list)
except KeyError:
    print("sorry only letters from the alphabet")


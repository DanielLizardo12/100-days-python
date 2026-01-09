import pandas as pd

data = pd.read_csv("squirrel_count.csv")
gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel, red_squirrel, black_squirrel],
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_color_count.csv")
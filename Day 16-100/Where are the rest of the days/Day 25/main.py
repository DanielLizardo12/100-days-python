import pandas

data = pandas.read_csv('weather_data.csv')
print(type(data))
print(data["temp"].mean())
print(data["temp"].max())
print(data.temp.max())

print(data[data.temp == data.temp.max()].condition)
print((data[data.day == "Monday"].temp * 9 / 5) + 32)

data_dict = {
    "students": ["amy", "dan", "david"],
    "scores": [70, 100, 90],
}

data = pandas.DataFrame(data_dict)
data.to_csv("students.csv")
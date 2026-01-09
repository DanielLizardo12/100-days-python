import csv
import pandas

with open('weather_data.csv') as f:
    reader = csv.reader(f)
    next(reader)
    temperatures = []
    for row in reader:
        temperatures.append(int(row[1]))
    #print(temperatures)


data = pandas.read_csv('weather_data.csv')
print(data["temp"])
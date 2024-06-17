import csv

with open('weather_data.csv') as f:
    data = csv.reader(f)
    temperatures = []
    for row in data:
        if not row[1] == 'temp':
            temperatures.append(int(row[1]))
print(temperatures)

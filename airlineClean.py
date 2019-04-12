import pandas as pd
import random

df = pd.read_csv("parsed_results/flight_dataset.csv")

df = df[df.airline != "Multiple Airlines"]

df = df[df.stops != 2]

airlineSet = {'Delta'}
airportSet = {'CHS'}

i = 1

for index, row in df.iterrows():
    airlineSet.add(row['airline'])
    airportSet.add(row['destination'])
    airportSet.add(row['layover'])
    print(i)
    i = i + 1

print(airlineSet)
print(airportSet)

airportDict = {value : round(random.random() * 100) for value in airportSet}
airlineDict = {value : round(random.random() * 100) for value in airlineSet}
print(airportDict)
print(airlineDict)
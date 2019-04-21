import pandas as pd  
from sklearn.neighbors import KNeighborsRegressor

dataset = pd.read_csv("parsedResults/flightDatasetNew.csv")

airlineMap = {'American Airlines' : 66}
airportMap = {32.885193 : 'CHS'}

for index, row in dataset.iloc[1:].iterrows():
	airlineMap[row['airline']] = row['airlineCode']
	airportMap[row['departureLat']] = row['departure']
	airportMap[row['destinationLat']] = row['destination']
	airportMap[row['layoverLat']] = row['layover']

print(list(airlineMap.keys()))
print('Which airline would you like to fly from CLT to LGA? (Match the case)')
firstAirline = input('-->')
print('Which airline would you like to fly from SEA to ATL? (Match the case)')
secondAirline = input('-->')
print('Which airline would you like to fly from EWR to SFO? (Match the case)')
thirdAirline = input('-->')


data = dataset.iloc[:, [4, 5, 7, 8, 15]]
target = dataset.iloc[:,10:12].values

predictX = [
						[35.220448, -80.94377, 40.77289, -73.868805, airlineMap[firstAirline]],
						[47.44359, -122.302505, 33.640545, -84.43341, airlineMap[secondAirline]],
						[40.69297, -74.17799, 37.616714, -122.38709, airlineMap[thirdAirline]],
						]


knn = KNeighborsRegressor(n_neighbors = 1)
knn.fit(data, target)


predictionResults = knn.predict(predictX)

print("Clustering with 1 cluster\n", predictionResults)

print("Flying from CLT to LGA on", firstAirline, "would likely result in a layover in",airportMap[predictionResults[0][0]])
print("Flying from SEA to ATL on", secondAirline, "would likely result in a layover in",airportMap[predictionResults[1][0]])
print("Flying from EWR to SFO on", secondAirline, "would likely result in a layover in",airportMap[predictionResults[2][0]])


import pandas as pd  
from sklearn.neighbors import KNeighborsRegressor

dataset = pd.read_csv("parsedResults/flightDatasetNew.csv")

# Creating map to link the characteristics back
airlineMap = {'American Airlines' : 66}
airportMap = {32.885193 : 'CHS'}

# Adding all values to the map
for index, row in dataset.iloc[1:].iterrows():
	airlineMap[row['airline']] = row['airlineCode']
	airportMap[row['departureLat']] = row['departure']
	airportMap[row['destinationLat']] = row['destination']
	airportMap[row['layoverLat']] = row['layover']

# Giving the user the option to choose what airline to fly on each pre-determined route
print(list(airlineMap.keys()))
print('Which airline would you like to fly from CLT to LGA? (Match the case)')
firstAirline = input('-->')
print('Which airline would you like to fly from SEA to ATL? (Match the case)')
secondAirline = input('-->')
print('Which airline would you like to fly from EWR to SFO? (Match the case)')
thirdAirline = input('-->')

# Setting up data and target values
data = dataset.iloc[:, [4, 5, 7, 8, 15]]
target = dataset.iloc[:,10:12].values

# Unique test cases
predictX = [
						[35.220448, -80.94377, 40.77289, -73.868805, airlineMap[firstAirline]],
						[47.44359, -122.302505, 33.640545, -84.43341, airlineMap[secondAirline]],
						[40.69297, -74.17799, 37.616714, -122.38709, airlineMap[thirdAirline]],
						]

# Here we are using a KNN Regression to deal with the multitarget output
# If there was not a multitarget output, a normal KNN Classifier would have worked fine
# Using 1 cluster to guarantee that the resulting layover shows an actual airport location
knn = KNeighborsRegressor(n_neighbors = 1)
knn.fit(data, target)


predictionResults = knn.predict(predictX)

# Demonstration of the results
for i in range(3):
	
	if airportMap[predictionResults[i][0]] == 'ZZZ' || :
		airportMap[predictionResults[i][0]] = 'no airport!'

print("Flying from CLT to LGA on", firstAirline, "would likely result in a layover in",airportMap[predictionResults[0][0]])
print("Flying from SEA to ATL on", secondAirline, "would likely result in a layover in",airportMap[predictionResults[1][0]])
print("Flying from EWR to SFO on", secondAirline, "would likely result in a layover in",airportMap[predictionResults[2][0]])
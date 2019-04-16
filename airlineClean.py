import pandas as pd
import numpy as np
import random
import os
from sklearn.neighbors import KNeighborsClassifier

if not os.path.exists("cleanedHtml"):
	os.mkdir("cleanedHtml")

	df = pd.read_csv("parsedResults/flightDataset.csv")

	df2 = pd.DataFrame()

	airlineSet = {'Delta'}
	airportSet = {'CHS'}

	for index, row in df.iloc[1:].iterrows():
	  airlineSet.add(row['airline'])
	  airportSet.add(row['destination'])
	  airportSet.add(row['layover'])

	airportDict = {value : round(random.random() * 100) for value in airportSet}
	airlineDict = {value : round(random.random() * 100) for value in airlineSet}

	for i in range (len(df.index)):
		df2 = df2.append({
									'airlineCode' : airlineDict[df.loc[i,'airline']],
									'departureCode' : airportDict[df.loc[i,'departure']],
									'destinationCode' : airportDict[df.loc[i,'destination']],
									'layoverCode' : airportDict[df.loc[i,'layover']]

									}, ignore_index = True)

	df.join(df2, how = 'outer').to_csv("cleanedHtml/cleanFlightDataset.csv")


learningDF = pd.read_csv("cleanedHtml/cleanFlightDataset.csv")

data = learningDF.iloc[:,12:13]

target = learningDF.iloc[:,9].values

for i in range (1, 15):
	knn = KNeighborsClassifier(n_neighbors = i)
	knn.fit(data, target)
	testData = [
							[25]]
	predictionResults = knn.predict(testData)

	print("KNN metric for", i, "clusters:", predictionResults)

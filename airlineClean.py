import pandas as pd
import numpy as np
import random
import os
from sklearn.neighbors import KNeighborsClassifier

if not os.path.exists("cleanedHtml"):
	os.mkdir("cleanedHtml")

	df = pd.read_csv("parsedResults/flightDatasetNew.csv")

	df2 = pd.DataFrame()

	airlineSet = {'Delta'}
	airportSet = {'CHS'}

	for index, row in df.iloc[1:].iterrows():
	  airlineSet.add(row['airline'])

	airlineDict = {value : round(random.random() * 100) for value in airlineSet}

	for i in range (len(df.index)):
		df2 = df2.append({
									'airlineCode' : airlineDict[df.loc[i,'airline']],
									}, ignore_index = True)

	df.join(df2, how = 'outer').to_csv("parsedResults/flightDatasetNew.csv")


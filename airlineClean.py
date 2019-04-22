import pandas as pd
import numpy as np
import random
import os
from sklearn.neighbors import KNeighborsClassifier

# Setting up a clean directory for the data
if not os.path.exists("cleanedHtml"):
	os.mkdir("cleanedHtml")

	df = pd.read_csv("parsedResults/flightDatasetNew.csv")
	df2 = pd.DataFrame()

	# Creating a set to hold each airline which will later turn into a dictionary
	airlineSet = {'Delta'}

	# Now this is just going to itterate through the data frame adding all the airlines to the set
	for index, row in df.iloc[1:].iterrows():
	  airlineSet.add(row['airline'])

	# Transforming the set into a dictionary.  The value for each key is arbitrary and just used as an identifier
	airlineDict = {value : round(random.random() * 100) for value in airlineSet}

	# Now we just need to add the key-value pair to a data frame and combine it with the first.
	for i in range (len(df.index)):
		df2 = df2.append({
									'airlineCode' : airlineDict[df.loc[i,'airline']],
									}, ignore_index = True)

	df.join(df2, how = 'outer').to_csv("parsedResults/flightDatasetNew.csv")

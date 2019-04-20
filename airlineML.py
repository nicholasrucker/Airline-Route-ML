import pandas as pd  
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsRegressor

dataset = pd.read_csv("parsedResults/flightDatasetNew.csv")

data = dataset.iloc[:, [4, 5, 7, 8, 15]]
target = dataset.iloc[:,10:12].values

#dataTrain, dataTest, targetTrain, targetTest = train_test_split(data, target, test_size = .2)
#decisionTreeMachine = tree.DecisionTreeClassifier(criterion="gini")
#decisionTreeMachine.fit(dataTrain, targetTrain)

#predictions = decisionTreeMachine.predict(dataTest)

#print(accuracy_score(targetTest, predictions))

#print(confusion_matrix(targetTest, predictions))


reg1 = DecisionTreeRegressor(max_depth=3)

reg1.fit(data, target)

predictX = [
						[35.220448, -80.94377, 40.77289, -73.868805, 66],
						[40.69297, -74.17799, 32.885193, -80.03694, 91],
						]




y1 = reg1.predict(predictX)

print("Decision tree regressor\n", y1)

for i in range (1, 10):

	knn = KNeighborsRegressor(n_neighbors = i)
	knn.fit(data, target)
	predictionResults = knn.predict(predictX)

	print("Clustering with", i, "clusters\n", predictionResults)


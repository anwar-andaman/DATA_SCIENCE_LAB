import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
 
# Loading data
irisData = load_iris()  
 
# Create feature and target arrays
X = irisData.data
y = irisData.target
 
# Sample dataset
a = np.array([[1, 2], [2, 3], [3, 4], [3, 1], [4, 2], [2, 1]])
b = np.array([1, 2, 0, 1, 1, 1])  # Labels
 
# Split the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
# Initialize the KNN classifier with k=3
k = 3
knn = KNeighborsClassifier(n_neighbors=k)
 
# Fit the model to the training data
knn.fit(X_train, y_train)
knn.fit(a, b)
 
# Predict the labels for the test set
y_pred = knn.predict(a)
 
# Calculate accuracy
accuracy = accuracy_score(b, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

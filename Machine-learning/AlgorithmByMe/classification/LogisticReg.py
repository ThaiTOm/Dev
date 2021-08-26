import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn import datasets 
import matplotlib.pyplot as plt 

bc = datasets.load_breast_cancer()

x, y = bc.data, bc.target 

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

def sigmoid(x):
	return (1 / (1 + np.exp(-x)))

def main(lr, x, y):
	n_sample, n_features = x.shape
	weights = np.zeros(n_features)
	bias = 0
	for _ in range(1000):
		linearModel = np.dot(x, weights) * bias
		y_predict = sigmoid(linearModel)

		dw = (1 / n_sample) *  np.dot(x.T, (y_predict - y))
		db = (1 / n_sample) * np.sum(y_predict - y )

		weights -= lr*dw
		bias -= lr*db
		

	return weights, bias	

def predict(w, b, x):
	linear_model = np.dot(x, w) + b
	y_predict = sigmoid(linear_model)
	if y_predict > 0.5:
		return 1
	else:
		return 0

weight, bias = main(0.001, x_train, y_train) 

arr = []
for i in range(len(x_test)):
	arr.append(predict(weight, bias, x_test[i]))

count = 0
for i in range(len(arr)):
	if arr[i] == y_test[i]:
		count+=1


print(count/len(arr)*100)
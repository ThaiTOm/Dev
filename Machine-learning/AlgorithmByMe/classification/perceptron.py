import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from scipy.spatial.distance import cdist
np.random.seed(2)

means = [[2, 2], [4, 2]]
cov = [[.3, .2], [.2, .3]]
N = 10
X0 = np.random.multivariate_normal(means[0], cov, N).T
X1 = np.random.multivariate_normal(means[1], cov, N).T

X = np.concatenate((X0, X1), axis = 1)
y = np.concatenate((np.ones((1, N)), -1*np.ones((1, N))), axis = 1)
x_train, x_test, y_train, y_test = train_test_split(X[0], X[1], test_size = 0.2)

plt.scatter(X[0], X[1])
plt.show()

def activation_func(x):
  return np.where(x >= 0, 1, 0)

def fit(x, y, lr):
  n_samples, n_feartures = x.shape
  weights = np.zeros(n_feartures)
  bias = 0
  y_ = np.array([1 if i > 0 else 0 for i in y[0]])
  for _ in range(1000):
    for ind, x_i in enumerate(x):
      linear_output = np.dot(x_i, weights) + bias
      y_predicted = activation_func(linear_output)
      update = lr * (y_[ind] - y_predicted)
      weights += update + x_i
      bias += update
  return weights, bias

w, b = fit(X, y, 0.001)
print(w, b)
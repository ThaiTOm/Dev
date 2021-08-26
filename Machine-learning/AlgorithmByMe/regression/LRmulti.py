import numpy as np

x_data = np.array([[1, 2104, 5, 1, 45], [1, 1416, 3, 2, 40], [1, 1534, 3, 2, 30], [1, 852, 2, 1, 36]])
y_data = np.array([460, 232, 315, 178])

theta = np.dot(1/((np.dot(np.transpose(x_data), x_data))), np.dot(np.transpose(x_data), y_data))
print(theta)
import numpy as np
import matplotlib.pyplot as plt

class_x_1 = np.array([0.72, 0.91, 0.03, 0.12, 0.96, 0.8, 0.46, 0.66, 0.72, 0.35])
class_y_1 = np.array([0.82, -0.69, 0.93, 0.25, 0.47, -0.75, 0.98, 0.24, -0.15, 0.01])

class_x_2 = np.array([-0.11, -0.31, 0, -0.43, 0.57, -0.72, -0.25, -0.12, -0.58, -0.77])
class_y_2 = np.array([0.1, -0.96, -0.26, -0.65, -0.97, -0.64, -0.43, -0.9, 0.02, -0.76])

plt.scatter(class_x_1, class_y_1, c="b")
plt.scatter(class_x_2, class_y_2, c="r")

# plt.show()

w = np.zeros(10)


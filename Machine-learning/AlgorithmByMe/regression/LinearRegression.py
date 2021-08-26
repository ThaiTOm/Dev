import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# [(183,68), (180, 67)]


def predicFunction():
    return


df = pd.DataFrame({
    "x": [1, 2, 2, 3, 3, 4, 5, 6, 6, 6, 8, 10],
    "y": [-890, -1411, -1560, -2220, -2091, -2878, -3557, -3268, -3920, -4163, -5471, -5157]
})

x_data = df["x"].to_numpy()
y_train = df["y"].to_numpy()

x_train = []


for i in range(len(x_data)):
    x_train.append([x_data[i], 1])

a = np.linalg.pinv(np.array(x_train))

b = np.array(y_train)

equation = np.dot(a, b)

reg = LinearRegression().fit(x_train, y_train)

print("Toi du doan", equation)
print("Ban du doan", reg.coef_, reg.intercept_)

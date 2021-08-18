import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from collections import Counter


df = pd.DataFrame({
    "x": [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72],
    "y": [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
})

k = 3


def predicFunction(req, k, data):
    # find distance
    x_train, y_train = data["x"].to_numpy(), data["y"].to_numpy()
    distance = [np.sqrt(np.sum((req - i)**2)) for i in x_train]
    # get index
    k_idx = np.argsort(distance)[:k]
    k_nearestLabels = [y_train[i] for i in k_idx]

    most_common = Counter(k_nearestLabels).most_common(1)
    return most_common[0][0]


predict = predicFunction(df.iloc[17]["x"], 3, df)


x = df["x"].tolist()
y = df["y"].tolist()


plt.scatter(x, y, c="b")
plt.show()

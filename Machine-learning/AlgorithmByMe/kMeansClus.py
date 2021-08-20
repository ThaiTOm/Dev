from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np


features, true_labels = make_blobs(
    n_samples=200,
    centers=3,
    cluster_std=2.75,
    random_state=42
)

# define var

x_data = np.array([i[0] for i in features])
y_data = np.array([i[1] for i in features])

colorMap = {
    0: "b",
    1: "r",
    2: "y"
}

l1, l2, l3 = [], [], []
label = [l1, l2, l3]

centroids = {
    i+1: [np.random.randint(-10, 15), np.random.randint(-10, 15)]
    for i in range(3)
}

plt.scatter(x_data, y_data)


def euclidean_distance(ratio1, ratio2):
    return np.sqrt((ratio2[0] - ratio2[0])**2 + (ratio2[1] - ratio1[1])**2)


def reCentroids(label, centroids):
    for i in centroids.keys():
        x_data = [label[i-1][x][0] for x in range(len(label[i-1]))]
        y_data = [label[i-1][x][1] for x in range(len(label[i-1]))]
        centroids[i] = [sum(x_data) / max(len(x_data), 1),
                        sum(y_data) / max(len(y_data), 1)]


def main(centroids):
    for i in range(200):
        mn = 999999999999
        val = None
        for x in range(1, 4):
            distance = euclidean_distance([x_data[i], y_data[i]], centroids[x])
            if distance < mn:
                val = x
                mn = distance
        label[val-1].append([x_data[i], y_data[i]])


def setColor(colorMap, label):
    for i in range(len(label)):
        for value in label[i]:
            plt.scatter(value[0], value[1], c=colorMap[i])


main(centroids)
reCentroids(label, centroids)
main(centroids)
setColor(colorMap, label)

plt.show()

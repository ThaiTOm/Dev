import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from scipy.sparse import coo_matrix # for sparse matrix
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.metrics import accuracy_score

# features have from 1 - 100, label 0 - 99

path = "Machine-learning/DataFolder/SpamEmail"
data_fn = "/train-features-100.txt"
label_fn = "/train-labels-100.txt"
test_data_fn = "/test-features.txt"
test_label_fn = "/test-labels.txt"


nwords = 2500

def read_data(data_fn, label_fn):
	with open(path + label_fn) as f:
		content = f.readlines()
	label = [int(x.strip()) for x in content]
	with open(path + data_fn) as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	dat = np.zeros((len(content), 3), dtype = int)
	for i, line in enumerate(content):
		a = line.split(' ')
		dat[i, :] = np.array([int(a[0]), int(a[1]), int(a[2])])
	data = coo_matrix((dat[:, 2], (dat[:, 0] - 1, dat[:, 1] - 1)), shape=(len(label), nwords))
	return (data, label)

(train_data, train_label) = read_data(data_fn, label_fn)
(test_data, test_label) = read_data(test_data_fn, test_label_fn)

clf = MultinomialNB()
clf.fit(train_data, train_label)


y_pred = clf.predict(test_data)
print("Training size = %d, accuracy = %.2f%%" % (train_data.shape[0],accuracy_score(test_label, y_pred)*100))

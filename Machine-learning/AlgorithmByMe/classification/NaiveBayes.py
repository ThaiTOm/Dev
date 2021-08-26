import numpy as np

# traning data 
# hanoi, pho, chaoLong, bunCha, omai, banhGio, saiGon, huTiu, banhBo
d1 = [2, 1, 1, 0, 0, 0, 0, 0, 0]
d2 = [1, 1, 0, 1, 1, 0, 0, 0, 0]
d3 = [0, 1, 0, 0, 1, 1, 0, 0, 0]
d4 = [0, 1, 0, 0, 0, 0, 1, 1, 1]

train_data = np.array([d1, d2, d3, d4])

label = np.array(['B', "B", "B", "N"]) 

# test data 
d5 = np.array([[1, 0, 0, 1, 0, 0, 0, 1, 0]])
d6 = np.array([[0, 1, 0, 0, 0, 0, 0, 1, 1]])

def splitPercent():
	Bac = []
	Nam = []
	totalBac = len(d1)
	totalNam = len(d1)
	for i in range(len(label)):
		if label[i] == "B":
			totalBac += sum(train_data[i])
		else:
			totalNam += sum(train_data[i])
	for i in range(len(d1)):
		value_A = sum([train_data[x][i] for x in range(3)])
		value_B = sum([train_data[x][i] for x in range(3,4)])
		Bac.append((value_A + 1) / totalBac)
		Nam.append((value_B + 1) / totalNam )
	return Bac, Nam		

B, N = splitPercent()

pA = 3 / len(label)
pB = 1 / len(label)

def predict(req, B, N):
	with_B = 1
	with_N = 1
	for i in range(len(req)):
		if req[i] != 0:
			with_N *= (req[i] * N[i])
			with_B *= (req[i] * B[i])

	if with_B > with_N:
		return "B"
	return "N"



pre = predict(d6[0], B, N)

print(pre)




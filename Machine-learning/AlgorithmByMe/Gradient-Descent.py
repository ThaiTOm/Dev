import math 
import pandas as pd

# [(183,68), (180, 67)]

df = pd.DataFrame({
	"x": [147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178], 
	"y": [49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66]
})


x_data = df["x"].to_numpy()
y_data = df["y"].to_numpy()

def derivative(x, y, step):
	return -2 * (y - (step + 0.55 * x))

def main(learning_rate, x, y):
	step = 0
	i = 0 
	arr =  [0]
	for t in range(1000):
		sm = 0 
		for i in range(len(x)):
			sm += derivative(x[i], y[i], step)
		if sm == arr[-1] or (abs(sm) < 1e-3):
			break
		else:
			step = step - (learning_rate*round(sm, 2))
			arr.append(sm)
	return t, step

print(main(0.001, x_data, y_data))
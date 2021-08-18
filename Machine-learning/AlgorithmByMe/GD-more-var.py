# STEP FOOT
# step 1: tinh dao ham cua tung bien
# vi du: y = inter + slope * x (2 an la inter va slope)
# => tinh dao ham cua inter va slope
# chon ngau nhien so cho cac an (randomly pickup number for vars) => In this case we pick
# inter = 0, slope = 1

# step 2: thay inter va slope vao ham ham cua tung cai 

# inter thay vao dao ham inter se duoc inter moi 
# slope thay vao dao ham slope se duoc slope moi 
import pandas as pd 

df = pd.DataFrame({
	"x": [147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178], 
	"y": [49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66]
})

x_data, y_data = df["x"].to_numpy(), df["y"].to_numpy()


def derivative(x, y, inter, slope):
	return ((-2*(y-(inter + slope * x))), (-2*x*(y-(inter + slope * x))))

def main(x, y, learning_rate):
	inter, slope, arr = -33, 0.5 , [0]
	for t in range(1000):
		totalInter = 0
		totalSlope = 0 
		for i in range(len(x)):
			a, b = derivative(x[i], y[i], inter, slope)
			totalInter += a
			totalSlope += b
		if abs(totalSlope) < 1e-3 and abs(totalInter) < 1e-3:
			
			break
		else:
			inter = round(inter - (learning_rate * totalInter), 4)
			slope = round(slope - (learning_rate * totalSlope), 4)
	return inter, slope, t


print(main(x_data, y_data, 0.000001))

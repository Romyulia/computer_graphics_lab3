import math
import numpy as np
import matplotlib.pyplot as plt

angle = math.radians(10)
data = np.loadtxt('DS0.txt', dtype = np.int32)
dataX = []
dataY = []
for i in range(len(data)):
    x = data[i][0] - 480
    y = data[i][1] - 480
    rotatedX = 480 + x * math.cos(angle) - y * math.sin(angle)
    rotatedY = 480 + x * math.sin(angle) + y * math.cos(angle)
    dataX.append(rotatedX)
    dataY.append(rotatedY)

plt.figure(figsize=(9.6, 9.6))
plt.scatter(dataY, dataX, color = 'blue')
plt.savefig("output.jpg")
plt.show()
import numpy as np
import matplotlib.pyplot as plt
datapoints = 100
x = np.array([1,2,3,4,5,6])
y = np.array([10,100,1000,10000,100000,1000000])
y = np.log10(y)
plt.plot(x,y)
plt.xlabel("Pressure/Pa")
plt.ylabel("Volume/m$^3$")
plt.axis([0,7,0,7])
plt.show()

import numpy as np
import matplotlib.pyplot as plt
x=np.array([5,10,15,20,25])
y=np.array([0.2,0.5,0.8,1.0,1.3])
yerror = np.array([0.05,0.05,0.05,0.05,0.05])
#the next line is the model prediction,
#where we make some initial guess
#what the slope of the line will be
fx=0.05*x
plt.errorbar(x,y,yerror,fmt='bo')
plt.plot(x,fx,'r-')
plt.show()

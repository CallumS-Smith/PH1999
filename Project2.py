import numpy as np
import matplotlib.pyplot as plt
x=np.array([5,10,15,20,25])
y=np.array([0.2,0.5,0.8,1.0,1.3])
yerror = np.array([0.05,0.05,0.05,0.05,0.05])
#the next line is the model prediction,
#where we make some initial guess
#what the slope of the line will be
total = 0
for i in range(0,len(x)):
    total += (y[i]-0.05*x[i])**2/(yerror[i])**2
print(total)

minchi2=10000
minslope=0.0
for slope in np.arange(0, 1, 0.0001):
    total = 0
    for i in range(0,len(x)):
        total += (y[i]-slope*x[i])**2/(yerror[i])**2
    if(total<minchi2):
        minchi2=total
        minslope=slope
        
print(minslope)
fx=0.05*x
plt.errorbar(x,y,yerror,fmt='bo')
plt.plot(x,fx,'r-')
plt.plot(x,minslope*x,'g-')
plt.show()

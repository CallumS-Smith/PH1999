import numpy as np
import matplotlib.pyplot as plt

##################importing data##################
file = open("galaxy1.txt","r")
rawData = file.readlines()
file.close()
#################extracting data##################
#WARNING; THIS IS THE MOST INEFFICIENT PIECE OF CODE
#I HAVE EVER WRITTEN IN MY LIFE, BUT, IT WORKS
#I AM SURE THERE IS AN EASIER WAY OF EXTRACTING STRIPED
#DATA FROM A LIST BUT THIS IS THE WAY I USED
array = []
array2 = []
listed = []

radii = []
velocities = []
deltaRadii = []
deltaVelos = []
masses = []
for i in rawData:
    array.append(i)
for i in range(0,len(array)):
    array[i] = array[i].split()

for i in array:
    for x in i:
        listed.append(x)
for i in listed:
    if not str(i).isalpha():
        array2.append(i)


for i in range(11,len(array2),5):
    deltaVelos.append(array2[i])
    
for i in range(12,len(array2),5):
    masses.append(array2[i])
    
for i in range(8,len(array2),5):
    radii.append(array2[i])
    
for i in range(9,len(array2),5):
    velocities.append(array2[i])
    
for i in range(10,len(array2),5):
    deltaRadii.append(array2[i])
    
print("RADII:")
print(radii)
print("\n\n")
print("VELOCITIES: ")
print(velocities)
print("\n\n")
print("DELTARADII: ")
print(deltaRadii)
print("\n\n")
print("DELTAVELOS: ")
print(deltaVelos)
print("\n\n")
print("MASSES: ")
print(masses)

temp = []
for i in range(0,len(array)-1):
    temp.append(radii[i])
    temp.append(velocities[i])
    temp.append(deltaVelos[i])
    temp.append(deltaRadii[i])
    temp.append(masses[i])
    print(temp)
    temp = []
    
datapoints = 100
x = np.array([1,2,3,4,5,6])
y = np.array([10,100,1000,10000,100000,1000000])
y = np.log10(y)
plt.plot(x,y)
plt.xlabel("Pressure/Pa")
plt.ylabel("Volume/m$^3$")
plt.axis([0,7,0,7])
plt.show()

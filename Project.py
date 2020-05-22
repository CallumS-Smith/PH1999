import numpy as np
import matplotlib.pyplot as plt
import math

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
###TESTING####
#Checking lists are correctly populated
#print("RADII:")
#print(radii)
#print("\n\n")
#print("VELOCITIES: ")
#print(velocities)
#print("\n\n")
#print("DELTARADII: ")
#print(deltaRadii)
#print("\n\n")
#print("DELTAVELOS: ")
#print(deltaVelos)
#print("\n\n")
#print("MASSES: ")
#print(masses)

#####TESTING#####
#Ensuring database is rebuilt correctly
#temp = []
#for i in range(0,len(array)-1):
#    temp.append(radii[i])
#    temp.append(velocities[i])
#    temp.append(deltaVelos[i])
#    temp.append(deltaRadii[i])
#    temp.append(masses[i])
#    print(temp)
#    temp = []
#################################################

#Making numpy arrays.. finally...

npradii = np.array(radii)
npvelocities = np.array(velocities)
npmasses = np.array(masses)
npdeltaRadii = np.array(deltaRadii)
npdeltaVelos = np.array(deltaVelos)

#gravitational constant G
G = 4.3e-6
#Function is V = sqrt(GM/r)
calculated = []

#this loop calcualtes the velocity for each mass and radius pair for Q7
for i in range(0, len(masses)):
    
    calculated.append(math.sqrt(float(G*float(masses[i]))/float(radii[i])))
    
npcalculated = np.array(calculated)

datapoints = 100
x = npradii
y = npcalculated
####Second function below###
y2 = npvelocities
############################
plt.plot(x,y)
plt.plot(x,y2)

plt.xlabel("Radius (kpc)")
plt.ylabel("Velocity (km/s)")
plt.show()

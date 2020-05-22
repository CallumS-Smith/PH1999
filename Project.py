import numpy as np
import matplotlib.pyplot as plt
import math

##################importing data##################
file = open("galaxy1.txt","r")
rawData = file.readlines()
file.close()
#################extracting data##################
#WARNING; THIS IS THE MOST INEFFICIENT PIECE OF CODE
#I HAVE EVER WRITTEN TO EXTRACT DATA, BUT, IT WORKS
#I AM SURE THERE IS AN EASIER WAY OF EXTRACTING STRIPED
#DATA FROM A LIST BUT THIS IS THE WAY I USED... commence
#for loops...
array = []
array2 = []
listed = []

radii = []
velocities = []
deltaRadii = []
deltaVelos = []
masses = []
#First for loops split data into a list of lists
#Each row becomes a list of each data element
for i in rawData:
    array.append(i)
for i in range(0,len(array)):
    array[i] = array[i].split()
#################################################

#These next for loops flatten the array into a 1
#dimensional list of elements, striped with the
#5 data elements
for i in array:
    for x in i:
        listed.append(x)
#This next for loop will remove the headings for the
#data so that the final 'array2' will contain only the
#numeric data from galaxy1.txt
for i in listed:
    if not str(i).isalpha():
        array2.append(i)


#These final for loops append the relevant data to each of the
#corresponding: mass/velocity/radius/deltaR/deltaV lists.

#The for loops step through the 1 dimensional list
#created earlier and upon each iteration land on
#the correct element to append to the final lists
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
#This empty list will hold the corresponding calculations to come...
calculated = []

#this loop calcualtes the velocity for each mass and radius pair for Q7
#The answers are stored in calculated
for i in range(0, len(masses)):
    
    calculated.append(math.sqrt(float(G*float(masses[i]))/float(radii[i])))


#converting to numpy array....  
npcalculated = np.array(calculated)


####PLOTTING####
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

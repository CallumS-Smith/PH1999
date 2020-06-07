import numpy as np
import matplotlib.pyplot as plt
import math

##################importing data##################
file = open("galaxy1.txt","r")
rawData = file.readlines()
file.close()

#Creating empty arrays to store corresponding data
radii = []
velocities = []
deltaRadii = []
deltaVelos = []
masses = []

#Iterating through rawData to extract data
for i in range(1,len(rawData)):
    row = rawData[i].split()
    radii.append(float(row[0]))
    velocities.append(float(row[1]))
    deltaRadii.append(float(row[2]))
    deltaVelos.append(float(row[3]))
    masses.append(float(row[4]))

npradii = np.array(radii)
npvelocities = np.array(velocities)
npdeltaRadii = np.array(deltaRadii)
npdeltaVelos = np.array(deltaVelos)
npmasses = np.array(masses)

#gravitational constant G
G = 4.3e-6
#Function is V = sqrt(GM/r)
#This empty list will hold the corresponding calculations to come...
calculated = []

#this loop calcualtes the velocity for each mass and radius pair for Q7
#The answers are stored in calculated
for i in range(0, len(masses)): 
    calculated.append(float(math.sqrt(float(G*float(masses[i]))/float(radii[i]))))


#converting to numpy array....  
npcalculated = np.array(calculated)


####CALCULATING Mdm (mass of dark matter)####
darkMasses = []
p0 = 100e6
rc = 1.87
for i in radii:
    darkMasses.append(float((np.pi*4*p0*float(rc)**2)*(float(i)-rc*math.atan(float(i)/rc))))
npdarkMasses = np.array(darkMasses)


massAndDark = []
for i in range(0,len(masses)):
    massAndDark.append(float(float(masses[i])+float(darkMasses[i])))


calculated2 = []
for i in range(0, len(massAndDark)): 
    calculated2.append(float(math.sqrt(float(G*float(massAndDark[i]))/float(radii[i]))))
npcalculated2 = np.array(calculated2)

npmassAndDark = np.array(massAndDark)

print(massAndDark)
####PLOTTING####
datapoints = 100
x = npradii
y = npvelocities
####Second function below###
y2 = npcalculated
###Mass and Dark mass curves###
y3 = npmasses
y4 = npdarkMasses
y5 = npmassAndDark

y6 = npcalculated2

plt.plot(x,y)
plt.plot(x,y2)
plt.plot(x,y6)
plt.xlabel("Radius (kpc)")
plt.ylabel("Velocities (km/s)")
plt.show()

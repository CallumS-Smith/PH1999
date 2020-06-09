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


##



##
npdarkMasses = np.array(darkMasses)


massAndDark = []
for i in range(0,len(masses)):
    massAndDark.append(float(float(masses[i])+float(darkMasses[i])))


calculated2 = []
for i in range(0, len(massAndDark)): 
    calculated2.append(float(math.sqrt(float(G*float(massAndDark[i]))/float(radii[i]))))
npcalculated2 = np.array(calculated2)
########################################
minchi2=10000
minslope=0.0
Mass = 0
DarkMass = 0
CombinedMass= 0
Velocity = 0

for rho2 in np.arange(10000000, 1000000000, 50000):#Step is high here to increase speed
    total = 0
    for i in range(0,len(radii)):
        Mass = masses[i]
        DarkMass = 4*np.pi*rho2*rc**2*(radii[i]-rc*math.atan(radii[i]/rc))
        CombinedMass = Mass + DarkMass
        Velocity = math.sqrt((G*CombinedMass)/radii[i])
        total +=(velocities[i]-Velocity)**2
        total = total/deltaVelos[i]**2
      
    chi2=total
    if(chi2<minchi2):
        minchi2=chi2
        minslope=rho2
        

#print(minslope)

massAndDark2 = []
for i in range(0,len(masses)):
    DarkMass = 4*np.pi*minslope*rc**2*(radii[i]-rc*math.atan(radii[i]/rc))
    massAndDark2.append(masses[i]+DarkMass)

calculated3 = []
for i in range(0, len(massAndDark2)): 
    calculated3.append(float(math.sqrt(float(G*float(massAndDark2[i]))/float(radii[i]))))
npcalculated3 = np.array(calculated3)
#####ERROR BARS#######
#plus or minus value worked out prevously: 6770000
pm = 6770000
minslopeMax = minslope + pm
uncertainties = []

massAndDark3 = []
for i in range(0,len(masses)):
    DarkMass = 4*np.pi*minslopeMax*rc**2*(radii[i]-rc*math.atan(radii[i]/rc))
    massAndDark3.append(masses[i]+DarkMass)

calculated4 = []
for i in range(0, len(massAndDark2)): 
    calculated4.append(float(math.sqrt(float(G*float(massAndDark3[i]))/float(radii[i]))))
npcalculated4 = np.array(calculated3)

for i in range(0,len(calculated4)):
    uncertainties.append(calculated4[i]-calculated3[i])

npuncertainties = np.array(uncertainties)
    
######################
npmassAndDark = np.array(massAndDark)
#######
fractionOfDarkMass = []
for i in range(0,len(massAndDark2)):
    fractionOfDarkMass.append(massAndDark2[i]/(masses[i]+massAndDark2[i]))

    
#######
print("Fraction of Dark Mass: ", np.average(fractionOfDarkMass))
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
y7 = npcalculated3

plt.plot(x,y)
plt.plot(x,y6)#old curve old rho
plt.plot(x,y7)# New curve new rho2
plt.errorbar(x,y7,npuncertainties,fmt='bo')
plt.xlabel("Radius (kpc)")
plt.ylabel("Velocities (km/s)")
plt.show()

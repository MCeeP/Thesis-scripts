import numpy as np
import sys
from math import *

#Gas conditions
rmm = 78.118 # benzene
ppmL = 1,10,20,50,100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000
#ppmL = 1,10,25,50,100,250,500,1000,2500,5000,10000
temp = 298.15 #in kelvin

#monolayer conditions
apm = 3.0 #nm2/molecule
reten = 1.0 #us
retenS = reten/1000000

#constants
boltz = 1.38e-23 #m2 kg s-2 k-1
avagad = 6.02e23

#fibre optic surface rea
l = 0.2 #mm
d = 0.0015 #mm
sa = 2*pi*(d/2)*l #mm

#number of molecules
TnMol = (sa*1000000000000)/apm

PERs = []
SIperS = 0.0

for ppm in ppmL:
	#gas density
	n = ((ppm*40.9)/1000000)*avagad

	#impacts/retention time unit
	mass = (rmm/avagad)/1000
	vel = (8/(3*pi))*pow(((boltz*temp)/mass),0.5)
	SIperRt = ((sa/1000000)*(n*TnMol*vel*retenS))/((2*TnMol)+((sa/1000000)*n*vel*retenS))
	PERs.append((SIperRt/TnMol)*100)

print PERs
print vel


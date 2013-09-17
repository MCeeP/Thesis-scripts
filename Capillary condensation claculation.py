import math

Ps = 75 #Saturation vapour pressure (mmHg), bezene is 75
V =  24.465 #Ideal gas at 25 degrees C (L/mol)
y =  28.88 #Surface tension (Benzene = 28.88mN/m @ 20 degrees C)
R =  8.3145 #Universal gas constant (L mmHg K Mol)
T =  293.15 #temperature (kelvin)
d = 1.0 #diameter of pour (nm)
r =  d/2 #radius of pour
theta = 0 #contact angle

P = Ps*math.exp(-((2*V*y)/(r*R*T))*math.cos(theta))

ratio = P/Ps
ppm = (ratio*98000)/1000

print 'Suturation pressure ratio'
print ratio
print
print 'Kppmv of capillary condensation:'
print ppm


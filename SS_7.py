#A script graphing the relation between "omega"(omega) and "k" for the
#dispersion relation of lattice vibrations


import matplotlib.pyplot as plt
import numpy as np
import math as m

samplerate = 1000
omega = np.zeros((samplerate, 1))
a = 1
b = 2 #Constants to use in the dispersion relation
c = 1




def relationPlotter(a, b, c):
    k = np.linspace(0, 20, samplerate) #Wavenumber of the lattice vibration
    for n in range(0, k.size):
        omega[n] = m.sqrt((a*(m.sin(2*c*k[n]))**2)+b*(m.sin(c*k[n]))**2)#Dispersion relation
    #print(k, omega)

    plt.plot(k, omega)


for a in range(0, 3): #Used to test the effects of varying the constants
   relationPlotter(a,b,c)

#relationPlotter(a,b,c)

plt.figure()

for b in range(0, 3): #Used to test the effects of varying the constants
   relationPlotter(a,b,c)

#relationPlotter(a,b,c)

#plt.figure()
plt.show()

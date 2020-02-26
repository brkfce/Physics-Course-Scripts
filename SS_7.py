#A script graphing the relation between "omega"(omega) and "k" for the
#dispersion relation of lattice vibrations


import matplotlib.pyplot as plt
import numpy as np
import math as m

samplerate = 1000

k = np.linspace(0, 50, samplerate) #Wavenumber of the lattice vibration
omega = np.zeros((samplerate, 1))
a = 1
b = 1 #Constants to use in the dispersion relation
c = 1

for n in range(0, k.size):
    omega[n] = m.sqrt((a*(m.sin(2*c*k[n]))**2)+b*(m.sin(c*k[n]))**2)#Dispersion relation
#print(k, omega)

plt.plot(k, omega)
plt.show()

"""
A small test of SIR model
"""

__version__ = '0.1'
__author__ = 'Frederico Moeller'


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import e

S = 99999  #susceptible population
beta = 3/7  #infection producing contacts per unit time
I = 1  #infected
R = 0  #recovered or dead
tau = 7 #infection mean period
N=S+R+I
s_pop=[S]
i_pop=[I]
r_pop=[R]
period = 365

for t in range(period):
    fac1 = beta*I*S/N
    fac2 = (I/tau)
    ds = -fac1
    di = fac1 - fac2
    dr = fac2
    S+=ds
    I+=di
    R+=dr
    s_pop.append(S)
    i_pop.append(I)
    r_pop.append(R)

fig, ax = plt.subplots()
ax.plot(s_pop)
ax.plot(i_pop)
ax.plot(r_pop)
plt.show()


    
    

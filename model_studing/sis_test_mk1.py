"""
A small test of SIS model
"""

__author__ = 'Frederico Moeller'
__version__ = '0.1'
__license__ =  'MPL 2.0'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import e

step_size = 0.5
S = 99999  #susceptible population
tau = 7*(1/step_size) #infection mean period
beta = 3/tau  #infection producing contacts per unit time
I = 1  #infected
#R = 0  #recovered or dead
N=S+I
s_pop=[S]
i_pop=[I]
period = int(365*(1/step_size))
time_stamp = np.array(range(period+1))*step_size

np.random.seed(1104)

for t in range(period):
    fac1 = beta*I*S/N
    fac2 = (I/tau)
    ds = -fac1 + fac2
    di = fac1 - fac2
    S += ds
    I += di
    s_pop.append(S)
    i_pop.append(I)
    N=S+I

fig, ax = plt.subplots()
ax.set_title("Normal")
ax.plot(time_stamp,s_pop)
ax.plot(time_stamp,i_pop)
plt.show()  

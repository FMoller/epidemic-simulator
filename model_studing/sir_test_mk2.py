"""
A small test of SIR model with population reposition
"""

__author__ = 'Frederico Moeller'
__version__ = '0.2'
__license__ =  'MPL 2.0'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import e

step_size = 0.5
S = 99999  #susceptible population
tau = 7*(1/step_size) #infection mean period
beta = 3/tau  #infection producing contacts per unit time
mu = (6.9*2 /(1000*365))*(1/step_size) #death rate
delta = (22.7 /(1000*365))*(1/step_size) #birth  rate
I = 1  #infected
R = 0  #recovered or dead
N=S+R+I
s_pop=[S]
i_pop=[I]
r_pop=[R]
n_pop=[N]
period = int(3650*(1/step_size))
time_stamp = np.array(range(period+1))*step_size

np.random.seed(1104)

for t in range(period):
    fac1 = beta*I*S/N
    fac2 = (I/tau)
    ds = delta*N - mu*S - fac1
    di = fac1 - fac2 - mu*I
    dr = fac2 - mu*R
    S+=ds
    I+=di
    R+=dr
    s_pop.append(S)
    i_pop.append(I)
    r_pop.append(R)
    N=S+R+I
    n_pop.append(N)

fig, ax = plt.subplots()
ax.set_title("Normal")
ax.plot(time_stamp,s_pop)
ax.plot(time_stamp,i_pop)
ax.plot(time_stamp,r_pop)
ax.plot(time_stamp,n_pop)
plt.show()

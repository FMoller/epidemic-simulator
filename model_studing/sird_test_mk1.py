"""
A small test of SIRD model
"""

__author__ = 'Frederico Moeller'
__version__ = '0.1'
__license__ =  'MPL 2.0'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import e

step_size = 0.125
S = 99999  #susceptible population
tau = 13*(1/step_size) #infection mean period
beta = 6/tau  #infection producing contacts per unit time
mu = 0.1/tau #death rate by the infection
I = 1  #infected
R = 0  #recovered
D = 0 #dead by the infection
N=S+R+I
s_pop=[S]
i_pop=[I]
r_pop=[R]
d_pop=[D]
n_pop=[N]
period = int(800*(1/step_size))
time_stamp = np.array(range(period+1))*step_size

np.random.seed(1104)

for t in range(period):
    fac1 = beta*I*S/N
    fac2 = (I/tau)
    ds = -fac1
    di = fac1 - fac2 - mu*I
    dr = fac2
    dd = mu*I
    S+=ds
    I+=di
    R+=dr
    D+=dd
    s_pop.append(S)
    i_pop.append(I)
    r_pop.append(R)
    d_pop.append(D)
    N=S+R+I
    n_pop.append(N)

fig, ax = plt.subplots()
ax.set_title("Normal")
ax.plot(time_stamp,s_pop,label='s')
ax.plot(time_stamp,i_pop,label='i')
ax.plot(time_stamp,r_pop,label='r')
ax.plot(time_stamp,d_pop,label='d')
ax.plot(time_stamp,n_pop,label='n')
plt.legend()
plt.show()

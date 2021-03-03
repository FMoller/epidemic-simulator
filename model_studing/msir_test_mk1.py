"""
A small test of MSIR model
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
tau = 7*(1/step_size) #infection mean period
beta = 6/tau  #infection producing contacts per unit time
mu = 0.002/tau #death rate by the infection
big_delta = (22.7 /(1000*365))*(1/step_size) #birth  rate
delta = 1/(30*(1/step_size))#passive immunity period
M = 0 #passive immunity newborns
I = 1  #infected
R = 0  #recovered
N=S+R+I+M
m_pop=[M]
s_pop=[S]
i_pop=[I]
r_pop=[R]
n_pop=[N]
period = int(365*(1/step_size))
time_stamp = np.array(range(period+1))*step_size

np.random.seed(1104)

for t in range(period):
    fac1 = beta*I*S/N
    fac2 = (I/tau)
    dm = big_delta*N -delta*M -mu*M
    if dm<0:
        dm=0
##    if t%30:
##        print(dm)
    ds = delta*M -fac1 -mu*S
    di = fac1 -fac2 -mu*I
    dr = fac2 -mu*R
    M+=dm
    S+=ds
    I+=di
    R+=dr
    m_pop.append(M)
    s_pop.append(S)
    i_pop.append(I)
    r_pop.append(R)
    N=S+R+I+M
    n_pop.append(N)

fig, ax = plt.subplots()
ax.set_title("Normal")
ax.plot(time_stamp,m_pop,label='m')
ax.plot(time_stamp,s_pop,label='s')
ax.plot(time_stamp,i_pop,label='i')
ax.plot(time_stamp,r_pop,label='r')
ax.plot(time_stamp,n_pop,label='n')
plt.legend()
plt.show()

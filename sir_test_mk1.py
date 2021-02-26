"""
A small test of SIR model
"""

__author__ = 'Frederico Moeller'
__version__ = '0.2'
__license__ =  'MPL 2.0'



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import e

S = 99999  #susceptible population
SR2 = SR1 = S
beta = 3/7  #infection producing contacts per unit time
I = 1  #infected
IR2 = IR1 = I
R = 0  #recovered or dead
RR2 = RR1 = R
tau = 7 #infection mean period
N=S+R+I
NR2 = NR1 = N
s_pop=[S]
i_pop=[I]
r_pop=[R]
sr1_pop=[SR1]
ir1_pop=[IR1]
rr1_pop=[RR1]
sr2_pop=[SR2]
ir2_pop=[IR2]
rr2_pop=[RR2]
period = 150

for t in range(period):
    tfac = np.random.normal(0,2)
    fac1 = beta*I*S/N
    fac1R1 = beta*IR1*SR1/NR1
    fac2 = (I/tau)
    fac2R1 = (IR1/(tau+tfac))
    ds = -fac1
    dsR1 = -fac1R1
    di = fac1 - fac2
    diR1 = fac1R1 - fac2R1
    dr = fac2
    drR1 = fac2R1
    S+=ds
    SR1+=dsR1
    I+=di
    IR1+=diR1
    R+=dr
    RR1+=drR1
    s_pop.append(S)
    sr1_pop.append(SR1)
    i_pop.append(I)
    ir1_pop.append(IR1)
    r_pop.append(R)
    rr1_pop.append(RR1)

fig, ax = plt.subplots(2)
ax[0].plot(s_pop)
ax[0].plot(i_pop)
ax[0].plot(r_pop)
ax[1].plot(sr1_pop)
ax[1].plot(ir1_pop)
ax[1].plot(rr1_pop)
plt.show()


    
    

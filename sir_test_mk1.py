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

step_size = 0.5
S = 99999  #susceptible population
SR2 = SR1 = S
tau = 7*(1/step_size) #infection mean period
beta = 3/tau  #infection producing contacts per unit time
I = 1  #infected
IR2 = IR1 = I
R = 0  #recovered or dead
RR2 = RR1 = R
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
period = int(100*(1/step_size))
time_stamp = np.array(range(period+1))*step_size

for t in range(period):
    tfac = np.random.normal(0,2)
    bfac = np.random.normal(0,1)
    beta2 = (beta*tau + bfac)/tau
    fac1 = beta*I*S/N
    fac1R1 = beta*IR1*SR1/NR1
    fac1R2 = beta2*IR2*SR2/NR2
    fac2 = (I/tau)
    fac2R1 = (IR1/(tau+tfac))
    fac2R2 = (IR2/tau)
    ds = -fac1
    dsR1 = -fac1R1
    dsR2 = -fac1R2
    di = fac1 - fac2
    diR1 = fac1R1 - fac2R1
    diR2 = fac1R2 - fac2R2
    dr = fac2
    drR1 = fac2R1
    drR2 = fac2R2
    S+=ds
    SR1+=dsR1
    SR2+=dsR2
    I+=di
    IR1+=diR1
    IR2+=diR2
    R+=dr
    RR1+=drR1
    RR2+=drR2
    s_pop.append(S)
    sr1_pop.append(SR1)
    sr2_pop.append(SR2)
    i_pop.append(I)
    ir1_pop.append(IR1)
    ir2_pop.append(IR2)
    r_pop.append(R)
    rr1_pop.append(RR1)
    rr2_pop.append(RR2)
    N=S+R+I
    NR1=SR1+RR1+IR1
    NR2=SR2+RR2+IR2

fig, ax = plt.subplots(2,2)
ax[0,0].set_title("Normal")
ax[0,0].plot(time_stamp,s_pop)
ax[0,0].plot(time_stamp,i_pop)
ax[0,0].plot(time_stamp,r_pop)
ax[0,1].set_title("Var inf time")
ax[0,1].plot(time_stamp,sr1_pop)
ax[0,1].plot(time_stamp,ir1_pop)
ax[0,1].plot(time_stamp,rr1_pop)
ax[1,0].set_title("Var spread")
ax[1,0].plot(time_stamp,sr2_pop)
ax[1,0].plot(time_stamp,ir2_pop)
ax[1,0].plot(time_stamp,rr2_pop)
plt.show()


    
    

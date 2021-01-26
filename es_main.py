import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import es_classes as ec
import es_func as ef

N_IND = 200
A = 50
T_ITER = 1000

AREA = np.zeros((A,A))
ZONES = ef.set_zones(A)
RD = ZONES[0][0]
RL = ZONES[0][1]
RC = ZONES[0][2]

popul = []



####################
#Placing           #
####################
for i in range(N_IND):
    pos_x = np.random.randint(A)
    pos_y = np.random.randint(A)
    popul.append(ec.Individual((pos_x,pos_y),(0,0),(0,0),(0,0)))
    
#teste
for i in popul:
    AREA[i.pos[0],i.pos[1]]=1

#for i in range(T_ITER)

fig, ax = plt.subplots()
ax.imshow(AREA)
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import es_classes as ec

N_IND = 20
A = 10
T_ITER = 1000

AREA = np.zeros((A,A))
RD =((0,0),(32,32))
RC =((25,25),(75,75))

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

"""
a simple SIR model as cellular automata
"""

__author__ = 'Frederico Moeller'
__version__ = '0.1'
__license__ =  'MPL 2.0'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import aux_picker as pk
from math import e

area = 50
space = np.zeros((area,area))
i_ppp = 0.25
i_dur = 7
step_size = 0.5
period = int(100*(1/step_size))
colspace = []

def get_neighboor(coord, area):
    if coord[0] == 0:
        if coord[1] == 0:
            return [
                space[coord[0],coord[1]+1],
                space[coord[0]+1,coord[1]],
                space[coord[0]+1,coord[1]+1],
                ]
        elif coord[1] == area-1:
            return [
                space[coord[0],coord[1]-1],
                space[coord[0]+1,coord[1]],
                space[coord[0]+1,coord[1]-1],
                ]
        else:
            return [
                space[coord[0],coord[1]-1],
                space[coord[0],coord[1]+1],
                space[coord[0]+1,coord[1]],
                space[coord[0]+1,coord[1]-1],
                space[coord[0]+1,coord[1]+1],
                ]
    elif coord[0] == area-1:
        if coord[1] == 0:
             return [
                space[coord[0],coord[1]+1],
                space[coord[0]-1,coord[1]],
                space[coord[0]-1,coord[1]+1],
                ]
        elif coord[1] == area-1:
            return [
                space[coord[0],coord[1]-1],
                space[coord[0]-1,coord[1]],
                space[coord[0]-1,coord[1]-1],
                ]
        else:
            return [
                space[coord[0],coord[1]-1],
                space[coord[0],coord[1]+1],
                space[coord[0]-1,coord[1]],
                space[coord[0]-1,coord[1]-1],
                space[coord[0]-1,coord[1]+1],
                ]
    else:
        if coord[1] == 0:
             return [
                space[coord[0]-1,coord[1]],
                space[coord[0]+1,coord[1]],
                space[coord[0],coord[1]+1],
                space[coord[0]-1,coord[1]+1],
                space[coord[0]-1,coord[1]+1],
                ]
        elif coord[1] == area-1:
            return [
                space[coord[0]-1,coord[1]],
                space[coord[0]+1,coord[1]],
                space[coord[0],coord[1]-1],
                space[coord[0]-1,coord[1]-1],
                space[coord[0]-1,coord[1]-1],
                ]
        else:
            return [
                space[coord[0]-1,coord[1]-1],
                space[coord[0],coord[1]-1],
                space[coord[0]+1,coord[1]-1],
                space[coord[0]-1,coord[1]],
                space[coord[0]+1,coord[1]],
                space[coord[0]-1,coord[1]+1],
                space[coord[0],coord[1]+1],
                space[coord[0]+1,coord[1]+1],
                ]
        
def eval_cell(coord):
    #print(coord)
    if space[coord[0],coord[1]] == 1:
        return 1
    elif space[coord[0],coord[1]] == 2:
        chance = step_size/i_dur
        if np.random.rand() < chance:
            return  1
        return 2
    else:
        vizinhos = get_neighboor(coord,area)
        for i in vizinhos:
            if i == 2:
                chance = step_size*i_ppp
                if np.random.rand() < chance:
                    return  2
        return 0

def eval_line(line):
    coords = [(line,i) for i in range(area)]
    return list(map(eval_cell,coords)) 


                
        



#space_img = np.ones((area,area,3))
"""
0 -> S susceptivle
1 -> R removed
2 -> I infected

"""
#space[0,0] = 1
#space[0,1] = 2
N = area*area
I = 1
R = 0
S = N -I -R



st_inf = pk.few_picks(1,(area,area))
for i in st_inf:
    space[i[0],i[1]]=2
colspace.append(space.copy())
for t in range(period):
    space[:,:] = list(map(eval_line, range(area)))
    colspace.append(space.copy())
    

def anima(col,iterMax = period):
    fig, axt = plt.subplots()
    for i in range(iterMax+1):
        axt.cla()
        axt.imshow(col[i])
        axt.set_title("frame {}".format(i))
        plt.pause(0.1)

anima(colspace)

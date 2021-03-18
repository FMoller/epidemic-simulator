"""
a simple SIR model as cellular automata
"""

__author__ = 'Frederico Moeller'
__version__ = '0.1'
__license__ =  'MPL 2.0'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import e

area = 50
space = np.zeros((area,area))
#space_img = np.ones((area,area,3))
"""
0 -> S susceptivle 
1 -> I infected
2 -> R removed
"""
#space[0,0] = 1
#space[0,1] = 2
N = area*area
I = 1
R = 0
S = N -I -R



fig, ax=plt.subplots()
ax.imshow(space)
plt.show()

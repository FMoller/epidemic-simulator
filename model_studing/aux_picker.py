"""
Auxiliary functions to pick random coordinates in a matrix
"""

__author__ = 'Frederico Moeller'
__version__ = '0.1'
__license__ =  'MPL 2.0'

import numpy as np
import itertools as it

def few_picks(picks, dim):
    r_picks = []

    for i in range(picks):
        while True:
            n_pick = tuple(np.random.randint(list(dim)))
            if n_pick not in r_picks:
                r_picks.append(n_pick)
            break
    return r_picks

def many_picks(picks, dim):
    r_picks = []
    d_range = list(map(list,list(map(range,dim))))
    coord = list(it.product(d_range[0],d_range[1]))
    np.random.shuffle(coord)
    r_picks = coord[:picks]
    
    return r_picks
    

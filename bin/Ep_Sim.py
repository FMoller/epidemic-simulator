"""
Epidemic Simulator 
"""

__author__ = 'Frederico Moeller'
__version__ = '0.1'
__license__ =  'MPL 2.0'

import sys, getopt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import e



def main(argv):
    """
    Arguments:
    0 - Susceptivle pop , 1 - Infected pop, 2 - Recovered pop
    3 - step size in fraction of a day, 4 - infection mean period in days
    5 - Infections produced by contacts in the infection mean period
    6 - Total period in days
    7 - Output file CSV
    8 - Output file graph
    9 - Seed
    """
    args = sys.argv
    S = int(args[1])
    I = int(args[2])
    R = int(args[3])
    step_size = int(args[4])
    tau = int(args[5])*(1/step_size)
    beta = int(args[6])/tau
    period = int(int(args[7])*(1/step_size))
     
    N=S+R+I
    s_pop=[S]
    i_pop=[I]
    r_pop=[R]
    n_pop=[N]
    
    

if __name__ == "__main__":
    main()

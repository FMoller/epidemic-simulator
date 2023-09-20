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
    3 - step size, 4 - infection mean period
    5 - Infections produced by contacts in the infection mean period
    
    6 - Output file CSV
    7 - Output file graph
    """
    args = sys.argv

if __name__ == "__main__":
    main()

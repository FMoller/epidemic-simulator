"""
Epidemic simulator classes

This module contains the classes from the epidemic simulator
"""

__version__ = '0.1'
__author__ = 'Frederico Moeller'


import numpy as np
import pandas as pd


class Node:    
    def __init__(
            self, idt, name,
            kind, mce, neighboors
            population, density):
        
        self.idt = idt       
        self.name = name
        self.kind = kind  #0-Residential 1-Industrial 2-Commercial
        self.mce = mce    #The ID of the main next node to go to the center
        self.sts = neighboors  #A list with the IDs of all neighboors
        self.population = population
        self.density = density

    

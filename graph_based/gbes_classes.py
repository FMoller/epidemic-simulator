import numpy as np
"""
Epidemic simulator classes

This module contains the classes from the epidemic simulator
"""

__version__ = '0.1'
__author__ = 'Frederico Moeller'

class node:
    def __init__(self,base_id,name,node_type,pattern_matrix,connections,n2c):
        self.base_id = base_id
        self.name = name
        self.node_type = node_type
        self.pattern_matrix = pattern_matrix
        self.connections = connections
        self.next_to_center = n2c
        self.population  = 0 #mudar, colocar como vetor
        self.density = 0
        

class p_matrix:
    pass

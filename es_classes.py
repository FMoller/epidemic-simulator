import numpy as np
import pandas as pd


class Individual:
    def __init__(self,posicao,adress,work,leisure):
        self.pos = posicao
        self.adr = adress
        self.wrk = work
        self.lei = leisure
        self.sts = 0
        #0 = susceptible ; 1 = contaminated ; 2 = recovered ; 4 = immunized
    

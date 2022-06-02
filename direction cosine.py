# -*- coding: utf-8 -*-
"""
Created on Mon May 31 16:26:38 2021

@author: jenny
"""
#let U and V be matrices already known to the algorithm. 
#to use this we must know the previous def stored into mathematical calculations
#and the transposing function from numpy (perhaps a little childish of me to use numpy but here we are)

import numpy as np
K = matrix(U)
L = matrix(V)

def direction_cosine(K,L):
    
    A = []
    newL = L.transpose()
    n = len(K) #number of rows
    l = len(K[0]) #number of collumns
    #same with m
    k = len(newL)
    t = len(newL[0])
    
    for i in range (n-1):
        for s in range (l-1):
            r = 0
            while j<(l-1) and f<(t-1):
                r = r+ K[j]*newL[f]
                j=j+1
                f=f+1
            A.append(r)
    return A

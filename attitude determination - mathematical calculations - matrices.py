# -*- coding: utf-8 -*-
"""
Created on Mon May 31 15:59:46 2021

@author: jenny
"""

#mathematical calculations - matrices

#let U and V be matrices already known to the algorithm. 
#They are orthogonal and they are what B (from observed stars) dicomposes into

import numpy as np


def matrix(U):
    a = np.linalg.det(U)
    m = np.array([[1,0,0],[0,1,0],[0,0,a]])
    print(m)
    n = len(U) #number of rows
    l = len(U[0]) #number of collumns
    #same with m
    k = len(m)
    t = len(m[0])
    newU = []
    i = 0    
    for i in range (n):
        
        temp = []
        j = 0
        
        for j in range (k):
            r = 0
            f = 0
            s = 0
            while f <= (t-1) and s<=(l-1):

                r = r + U[i][s]*m[f][j]
                s = s + 1
                f = f + 1
        
           
        	temp.append(r)        
    	newU.append(temp)
            
    return newU

newU = matrix(U)
newV = matrix(VT)
#for V we also need to find it's transposed equivalent

#now we need to find the final matrix A

def A(newU,newV):

    arr1 = np.array(newV)    
    VT = arr1.transpose()
    n = len(newU)
    l = len(newU[0])
    k = len(VT)
    t = len(VT[0])
    A = []
    i = 0    
    for i in range (n):
        
        temp = []
        j = 0
        
        for j in range (k):
            r = 0
            f = 0
            s = 0
            while f <= (t-1) and s<=(l-1):

                r = r + U[i][s]*VT[f][j]
                s = s + 1
                f = f + 1
        
           
        	temp.append(r)        
    	A.append(temp)
    return A

finalA = np.array(A(newU,newV))
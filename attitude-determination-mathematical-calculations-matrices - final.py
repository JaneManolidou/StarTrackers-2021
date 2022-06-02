# -*- coding: utf-8 -*-
"""
Created on Mon May 31 15:59:46 2021

@author: jenny
"""

#mathematical calculations - matrices

#let U and V be matrices already known to the algorithm. 
#They are orthogonal and they are what B (from observed stars) dicomposes into

import numpy as np
from scipy.linalg import svd


n = np.array([[1], [2], [3]])   # identified observed stars
#print(n)

#bn1 = np.array([[1], [2], [3]])  # unit vectors of n'th candidate star
#bn2 = np.array([[8], [7], [7]])
#bn3 = np.array([[3], [9], [4]])
#print (bn1,bn2,bn3)
#rn1 = np.array([[5], [2], [8]])  # unit vectors of n'th catalogue star
#rn2 = np.array([[1], [2], [3]])
#rn3 = np.array([[4], [9], [2]])

bn = np.array([[3], [6], [4]])
#print(bn)
rn = np.array([[1], [2], [3]])

matrix0 = np.array([[n], [bn], [rn]])

B0 = 0

for i in matrix0:

    Bn = bn.dot(rn.transpose())
    B0 = B0 + Bn
print("B", B0)
# 2nd function

U, D, VT = np.linalg.svd(B0)

print("U", U)
print("D", D)
print("VT", VT)


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


#for V we also need to find it's transposed equivalent

#now we need to find the final matrix A
newU = matrix(U)
newV = matrix(VT)

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

finalA= A(newU,newV)

print("A is: ", finalA)
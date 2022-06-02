# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 15:55:06 2021

@author: jenny
"""
Raxis = []
Thaxis = []
Phaxis = []


def initializing():
    ro = input("give initial position r: ")
    tho = input("give initial position th: ")
    pho = input("give initial position ph: ")
    Raxis.append(ro)
    Thaxis.append(tho)
    Phaxis.append(pho)
    
initializing()

r=float(input("give an r: " ))
th=input("give a theta in degrees: ")
ph = input("give a ph in degrees : ")
ur=0
uth=0

t = 0.000005

def oracle(r,th,ph):
     
    Raxis.append(r)
    Thaxis.append(th)
    Phaxis.append(ph)
    if input("Is it moving east to west")=="y":
        EastToWest = True
    if EastToWest == True:
        uph= -460
    else:
        uph = 460
    ur = (float(Raxis[1])-float(Raxis[0]))/t
    uth = (float(Thaxis[1])-float(Thaxis[0]))/t
    uph = uph + (float(Phaxis[1])-float(Phaxis[0]))/t
    
    r = float(Raxis[1]) + ur*t
    th = float(Thaxis[1]) + uth*t
    ph = float(Phaxis[1]) + uph*t
   
    if float(Phaxis[1])>=0 and float(Phaxis[1])<=90:
                
        if ph>90:
            ph = ph - 360
        
    if float(Phaxis[1])<0 and float(Phaxis[1])>=-90:
        
        if ph<-90:
            ph = ph + 360
    
    del(Raxis[0])
    del(Thaxis[0])
    del(Phaxis[0])
    
    
    
    return([r,th,ph])


new = oracle(r,th, ph)
print(new)

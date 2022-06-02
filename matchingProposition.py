# -*- coding: utf-8 -*-
"""
Created on Sat May  1 21:25:39 2021

@author: jenny
"""


error = 0.01
#error is tolerance

def matching_lists (real_angular_distances, angdis):
    #real_angular_distances is a list of n lists of 3 values: (x1,y1), (x2,y2) and angular distance
    newlist = []
    k=[]
    length = len(real_angular_distances)
    for i in range(0,length-1):
        k=real_angular_distances[i]
        if k[2] > (angdis-error) and k[2] < (angdis+error):
            newlist.append(real_angular_distances[i])
        del(k[0])
        
    if len(newlist)!= 0:    
        return newlist
    else:
        print("failed to find match")
        





def process_matching (newlist,angdis):
    
    length = len(newlist)
    k = newlist[0]
    min = abs(k[2]-angdis)
    place = 0
    for i in range(1, length-1):
        del(k[0])
        k=newlist[i]
        a = abs(k[2]-angdis)
        if a < min:
            min = a
            place = i
    match = []
    again = newlist[place]
    match.append(again[0])
    match.append(again[1])
    
    return match
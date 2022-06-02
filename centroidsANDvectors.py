# -*- coding: utf-8 -*-
"""
Created on Sat May  1 20:48:52 2021

@author: jenny
"""

def star_vector (xcm,ycm):
    
    #turns the coordinates of a star on a square image to a unit vector
    
    Vmagnitude = xcm*xcm + ycm*ycm
    
    ux = xcm/Vmagnitude
    uy = ycm/Vmagnitude
    
    vector = (ux , uy )
    
    return vector

#the centroid_location function refers to the star_points_table of the photo, which is also known as "points" in other functions

def centroid_location (star_points_table, points_intensity):
    
    length = len(star_points_table)
    x1 = 0
    y1 = 0
    for i in range (0,length-1):
        
        x1 = x1 + star_points_table[i[0]]  
        y1 = y1 + star_points_table[i[1]]
        
    xcm = x1/length
    ycm = y1/length
    
    return [xcm,ycm]
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 22:07:07 2021

@author: jenny
"""
#let angdis the angular distance between 2 stars that can be found on the photo. 
#points, is the list of each star point's location on the photo. It only lists their centroid's locations
#real_angular_distances is the shrunken star catalogue data base
#this algorithm refers to a lot of functions stored in different python files

def pair_processing(points):

    final_matches = []
    l = len(points)
    for i in range(0,l-1):
        for j in range(0,l-1):
            if j == i :
                continue
            k = points[i]
            n = points[j]
            u1 = star_vector(k[0],k[1])
            u2 = star_vector(n[0],n[1])
            angdis = angular_distance (u1, u2)
            possible_matches = matching_lists(real_angular_distances, angdis)
            final_matches.append(process_matching (possible_matches,angdis))
            del(k[i])
            del(n[j])
            possible_matches = []

    print(final_matches)
    return final_matches
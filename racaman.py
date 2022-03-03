#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 12:30:54 2022

@author: tandeitnik
"""

import numpy as np
import matplotlib.pyplot as plt

max_jump = 10000
circle_resolution = 1000


visited_numbers = {0}
sequence = np.zeros(max_jump)

for i in range(1,max_jump):
    
    if sequence[i-1] - i < 0 or (sequence[i-1] - i) in visited_numbers:
        
        sequence[i] = sequence[i-1] + i
        visited_numbers.add(sequence[i-1] + i)
        
    else:
        
        sequence[i] = sequence[i-1] - i
        visited_numbers.add(sequence[i-1] - i)
        
racaman_x_points = np.zeros(circle_resolution*(max_jump-1))
racaman_y_points = np.zeros(circle_resolution*(max_jump-1))

for i in range(max_jump-1):
    
    if i%2 == 0:
        
        sign = -1
        
    else:
        
        sign = 1
        
    r = np.abs(sequence[i]-sequence[i+1])/2
    center = min(sequence[i],sequence[i+1]) + r
    
    if sequence[i+1] > sequence[i]:
    
        racaman_x_points[i*circle_resolution:(i+1)*circle_resolution] = r*np.sin(np.array(range(circle_resolution))*1*np.pi/circle_resolution - np.pi/2) + center
        racaman_y_points[i*circle_resolution:(i+1)*circle_resolution] = sign*r*np.cos(np.array(range(circle_resolution))*1*np.pi/circle_resolution - np.pi/2)

    else:
        
        racaman_x_points[i*circle_resolution:(i+1)*circle_resolution] = np.flip(r*np.sin(np.array(range(circle_resolution))*1*np.pi/circle_resolution - np.pi/2) + center)
        racaman_y_points[i*circle_resolution:(i+1)*circle_resolution] = sign*r*np.cos(np.array(range(circle_resolution))*1*np.pi/circle_resolution - np.pi/2)


plt.plot(racaman_x_points,racaman_y_points)
plt.axis("off")

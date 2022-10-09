#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:24:43 2022

@author: tandeitnik
"""

import numpy as np
import matplotlib.pyplot as plt

#number of iterations
steps = 10

#this set contains the end points of the set at each step
cantorSet = [ [ [0,1] ] ]

#evaluation of the set after each step
for i in range(steps):
    
    tempSet = []
    
    for j in range(len(cantorSet[-1])):
        
        d = cantorSet[-1][j][1] - cantorSet[-1][j][0]
        tempSet.append([cantorSet[-1][j][0],cantorSet[-1][j][0] + d/3])
        tempSet.append([cantorSet[-1][j][0] + (2/3)*d,cantorSet[-1][j][1]])
        
    cantorSet.append(tempSet)

#plotting of the various sets
y = np.array([steps,steps])

for i in range(steps+1):
    
    for j in range(len(cantorSet[i])):
        
        plt.plot(cantorSet[i][j],y,c = 'k')
        
    y -= 1

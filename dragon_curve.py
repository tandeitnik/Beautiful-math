#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 08:00:53 2022

@author: tandeitnik
"""

import numpy as np
import matplotlib.pyplot as plt

steps = 2

seed_x = [0,0,1]
seed_y = [0,1,1]

#plt.plot(seed_x,seed_y)

for step in range(steps):

    seed_x_temp = [0]
    seed_y_temp = [0]
    
    sign = 1
    
    for i in range(len(seed_x)-1):
        
        
        x_0 = [seed_x[i],seed_x[i+1]]
        y_0 = [seed_y[i],seed_y[i+1]]

        scale = np.cos(45*np.pi/180)

        
        x_1 = [x_0[0],x_0[0]+scale*((x_0[1]-x_0[0])*np.cos(sign*45*np.pi/180) -(y_0[1]-y_0[0])*np.sin(sign*45*np.pi/180))]
        y_1 = [y_0[0],y_0[0]+scale*((x_0[1]-x_0[0])*np.sin(sign*45*np.pi/180) +(y_0[1]-y_0[0])*np.cos(sign*45*np.pi/180))]
        

        
        seed_x_temp.append(x_1[1])
        seed_y_temp.append(y_1[1])
        
        sign = sign*(-1)
        

        
        seed_x_temp.append(seed_x[i+1])
        seed_y_temp.append(seed_y[i+1])
        

    
    seed_x = seed_x_temp
    seed_y = seed_y_temp
    
plt.plot(seed_x,seed_y)
plt.axis('off')
plt.gca().set_aspect('equal', adjustable='box')
plt.tight_layout()

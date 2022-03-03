#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 18:14:46 2022

@author: tandeitnik
"""

import numpy as np
import matplotlib.pyplot as plt

seed_x = np.array([1,1,3,3])
seed_y = np.array([1,3,3,1])



steps = 4

for k in range(steps):
    
    #rotating 90
    
    left_inf_x = np.copy(seed_y)
    left_inf_y = np.copy(seed_x)
    
    #plt.plot(left_inf_x,left_inf_y)
    
    #two copies deslocated
    
    left_sup_x = np.copy(seed_x)
    left_sup_y = np.copy(seed_y) + 4*2**k
    
    #plt.plot(left_sup_x,left_sup_y)
    
    right_sup_x = np.copy(seed_x) + 4*2**k
    right_sup_y = np.copy(seed_y) + 4*2**k
    
    #plt.plot(right_sup_x,right_sup_y)
    
    # rotated flipped deslocated
    
    right_inf_x = np.flip(np.copy(seed_y))
    right_inf_y = np.flip(np.copy(seed_x))
    
    centro = 2*2**k
    
    for j in range(len(right_inf_x)):
        
        if right_inf_x[j] < centro:
            
            right_inf_x[j] += 2*(centro-right_inf_x[j])
            
        elif right_inf_x[j] > centro:
            
            right_inf_x[j] -= 2*(right_inf_x[j]-centro)
            
    right_inf_x = right_inf_x +  4*2**k
    
    #plt.plot(right_inf_x,right_inf_y)
    
    #piecing it all together
    
    seed_x = np.array(list(left_inf_x) + list(left_sup_x) + list(right_sup_x)+ list(right_inf_x))
    seed_y = np.array(list(left_inf_y) + list(left_sup_y) + list(right_sup_y)+ list(right_inf_y))
    #plt.plot(seed_x,seed_y)
    
    
plt.plot(seed_x,seed_y)
plt.axis("off")
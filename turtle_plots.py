#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 16:05:50 2022

@author: tandeitnik
"""

#https://www.youtube.com/watch?v=kMBj2fp52tA&ab_channel=Numberphile

import numpy as np
import matplotlib.pyplot as plt


### Euler Spirals - esse aqui começa com um seed e os passos seguintes multiplicam o seed por 2, 3, 4, etc e soma ao angulo anterior

steps = 2

turtle_direction = np.zeros(steps) #the direction is the angle in radians the turtle makes with the x axis. I Assume it always walks unit distance steps


seed = 1.03 *(np.pi/180)

turtle_direction[0] = seed

for i in range(1,steps):
    
    turtle_direction[i] = turtle_direction[i-1]+seed*(i+1)
    #turtle_direction[i] = turtle_direction[i-1]*(i+1)
    
x_points = np.zeros(steps+1)
y_points = np.zeros(steps+1)

for i in range(steps):
    
    x_points[i+1] = x_points[i] + np.cos(turtle_direction[i])
    y_points[i+1] = y_points[i] + np.sin(turtle_direction[i])
    
plt.plot(x_points,y_points, lw = 0.5)
plt.axis('off')
plt.gca().set_aspect('equal', adjustable='box')
plt.tight_layout()


### esse aqui faz Sierpiński Triangles

steps = 8
turn_degrees = 80

sequence = ['x']

for i in range(steps):
    
    sequence_temp = []
    
    for j in range(len(sequence)):
        
        if sequence[j] == '+':
            
            sequence_temp.append('+')
            
        elif sequence[j] == '-':
            
            sequence_temp.append('-')
            
        elif sequence[j] == 'x':
            
            sequence_temp = sequence_temp + ['y','+','x','+','y']
            
        else:
            
            sequence_temp = sequence_temp + ['x','-','y','-','x']
            
    sequence = sequence_temp
    
turtle_direction = np.zeros(int((len(sequence)-1)/2)+1)

for i in range(len(turtle_direction)-1):
    
    if sequence[2*i+1] == '+': #turn right 60 degrees
    
        turtle_direction[i+1] = turtle_direction[i]- turn_degrees *(np.pi/180)
        
    elif sequence[2*i+1] == '-': #turn left 60 degrees
    
        turtle_direction[i+1] = turtle_direction[i]+turn_degrees *(np.pi/180)
        
x_points = np.zeros(len(turtle_direction)+1)
y_points = np.zeros(len(turtle_direction)+1)

for i in range(len(turtle_direction)):
    
    x_points[i+1] = x_points[i] + np.cos(turtle_direction[i])
    y_points[i+1] = y_points[i] + np.sin(turtle_direction[i])
    
plt.plot(x_points,y_points, alpha = 1, lw = 1)
plt.axis('off')
plt.gca().set_aspect('equal', adjustable='box')
plt.tight_layout()

## esse sorteia um número aleatório numa base e os ângulos são frações dos digitos no circulo

digits = 1000 #how many digits
base = 3

import random

def rand_key(digits,base):

    key1 = ""
 
    for i in range(digits):
         
        temp = str(random.randint(0, base-1))
 
        key1 += temp
         
    return(key1)

random_number = rand_key(digits,base)

turtle_direction = np.zeros(digits+1)

count = 0

for digit in random_number:
    
    turtle_direction[count+1] = turtle_direction[count] + int(digit)*(2*np.pi/base)
    count += 1
    
x_points = np.zeros(digits+1)
y_points = np.zeros(digits+1)

for i in range(digits):
    
    x_points[i+1] = x_points[i] + np.cos(turtle_direction[i])
    y_points[i+1] = y_points[i] + np.sin(turtle_direction[i])
    
plt.plot(x_points,y_points, alpha = 1, lw = 1)
plt.axis('off')
plt.gca().set_aspect('equal', adjustable='box')
plt.tight_layout()
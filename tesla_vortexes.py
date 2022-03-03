#https://www.youtube.com/watch?v=6ZrO90AI0c8&ab_channel=Mathologer

import numpy as np
import matplotlib.pyplot as plt


multiplier = 240
modulus = 7417
seed = 1 #fitst number in the sequence
circle = False #if True, prints outer circle
points = False #if True, prints the integers on the circle
circle_resolution = 1000 #number of points making up the circle
alpha = 0.6 #transparency of the graph
lw = 0.01 #line-width of the graph

sequence = [seed,(seed*multiplier)%modulus]

while (sequence[-1] in set(sequence[:-1])) == False:
    
    sequence.append((sequence[-1]*multiplier)%modulus)



coord_x_sequence = np.sin(np.array(sequence)*2*np.pi/modulus)
coord_y_sequence = np.cos(np.array(sequence)*2*np.pi/modulus)

if circle == True:

    circle_x = np.sin(np.array(range(circle_resolution))*2*np.pi/circle_resolution)
    circle_y = np.cos(np.array(range(circle_resolution))*2*np.pi/circle_resolution)

    plt.plot(circle_x,circle_y)
    
if points == True:
    
    coord_x = np.sin(np.array(range(modulus))*2*np.pi/modulus)
    coord_y = np.cos(np.array(range(modulus))*2*np.pi/modulus)
    
    plt.scatter(coord_x,coord_y)

plt.plot(coord_x_sequence,coord_y_sequence, alpha = alpha,lw = lw)
plt.axis('off')
plt.gca().set_aspect('equal', adjustable='box')
plt.tight_layout()



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:38:47 2022

@author: tandeitnik
"""

import numpy as np
import matplotlib.pyplot as plt

###################################################

points = 10000 #number of points calculated
steps = 100 #number of iterations
a = 1.4 #parameter of the Henon map
b = 0.3 #parameter of the Henon map
fps = 1 #frames per second of the video

###################################################

#creates initial points
xLow = np.linspace(-1,1,points)
yLow = np.ones(points)*-0.2

xHigh = np.linspace(-1,1,points)
yHigh = np.ones(points)*0.2

xLeft = np.ones(points)*-1
yLeft = np.linspace(-0.2,0.2,points)

xRight = np.ones(points)*1
yRight = np.linspace(-0.2,0.2,points)

xPoints = np.zeros(4*points)
yPoints = np.zeros(4*points)

xPoints[0:points] = xLow
xPoints[points:2*points] = xRight
xPoints[2*points:3*points] = xHigh
xPoints[3*points:4*points] = xLeft

yPoints[0:points] = yLow
yPoints[points:2*points] = yRight
yPoints[2*points:3*points] = yHigh
yPoints[3*points:4*points] = yLeft

#definition of the Henon map
def henonMap(x,y,a,b):
    
    xNew = y+1-a*x**2
    yNew = b*x
    
    return xNew, yNew

filenames = []
plt.figure(figsize=(8, 8), dpi=80)
figura = plt.scatter(xPoints,yPoints, s = 0.1)
fig = figura.get_figure()


fig.savefig("00.png") 
filenames.append("00.png")

plt.close()

for i in range(1,steps):
    
    xPoints, yPoints = henonMap(xPoints,yPoints,a,b)
    plt.figure(figsize=(8, 8), dpi=80)
    figura = plt.scatter(xPoints,yPoints, s = 0.1)
    fig = figura.get_figure()
    
    if i < 10:
        fig.savefig('0'+str(i)+".png") 
        filenames.append('0'+str(i)+".png")
    else:
        fig.savefig(str(i)+".png") 
        filenames.append(str(i)+".png")
    plt.close()
    

import moviepy.video.io.ImageSequenceClip
import os

image_folder='image_folder_path'


image_files = [os.path.join(image_folder,img)
                for img in sorted(os.listdir(image_folder))
                if img.endswith(".png")]
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile('henonMapEvolution.mp4')
    
            
for filename in set(filenames):
    os.remove(filename)

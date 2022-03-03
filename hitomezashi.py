#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 07:28:17 2022

@author: tandeitnik
"""

#https://www.youtube.com/watch?v=JbfhzlMk2eY&ab_channel=Numberphile

import random
import numpy as np
import matplotlib.pyplot as plt

#square

n_largura = 20
n_altura = 10
borda = True
 
 
# Function to create the
# random binary string
def rand_key(p):
   
    # Variable to store the
    # string
    key1 = ""
 
    # Loop to find the string
    # of desired length
    for i in range(p):
         
        # randint function to generate
        # 0, 1 randomly and converting
        # the result into str
        temp = str(random.randint(0, 1))
 
        # Concatenation the random 0, 1
        # to the final result
        key1 += temp
         
    return(key1)
 
# Driver Code

str_largura = rand_key(n_largura)
str_altura = rand_key(n_altura)


#fazendo as linhas horizontais

count = 0

for digit in str_altura:
    
    for i in range(n_largura):
        
        if digit == '1': #linhas ligam pontos pares a pontos ímpares
        
            if i%2 == 0: #ponto é par, plotar
            
                plt.plot([i,i+1],[count,count],'k')
                
        if digit == '0': #linhas ligam pontos ímpares a pontos pares
        
            if i%2 == 1: #ponto é impar, plotar
            
                plt.plot([i,i+1],[count,count],'k')
                
    count += 1
    
    
#fazendo as linhas verticais

count = 0

for digit in str_largura:
    
    for i in range(n_altura):
        
        if digit == '1': #linhas ligam pontos pares a pontos ímpares
        
            if i%2 == 0: #ponto é par, plotar
            
                plt.plot([count,count],[i,i+1],'k')
                
        if digit == '0': #linhas ligam pontos ímpares a pontos pares
        
            if i%2 == 1: #ponto é impar, plotar
            
                plt.plot([count,count],[i,i+1],'k')
                
    count += 1
        
if borda == True:
    
    plt.plot(range(n_largura+1),np.zeros(n_largura+1),'k') #horizontal inf
    plt.plot(np.ones(n_altura+1)*(n_largura),range(n_altura+1),'k') #vertical direita
    plt.plot(range(n_largura+1),np.ones(n_largura+1)*(n_altura),'k') #horizontal superior
    plt.plot(np.zeros(n_altura+1),range(n_altura+1),'k') #vertical esquerda

plt.axis('off')
plt.gca().set_aspect('equal', adjustable='box')
plt.tight_layout()
        
        
#triangle

height = 20 #how many layers has the triangle
borda = False

str_hoz = rand_key(height-1)
str_right = rand_key(height-1)
str_left = rand_key(height-1)

#fazendo a borda

if borda == True:
    plt.plot([0,height-1],[0,0],'k')
    plt.plot([0,(height-1)/2],[0,(height-1)*np.cos(60*np.pi/180)],'k')
    plt.plot([(height-1)/2,height-1],[(height-1)*np.cos(60*np.pi/180),0],'k')

pontos_layers = []

for i in range(height):
    
    x_coord = np.zeros(height-i)
    
    for j in range(height-i):
        
        if j == 0:
        
            x_coord[j] = 0.5*i
            
        else:
            
            x_coord[j] = x_coord[j-1] + 1
            
    y_coord = np.ones(height-i)*i*np.cos(60*np.pi/180)
    
    pontos_layers.append([x_coord,y_coord])
    
# for i in range(len(pontos_layers)):
    
#     plt.scatter(pontos_layers[i][0],pontos_layers[i][1])


#fazendo as linhas horizontais de baixo para cima

count_layer = 0

for digit in str_hoz:
    
    for i in range(len(pontos_layers[count_layer][0])-1):
        
        if digit == '1': #linhas ligam pontos pares a pontos ímpares
        
            if i%2 == 0: #ponto é par, plotar
                
                plt.plot([pontos_layers[count_layer][0][i],pontos_layers[count_layer][0][i+1]],[pontos_layers[count_layer][1][i],pontos_layers[count_layer][1][i+1]],'k')
                
                
        if digit == '0': #linhas ligam pontos ímpares a pontos pares
        
            if i%2 == 1: #ponto é impar, plotar
            
                plt.plot([pontos_layers[count_layer][0][i],pontos_layers[count_layer][0][i+1]],[pontos_layers[count_layer][1][i],pontos_layers[count_layer][1][i+1]],'k')

    count_layer += 1


pontos_layers = []

for i in range(height):
    
    x_coord = np.zeros(height-i)
    y_coord = np.array(range(height-i))*np.cos(60*np.pi/180)
    
    for j in range(height-i):
        
        if j == 0:
        
            x_coord[j] = i
            
        else:
            
            x_coord[j] = x_coord[j-1] + 0.5
            
    
    pontos_layers.append([x_coord,y_coord])
    
# for i in range(len(pontos_layers)):
    
#     plt.scatter(pontos_layers[i][0],pontos_layers[i][1])



#fazendo as linhas verticais / de baixo para cima

count_layer = 0

for digit in str_right:
    
    for i in range(len(pontos_layers[count_layer][0])-1):
        
        if digit == '1': #linhas ligam pontos pares a pontos ímpares
        
            if i%2 == 0: #ponto é par, plotar
                
                plt.plot([pontos_layers[count_layer][0][i],pontos_layers[count_layer][0][i+1]],[pontos_layers[count_layer][1][i],pontos_layers[count_layer][1][i+1]],'k')
                
                
        if digit == '0': #linhas ligam pontos ímpares a pontos pares
        
            if i%2 == 1: #ponto é impar, plotar
            
                plt.plot([pontos_layers[count_layer][0][i],pontos_layers[count_layer][0][i+1]],[pontos_layers[count_layer][1][i],pontos_layers[count_layer][1][i+1]],'k')

    count_layer += 1
    
    
pontos_layers = []

for i in range(height):
    
    x_coord = np.zeros(height-i)
    y_coord = np.array(range(height-i))*np.cos(60*np.pi/180)
    
    for j in range(height-i):
        
        if j == 0:
        
            x_coord[j] = height-1-i
            
        else:
            
            x_coord[j] = x_coord[j-1] - 0.5
            
    
    pontos_layers.append([x_coord,y_coord])
    
# for i in range(len(pontos_layers)):
    
#     plt.scatter(pontos_layers[i][0],pontos_layers[i][1])

#fazendo as linhas verticais \

count_layer = 0

for digit in str_left:
    
    for i in range(len(pontos_layers[count_layer][0])-1):
        
        if digit == '1': #linhas ligam pontos pares a pontos ímpares
        
            if i%2 == 0: #ponto é par, plotar
                
                plt.plot([pontos_layers[count_layer][0][i],pontos_layers[count_layer][0][i+1]],[pontos_layers[count_layer][1][i],pontos_layers[count_layer][1][i+1]],'k')
                
                
        if digit == '0': #linhas ligam pontos ímpares a pontos pares
        
            if i%2 == 1: #ponto é impar, plotar
            
                plt.plot([pontos_layers[count_layer][0][i],pontos_layers[count_layer][0][i+1]],[pontos_layers[count_layer][1][i],pontos_layers[count_layer][1][i+1]],'k')

    count_layer += 1
    
plt.axis('off')
plt.gca().set_aspect('equal', adjustable='box')
plt.tight_layout()
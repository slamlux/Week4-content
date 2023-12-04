# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:03:59 2023

@author: Administrator
"""


import matplotlib.pyplot as plt
import numpy as np
a=1
b=10
t=0
#the constants
plt.close('all')
coords = np.linspace(-10, 10, 10)#define the limits for x axis
coord = np.linspace(-10, 10, 10)#define the limits for y axis
X,Y = np.meshgrid(coords, coord)
U = Y
V = (b*np.cos(2*t)-a)*X
plt.figure(figsize=(6,6))
plt.gca().set_aspect('equal' ,adjustable='box') #Make plot box square
plt.xlabel('rabbits')
plt.ylabel('foxes')
plt.title('quiver plot and streamlines of an interacting population of rabbits and foxes')
 # plot field as quiver
#plt.streamplot(X,Y,U,V) # plot streamlines of field.
seed_points = np.array([[0.85], [-2.5]])
plt.streamplot(X, Y, U, V, color='b', start_points=seed_points.T)
#plt.plot(seed_points[0],seed_points[1],'bo') #show seeds on graph
#plt.streamplot(X, Y, U, V, start_points=seed_points.T, integration_direction='forward')
#plt.streamplot(X,Y,U,V, density = [0.5, 0.5])
#strm = plt.streamplot(X, Y, U, V, color=np.sqrt(U*U+V*V), linewidth=2, cmap='autumn')
#plt.colorbar(strm.lines)
strm=plt.streamplot(X, Y, U, V, color='grey', cmap='gnuplot')
print(a)

plt.savefig('rabbits-quiver5.png', bbox_inches='tight')#saves the figure 
plt.show()
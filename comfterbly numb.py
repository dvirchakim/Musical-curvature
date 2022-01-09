import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure('comfterbly numb  verse-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[2,0,10,7],[5,4,2,10],[9,7,5,2]  

ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='r')



fig = plt.figure('comfterbly numb chorus -FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[ 5,0,3,10,5,0,3,10,0,3,10,5],[9,4,7,2,9,4,7,2,4,7,2,9],[0,7,10,5,0,7,10,5,7,10,5,0]


ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='y')


plt.show()
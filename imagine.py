import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure('imagine verse-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[3,3,8],[7,7,0],[10,2,4] 

ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='r')



fig = plt.figure('imagine chorus -FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[8,10,3,3,7,7,8,10,3] ,[0,2,7,7,11,11,0,2,7],[4,5,10,2,2,6,4,5,10] 

ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='y')



fig = plt.figure('imagine bridge -FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[8,0,5,8,10,3,10],[0,3,8,0,2,7,2],[4,7,3,4,5,10,8]



ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='b')


plt.show()
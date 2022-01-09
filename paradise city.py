import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure('paradise city verse-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[10,8,3,1],[2,0,7,5],[5,3,10,8]

ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='r')



fig = plt.figure('paradise city chorus-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[3,3,8,3,10],[7,7,0,7,2],[10,10,3,10,5]

ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='y')


plt.show()
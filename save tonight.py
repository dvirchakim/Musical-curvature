import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure('save tonight verse-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[0,8,3,10],[3,0,7,2],[7,3,10,5]

ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='r')



fig = plt.figure('save tonight chorus-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[10,0,8,3],[2,3,0,7],[5,7,3,10]

ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='y')


plt.show()
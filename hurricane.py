import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure('hurricane verse-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[0,8],[3,0],[7,4]

ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='r')



fig = plt.figure('hurricane chorus-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[3,8,10,3,8,5,3,5,3,7,0,8,3,10],[7,0,2,7,0,8,7,8,7,10,3,0,7,2],[10,4,5,10,4,0 ,10,0,10,2,7,4,10,5]



ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='y')


plt.show()
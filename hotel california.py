import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure('hotel california verse-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[0,7,10,5,8,3,5,7],[3,11,2,9,0,7,8,11],[7,2,5,0,3,10,0,2]

ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='r')



fig = plt.figure('hotel california chorus-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[8,3,7,0,8,3,5,7],[0,7,11,3,0,7,8,11],[3,10,2,7,3,10,0,2]

ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='y')


plt.show()
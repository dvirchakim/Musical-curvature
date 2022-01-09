import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure('take me home country roads verse-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[10,7,5,3,10],[2,10,9,7,2],[5,2,0,10,5]


ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='r')



fig = plt.figure('take me home country roads chorus -FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[10,5,7,3,10,5,3,10],[2,9,10,7,2,9,7,2],[5,4 ,2,10,5,0,10,5]



ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='y')


plt.show()
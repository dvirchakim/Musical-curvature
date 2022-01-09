import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure('hallelujah-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[10,7,10,7,3,5,10,5,10,3,5,7,3,5,2,7,3,7,3,10,5,10,5],[2,10,2,10,7,9,2,9,2,7,9,10,7,9,6,10,7,10,7,2,9,2,9],[5,2,5,2,10,0,5,0,5,10,0,2,10,0,9,2,10,2,0,5,0,5,0]

ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='r')


plt.show()
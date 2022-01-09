import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure('never gonnagive you up verse-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[10,0],[2,4],[5,7]


ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='r')



fig = plt.figure('never gonnagive you up chorus -FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[10,0,9,2],[2,4,0,5],[5,7,4,9]


ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='y')


plt.show()
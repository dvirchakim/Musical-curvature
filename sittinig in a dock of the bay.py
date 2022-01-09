import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure('sitting on a dock of the bay  verse-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[ 10,2,3,0],[2,6,7,4],[5,1,10,7]



ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='r')



fig = plt.figure('sitting on a dock of the bay -FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[ 10,7,10,0,10,7],[2,11,2,4,2,11],[5,2,5,7,5,2]




ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='y')


plt.show()
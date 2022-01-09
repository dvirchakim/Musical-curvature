import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure('tears in heaven verse-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[0,7,9,0,5,0,7],[4,11,0,4,9,4,1],[7,2,4,7,0,7,2]

ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='r')



fig = plt.figure('tears in heaven chorus-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[9,4,0,9,2,2,0],[0,8,4,1,5,5,4],[4,11,7,4,9,9,7]

ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='y')


plt.show()
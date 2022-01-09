import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math

fig = plt.figure('Yellow submarine-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[1,5,4,1,6,2,4,5,1,5,4,1,6,2,4,5],[3,7,6,3,1,4,6,7,3,7,6,3,1,4,6,7],[5,2,1,5,3,6,1,2,5,2,1,5,3,6,1,2]

ax.scatter(x,y,z, c='r',s=80)
ax.plot(x,y,z, color='r')

plt.show()

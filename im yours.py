import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure('im yours-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[10,5,7,3],[2,9,10,7],[5,0,2,10]

ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='r')







plt.show()
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure('get back-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[5,10,0,0],[9,2,4,4],[0,5,7,7]

ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='r')


plt.show()
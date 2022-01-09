import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure('shape of you-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[2,7,10,0],[5 ,10,2,4],[9,2,5,7]


ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='r')


plt.show()
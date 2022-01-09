import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure('get back-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[0,0,0,0,5,0,10,5],[4,4,4,4,9,4,2,9],[7,7,7,7,0,7,5,0]

ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='r')


plt.show()
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure('get back-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z= [3,10,0,8,3,8,3,10,3,8,3],[7,2,3,0,7,0,7,2,7,0,7],[10,5,7,4,10,4,10,5,7,4,10]




ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='r')


plt.show()
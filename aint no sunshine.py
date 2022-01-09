import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure('aint no sunshine -FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[0,7,10,0,7,5,0,7, 10,0],[ 3, 10 , 2, 3, 10, 8,3,10,2,3],[ 7,2 ,5,7,2,0,7,2,5,7]

ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='r')


plt.show()
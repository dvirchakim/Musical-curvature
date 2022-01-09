import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure('take on me verse  -FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[ 2, 7, 0 ,5,0],[ 5, 11 , 4,9,4],[ 9,2 ,7,0,7]

ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='r')



fig = plt.figure('take on me chorus -FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[0,7,9,5,0,7,5,7],[4,11,1,9,4, 11, 9,11],[7,2 ,4,0,7,2,0,2]



ax.scatter(x,y,z, c='y',s=10)
ax.plot(x,y,z, color='y')




plt.show()
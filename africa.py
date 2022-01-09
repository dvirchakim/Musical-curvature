import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure('africa verse-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[2,6,11,2,0,4,11,0,11,4],[6,9,2,6,4,7,2,4,2,7],[9,1,6,9,7,11,6,7,6,11]

ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='r')




fig = plt.figure('africa chorus-FullchorDot')
ax = fig.gca(projection='3d')

x,y,z=[9,5,0,7,4,7,9,7,0,11,4],[1,9,4,11,7,11,0,11,4,2,7],[4,0,7,2,11,2,4,2,7,6,11]

ax.scatter(x,y,z, c='r',s=10)
ax.plot(x,y,z, color='y')



plt.show()
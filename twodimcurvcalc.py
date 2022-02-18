import numpy as np
import math

x,y=[1,4,4,1],[4,4,0,0]

def TwoDimCurvCalc(x, y):
 H=[];L=[];vecs=[];antivecs=[];beta=0

 for i in range(len(x)-1):
   H= x[i+1]-x[i]
   L=y[i+1]-y[i]

   vecs.append((H, L))
   antivecs.append((-H,-L))

 for i in range(len(x)-2):

   alfa = np.arccos(np.abs((np.dot(vecs[i],antivecs[i+1])) /  ((np.linalg.norm(vecs[i])) * (np.linalg.norm(antivecs[i+1])))))

   beta += np.rad2deg(alfa)
    
 alfa2=np.arccos((np.dot(vecs[-1], antivecs[0])) /
                       (np.linalg.norm(vecs[-1]) * np.linalg.norm(antivecs[0])))

 beta+=(180-np.rad2deg(alfa2))

 return (beta)

K=TwoDimCurvCalc(x,y)

print(K)
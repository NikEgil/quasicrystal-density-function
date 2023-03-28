from math import *
import numpy as np
import matplotlib.pyplot as plt

n=300000

th= (sqrt(5)+1)/2
nu = pi/sqrt(th+2)
b=nu*np.matrix([
    [th,0,1],
    [th,0,-1],
    [1,th,0],
    [0,1,th],
    [0,-1,th],
    [1,-th,0]])
q=np.zeros((n,3))



for i in range (len(b)):
    q[i]=b[i]


p=0
t=0
for i in range(len(b),n):

    q[i]=b[p]+q[t]
    p+=1
    if p>=len(b): 
        p=0
        t+=1



print(len(q))
q=np.unique(q, axis = 0)
print(len(q))
w=np.zeros((len(q),3))

s=0
for i in range(len(q)):
    if 5<q[i][0]<15 and -5<q[i][1]<5 and 0<q[i][2]<10:
        w[s]=q[i]
        s+=1




x=q[:,0]
y=q[:,1]
z=q[:,2]
x1=w[:,0]
y1=w[:,1]
z1=w[:,2]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x1,y1,z1)
#ax.scatter(x,y,z)
ax.grid(False)
plt.show()






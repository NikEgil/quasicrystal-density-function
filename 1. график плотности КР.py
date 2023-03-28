from math import *

import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_subplot()

n=40

x=np.arange(-n,n,0.1)


q=np.zeros((len(x),len(x)))


for i in range(len(x)):
    for j in range(len(x)):
        #что-то красивое
        #q[i][j]=cos(x[i])+cos(x[j])+cos(x[i]/x[j])

        #квадратики
      q[i][j]=cos(x[i])+cos(x[j])+cos((x[i]+x[j])/sqrt(2))+cos((x[i]-x[j])/sqrt(2))

        #квадратики повернутые
      #  q[i][j]=cos(x[i])+cos(x[j])+cos(x[i]+x[j])+cos(x[i]-x[j])+cos(3*x[i]+x[j])+cos(x[i]-3*x[j])

c = ax.pcolor(q)
x_left, x_right=ax.get_xlim()
y_low, y_high=ax.get_ylim()
ax.set_aspect(1)
plt.show()
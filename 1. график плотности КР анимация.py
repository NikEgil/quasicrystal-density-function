from math import *

import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_subplot()

n=30

x=np.arange(-n,n,0.1)
q=np.zeros((len(x),len(x)))

z=0.005


for t in range(20):
    name='fig'+str(t)
    ax.clear()
    for i in range(len(x)):
      for j in range(len(x)):
        q[i][j]=cos(x[i])+cos(x[j])+cos((x[i]+x[j])/z)+cos((x[i]-x[j])/z)
    c = ax.pcolor(q)
    x_left, x_right=ax.get_xlim()
    y_low, y_high=ax.get_ylim()
    ax.set_aspect(1)
    ax.set_title(f"{t}")
    #для сохранения картинок раскоментить
    #plt.savefig(name, dpi=400)
    #для анимации раскоментить в скобках задержка перед выводом
    plt.pause(0.5)
    z+=0.005
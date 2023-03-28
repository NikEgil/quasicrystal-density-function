from operator import le
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
n=30
# Make data.
X = np.arange(-n, n, np.pi/30)
Y = np.arange(-n, n, np.pi/30)

X, Y = np.meshgrid(X, Y)
Z=np.cos(Y)+np.cos(X)+np.cos((X+Y)*2/3)+np.cos((X-Y)*2/3)


surf = ax.plot_surface(X,Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-3.01, 3.01)
#ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
#ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
#fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
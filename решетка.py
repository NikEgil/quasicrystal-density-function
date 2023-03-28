from math import*
import numpy as np
import matplotlib.pyplot as plt

fig, ax=plt.subplots()
ax.spines[["left", "bottom"]].set_position(("data", 0))
ax.spines[["top", "right"]].set_visible(False)

#основныелинии
x=np.arange(-5, 5.01, 0.01)
tg=pi/180
ax.plot(x, tan(65*tg)*x, color='blue', linewidth=1)
ax.plot(x, tan(155*tg)*x, color='blue', linewidth=1)
ax.axis([-5.5, 5.5, -5.5, 5.5])

#сетка
ax.grid(False)
ax.hlines(np.arange(-5, 5.1, 1), np.linspace(-5, -5, 11), np.linspace(5, 5, 11), linewidth=0.5)
ax.vlines(np.arange(-5, 5.1, 1), np.linspace(-5, -5, 11), np.linspace(5, 5, 11), linewidth=0.5)


#линии
k=np.arange(-0.6, 0.61, 0.01)

for i in range(-5, 6):
    for j in range(-10, 11):
        ax.plot(k+i, tan(155*tg)*(k)+j, color='black', linewidth=0.5)

#точки
xt=(-2.450929692, -2.272323497, -1.889301276, -1.506279054, -1.327672859, -0.9446506377, -0.5616284164, -0.3830222214, 0, 0.3830222214, 0.5616284164, 0.9446506377, 1.327672859, 1.506279054, 1.889301276, 2.272323497, 2.450929692)
yt=(-5.256035690, -4.873013468, -4.051619664, -3.230225858, -2.847203636, -2.025809831, -1.204416027, -0.8213938051, 0, 0.8213938051, 1.204416027, 2.025809831, 2.847203636, 3.230225858, 4.051619664, 4.873013468, 5.256035690)

filled_marker_style = dict(marker='o', linestyle=':', markersize=15,
                           color='darkgrey',
                           markerfacecolor='tab:blue',
                           markerfacecoloralt='lightsteelblue',
                           markeredgecolor='brown')

ax.scatter(xt,yt,marker='o', s=20,c='red')


#мастабирование
x_left, x_right=ax.get_xlim()
y_low, y_high=ax.get_ylim()
ax.set_aspect(1)

plt.show()
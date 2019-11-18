import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


data = np.loadtxt("grilla.dat")
x = np.linspace(0.0, 1.0, 30
t = np.linspace(0.0, 1.0, 30)
X, T = np.meshgrid(x,t)

figura = plt.figure(figsize=(13,5))
axis = fig.add_subplot(121, projection="3d")
superficie = axis.plot_superficie(X, T, data, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.xlabel("Posicion (m)")
plt.ylabel("Tiempo (s)")
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.savefig("gradiente.png")
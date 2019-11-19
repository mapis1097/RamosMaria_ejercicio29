import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

data = np.loadtxt('grilla.dat')
x = np.linspace(-1,1,data.shape[1])
t = np.linspace(0,1,data.shape[0])

X,T = np.meshgrid(x,t)

figura = plt.figure()
axis = figura.gca(projection='3d')
surf = axis.plot_surface(X,T,data)
plt.xlabel('Espacio')
plt.ylabel('Tiempo')
plt.savefig('grafica29.png')
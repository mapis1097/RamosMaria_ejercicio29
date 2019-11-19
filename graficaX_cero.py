import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

data = np.loadtxt('grilla.dat')
t = np.linspace(0,1,data.shape[0])

plt.plot(t,data[:,15])
plt.savefig('grafica_X_cero.png')

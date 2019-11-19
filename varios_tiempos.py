import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

data = np.loadtxt('grilla.dat')
x = np.linspace(-1,1,data.shape[1])

tiempos = [0,110,220,330,440,560,670,780]
for i in tiempos:
    plt.plot(x,data[i,:], label = i)
plt.legend()
plt.savefig('varios_tiempos.png')

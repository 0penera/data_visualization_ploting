import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

val = np.linspace(-1, 1, 100)
x, y = np.meshgrid(val, val)
z = x**2 + x*y

cs = plt.contour(x, y, z, levels=20)
plt.clabel(cs, fontsize=7)
plt.show()
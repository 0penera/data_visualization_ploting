import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

val = np.linspace(-1, 1, 100)
x, y = np.meshgrid(val, val)
z = x**2 + x*y

plt.figure(figsize=(7, 5), layout="constrained")
plt.contourf(x, y ,z, levels=1000, vmax=1.9,
             cmap="plasma")
plt.colorbar(label="asd")
plt.show()
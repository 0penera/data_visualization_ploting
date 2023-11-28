import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

val = np.linspace(-1, 1, 100)
x, y = np.meshgrid(val, val)
z = x**2 + x*y
u = 2 + x - y**2
v = 1 + x - y**2
speed = np.sqrt(u**2, v**2)

fig, axes = plt.subplots(2, 2, figsize=(7, 7), layout="constrained")
axes[0, 0].streamplot(x, y, u, v)
axes[0, 1].streamplot(x, y, u, v, color=speed)
lw = 5*speed / speed.max()
axes[1, 0].streamplot(x, y, u, v, linewidth=lw)
seedpoint = np.array([[0, 1], [1, 0]])
axes[1, 1].streamplot(x, y, u, v, start_points=seedpoint)
plt.show()
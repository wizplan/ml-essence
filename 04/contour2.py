import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return x**2 + y**2 / 4

x = np.linspace(-5, 5, 300)
y = np.linspace(-5, 5, 300)
xmesh, ymesh = np.meshgrid(x, y)
z = f(xmesh, ymesh)

colors = ["0.1", "0.3", "0.5", "0.7"]
levels = [1, 2, 3, 4, 5]
plt.contourf(x, y, z, colors=colors, levels=levels)
plt.show()
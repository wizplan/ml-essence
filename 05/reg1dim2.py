import numpy as np
import matplotlib.pyplot as plt

def reg1dim2(x, y):
    n = len(x)
    a = ((np.dot(x, y) - y.sum() * x.sum() / n) / # ❶
         ((x**2).sum() - x.sum()**2 / n))
    b = (y.sum() - a * x.sum()) / n # ❷
    return a, b

x = np.array([1, 2, 4, 6, 7])
y = np.array([1, 3, 3, 5, 4])
a, b = reg1dim2(x, y)

plt.scatter(x, y, color="k")
xmax = x.max()
plt.plot([0, xmax], [b, a * xmax + b], color="k")
plt.show()
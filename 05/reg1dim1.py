import numpy as np
import matplotlib.pyplot as plt

def reg1dim1(x, y):  # ❶
    a = np.dot(x, y) / (x**2).sum()  # ❷
    return a

x = np.array([1, 2, 4, 6, 7])
y = np.array([1, 3, 3, 5, 4])
a = reg1dim1(x, y)

plt.scatter(x, y, color="k")
xmax = x.max()
plt.plot([0, xmax], [0, a*xmax], color="k")
plt.show()
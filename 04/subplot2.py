import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 300)
y = x**2

fig, ax = plt.subplots()
ax.plot(x, y, color="r")
plt.show()
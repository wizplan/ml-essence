import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 300)  # ❶
y = x**2  # ❷

plt.plot(x, y, color="r")
plt.show()
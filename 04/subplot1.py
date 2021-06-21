import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 300)  # ❶
sin_x = np.sin(x)
cos_x = np.cos(x)

fig, axes = plt.subplots(2, 1)  # ❷
axes[0].set_ylim(-1.5, 1.5)  # ❸
axes[1].set_ylim(-1.5, 1.5)
axes[0].plot(x, sin_x, color="r")  # ❹
axes[1].plot(x, cos_x, color="k")

plt.show()
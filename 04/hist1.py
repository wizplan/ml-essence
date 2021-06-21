import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
l = []
for _ in range(1000):  # ❶
    l.append(np.random.randint(1, 7, size=10).sum()) 

plt.hist(l, 20, color="gray")  # ❷
plt.show()
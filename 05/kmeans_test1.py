import numpy as np
import matplotlib.pyplot as plt
import kmeans

np.random.seed(0)
points1 = np.random.randn(50, 2)
points2 = np.random.randn(50, 2) + np.array([5, 0])  # ❶
points3 = np.random.randn(50, 2) + np.array([5, 5])

points = np.r_[points1, points2, points3]
np.random.shuffle(points)

model = kmeans.KMeans(3)
model.fit(points)

markers = ["+", "*", "o"]  # ❷

for i in range(3):
    p = points[model.labels_ == i, :]  # ❸
    plt.scatter(p[:, 0], p[:, 1], color="k", marker=markers[i])  # ❹

plt.show()
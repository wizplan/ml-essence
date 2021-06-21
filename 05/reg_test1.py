import linearreg
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

n = 100
scale = 10

np.random.seed(0)
X = np.random.random((n, 2)) * scale  # ❶
w0 = 1
w1 = 2
w2 = 3
y = w0 + w1 * X[:, 0] + w2 * X[:, 1] + np.random.randn(n)  # ❷

model = linearreg.LinearRegression()
model.fit(X, y)
print("계수: ", model.w_) # ❸
print("(1, 1)에 대한 예측값: ", model.predict(np.array([1, 1])))  # ❹

xmesh, ymesh = np.meshgrid(np.linspace(0, scale, 20), # ❺
                           np.linspace(0, scale, 20))
zmesh = (model.w_[0] + model.w_[1] * xmesh.ravel() +
         model.w_[2] * ymesh.ravel()).reshape(xmesh.shape)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], y, color="k")
ax.plot_wireframe(xmesh, ymesh, zmesh, color="r")
plt.show()
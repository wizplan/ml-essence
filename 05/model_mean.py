import numpy as np
import matplotlib.pyplot as plt
import warnings
import polyreg
import linearreg

def f(x):
    return 1 / (1 + x)

def sample(n):
    x = np.random.random(n) * 5
    y = f(x)
    return x, y

xx = np.arange(0, 5, 0.01)
np.random.seed(0)
y_poly_sum = np.zeros(len(xx))
y_lin_sum = np.zeros(len(xx))
n = 100000
warnings.filterwarnings("ignore")

for _ in range(n):
    x, y = sample(5)
    poly = polyreg.PolynomialRegression(4)
    poly.fit(x, y)
    lin = linearreg.LinearRegression()
    lin.fit(x, y)
    y_poly = poly.predict(xx)
    y_poly_sum += y_poly
    y_lin = lin.predict(xx.reshape(-1, 1))
    y_lin_sum += y_lin

plt.plot(xx, f(xx), label="truth", color="k", linestyle="solid")
plt.plot(xx, y_poly_sum / n, label="polynomial reg.", color="k", linestyle="dotted")
plt.plot(xx, y_lin_sum / n, label="linear reg.", color="k", linestyle="dashed")
plt.legend()
plt.show()
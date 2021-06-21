import numpy as np

def softplus(x):
    return max(0, x) + np.log(1 + np.exp(-abs(x)))
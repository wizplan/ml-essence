import numpy as np

def qeq(a, b, c):
    d = np.sqrt(b**2 - 4 * a * c)
    return ((-b + d) / (2 * a), (-b - d) / (2 * a))
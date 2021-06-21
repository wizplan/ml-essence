import numpy as np
from scipy.sparse.linalg import svds

class PCA:
    def __init__(self, n_components, tol=0.0, random_seed=0):
        self.n_components = n_components
        self.tol = tol
        self.random_state_ = np.random.RandomState(random_seed)

    def fit(self, X):
        v0 = self.random_state_.randn(min(X.shape))  # ❶
        xbar = X.mean(axis=0)  # ❷
        Y = X - xbar  # ❸
        S = np.dot(Y.T, Y)  # ❹
        U, Sigma, VT = svds(S, k=self.n_components, tol=self.tol, v0=v0)
        self.VT_ = VT[::-1, :]

    def transform(self, X):
        return self.VT_.dot(X.T).T
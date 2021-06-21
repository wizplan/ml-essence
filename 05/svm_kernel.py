import numpy as np
from operator import itemgetter

class RBFKernel:
    def __init__(self, X, sigma):
        self.sigma2 = sigma**2
        self.X = X
        self.values_ = np.empty((X.shape[0], X.shape[0]))

    def value(self, i, j):
        return np.exp(-((self.X[i, :] - self.X[j, :])**2).sum() / (2*self.sigma2))

    def eval(self, Z, s):
        return np.exp(-((self.X[s, np.newaxis, :] - Z[np.newaxis, :, :])**2).sum(axis=2) / (2*self.sigma2))

class SVC:
    def __init__(self, C=1., sigma=1., max_iter=10000):
        self.C = C
        self.sigma = sigma
        self.max_iter = max_iter

    def fit(self, X, y, selections=None):
        a = np.zeros(X.shape[0])
        ay = 0
        kernel = RBFKernel(X, self.sigma)
        indices = np.arange(X.shape[0])
        for _ in range(self.max_iter):
            s = a != 0.
            ydf = y * (1 - y*np.dot(a[s]*y[s], kernel.eval(X, s)).T)
            iydf = np.c_[indices, ydf]
            i = int(min(iydf[((a > 0) & (y > 0)) | ((a < self.C) & (y < 0))], key=itemgetter(1))[0])
            j = int(max(iydf[((a > 0) & (y < 0)) | ((a < self.C) & (y > 0))], key=itemgetter(1))[0])
            if ydf[i] >= ydf[j]:
                break
            ay2 = ay - y[i]*a[i] - y[j]*a[j]
            kii = kernel.value(i, i)
            kij = kernel.value(i, j)
            kjj = kernel.value(j, j)
            s = a != 0.
            s[i] = False
            s[j] = False
            kxi = kernel.eval(X[i, :].reshape(1, -1), s).ravel()
            kxj = kernel.eval(X[j, :].reshape(1, -1), s).ravel()
            ai = ((1 - y[i]*y[j] + y[i]*((kij - kjj)*ay2 - (a[s]*y[s]*(kxi-kxj)).sum())) / (kii + kjj - 2*kij))
            if ai < 0:
                ai = 0
            elif ai > self.C:
                ai = self.C
            aj = (-ai*y[i] - ay2)*y[j]
            if aj < 0:
                aj = 0
                ai = (-aj*y[j] - ay2)*y[i]
            elif aj > self.C:
                aj = self.C
                ai = (-aj*y[j] - ay2)*y[i]
            ay += y[i] * (ai-a[i]) + y[j] * (aj-a[j])
            if ai == a[i]:
                break
            a[i] = ai
            a[j] = aj
        self.a_ = a
        self.y_ = y
        self.kernel_ = kernel
        s = a != 0.
        self.w0_ = (y[s] - np.dot(a[s]*y[s], kernel.eval(X[s], s))).sum() / s.sum()
        with open("svm.log", "w") as fp:
            print(a, file=fp)

    def predict(self, X):
        s = self.a_ != 0.
        return np.sign(self.w0_ + np.dot(self.a_[s]*self.y_[s], self.kernel_.eval(X, s)))
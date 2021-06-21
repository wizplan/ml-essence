import numpy as np
from operator import itemgetter

class SVC:
    def fit(self, X, y, selections=None):
        a = np.zeros(X.shape[0])  # ❶
        ay = 0
        ayx = np.zeros(X.shape[1])
        yx = y.reshape(-1, 1)*X
        indices = np.arange(X.shape[0])
        while True:
            ydf = y*(1-np.dot(yx, ayx.T))  # ❸
            iydf = np.c_[indices, ydf]
            i = int(min(iydf[(y < 0) | (a > 0)], key=itemgetter(1))[0])  # ❹
            j = int(max(iydf[(y > 0) | (a > 0)], key=itemgetter(1))[0])
            if ydf[i] >= ydf[j]:
                break
            ay2 = ay - y[i]*a[i] - y[j]*a[j]  # ❷
            ayx2 = ayx - y[i]*a[i]*X[i, :] - y[j]*a[j]*X[j, :]
            ai = ((1-y[i]*y[j] + y[i]*np.dot(X[i, :] - X[j, :], X[j, :]*ay2 - ayx2))  # ❺
                  / ((X[i] - X[j])**2).sum())
            if ai < 0:
                ai = 0
            aj = (-ai * y[i] - ay2) * y[j]  # ❻
            if aj < 0:
                aj = 0
            ai = (-aj*y[j] - ay2)*y[i]
            ay += y[i]*(ai - a[i]) + y[j]*(aj - a[j])
            ayx += y[i]*(ai - a[i])*X[i, :] + y[j]*(aj - a[j])*X[j, :]
            if ai == a[i]:
                break
            a[i] = ai
            a[j] = aj
        self.a_ = a
        ind = a != 0.
        self.w_ = ((a[ind] * y[ind]).reshape(-1, 1) * X[ind, :]).sum(axis=0)
        self.w0_ = (y[ind] - np.dot(X[ind, :], self.w_)).sum() / ind.sum()

    def predict(self, X):
        return np.sign(self.w0_ + np.dot(X, self.w_))
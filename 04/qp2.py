import numpy as np
import cvxopt

P = cvxopt.matrix(np.array([[2, 1], [1, 2]], dtype=np.float64))
q = cvxopt.matrix(np.array([2, 4], dtype=np.float64))
A = cvxopt.matrix(np.array([[1, 1]], dtype=np.float64))
b = cvxopt.matrix(np.array([0], dtype=np.float64))

sol = cvxopt.solvers.qp(P, q, A=A, b=b)

print(np.array(sol["x"]))
print(np.array(sol["primal objective"]))
import numpy as np
import cvxopt

P = cvxopt.matrix(np.array([[2, 1], [1, 2]], dtype=np.float64))  # ❶
q = cvxopt.matrix(np.array([2, 4], dtype=np.float64))

sol = cvxopt.solvers.qp(P, q)  # ❷

print(np.array(sol["x"]))
print(np.array(sol["primal objective"]))
import numpy as np
# task 1
matrix_1 = np.array([[-1, -6], [2, 6]])
w, v = np.linalg.eig(matrix_1)
print(f"совственные значения:\n {w}")
print(f"собственные векторы:\n {v}")

# task 2
matrix_2 = np.array([[-1, 0], [0, -1]])
w, v = np.linalg.eig(matrix_2)
print(f"совственные значения:\n {w}")
print(f"собственные векторы:\n {v}")
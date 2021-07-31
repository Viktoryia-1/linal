import numpy as np
matrix = np.array([[1, 2, 0], [0, 0, 5], [3, -4, 4],[1, 6, 5], [0, 1, 0]])
U, s, W = np.linalg.svd(matrix)
V = W.T
D = np.zeros_like(matrix)
D[np.diag_indices(min(matrix.shape))] = s
print(f"Матрица U \n {U}")
print(f"Матрица D \n {D}")
print(f"Матрица V \n {V}")
print(f"Норма Фробениуса {np.linalg.norm(matrix,ord='fro')}")

sum = 0
for el in D:
    for i in el:
        i = i ** 2
        sum += i

print(f"Норма Фробениуса для матрицы D перебором в цикле {sum ** (1/2)}")
print(f"Норма Фробениуса для матрицы D {np.linalg.norm(D,ord='fro')}")

sum_2 = 0
for el in matrix:
    for i in el:
        i = i ** 2
        sum_2 += i

print(f"Норма Фробениуса для исходной матрицы перебором в цикле {sum_2 ** (1/2)}")
print(f"Евклидова норма для матрицы D: {D[0][0]}")
print(f"Евклидова норма исходной матрицы {np.linalg.norm(matrix,2)}")
print(f"Евклидова норма {s[0]}")
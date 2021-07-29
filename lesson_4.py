import numpy as np

# task 3
small_matrix = np.array([[1, 3, -2, 4], [0, 5, 0, 1], [0, 0, 3, 0], [0, 0, 0, 2]])
small_rank = np.linalg.matrix_rank(small_matrix)
big_matrix = np.array([[1, 3, -2, 4, 3], [0, 5, 0, 1, 2], [0, 0, 3, 0, 4], [0, 0, 0, 2, 1]])
big_rank = np.linalg.matrix_rank(big_matrix)

if small_rank == big_rank:
    if len(small_matrix[0]) == small_rank:
        print("Система имеет единственное решение")
    else:
        print("Система имеет бесконечное множество решений")
else:
    print("Система несовместна")
# task 5
rate_matrix = [[2, -1, 5], [1, 1, -3], [2, 4, 1]]
b_value = [10, -2, 1]

first = rate_matrix.copy()
first[0][0] = b_value[0]
first[1][0] = b_value[1]
first[2][0] = b_value[2]
print(first)

rate_matrix = [[2, -1, 5], [1, 1, -3], [2, 4, 1]]
second = rate_matrix.copy()
second[0][1] = b_value[0]
second[1][1] = b_value[1]
second[2][1] = b_value[2]
print(second)

rate_matrix = [[2, -1, 5], [1, 1, -3], [2, 4, 1]]
third = rate_matrix.copy()
third[0][2] = b_value[0]
third[1][2] = b_value[1]
third[2][2] = b_value[2]
print(third)
rate_matrix = np.array(rate_matrix)
first = np.array(first)
second = np.array(second)
third = np.array(third)

x_1 = np.linalg.det(first) / np.linalg.det(rate_matrix)
x_2 = np.linalg.det(second) / np.linalg.det(rate_matrix)
x_3 = np.linalg.det(third) / np.linalg.det(rate_matrix)
print(x_1, x_2, x_3)










import numpy as np
# task 2
matrix_1 = np.array([[1, -2], [3, 0]])
matrix_2 = np.array([[4, -1], [0, 5]])
print(f"Сумма матриц \n {matrix_1 + matrix_2}")
print(f"Произведение матриц \n {matrix_1 @ matrix_2}")

# task 3
m_1 = np.array([[1, 7], [3, -6]])
k_1 = 3
m_2 = np.array([[0, 5], [2, -1]])
k_2 = 2
m_3 = np.array([[2, -4], [1, 1]])
k_3 = 4
result = m_1 * k_1 - m_2 * k_2 + m_3 * k_3
print(f"Итоговая матрица \n {result}")

# task 4
normal_matrix = np.array([[4, 1], [5, -2], [2, 3]])
trans_matrix = normal_matrix.T
print(f"Транспонированная матрица \n {trans_matrix}")
print(f"Произведение матрицы с транспонированной \n {normal_matrix.dot(trans_matrix)}")
print(f"Произведение транспонированной с базовой \n {trans_matrix @ normal_matrix}")

# part 2
# task 1
first_matrix = np.array([[4, 2, 3], [0, 5, 1], [0, 0, 9]])
second_matrix = np.array([[1,2,3], [4, 5, 6], [7, 8, 9]])
print(f"Определитель первой матрицы: {np.linalg.det(first_matrix)} \n"
      f"Определитель второй матрицы: {np.linalg.det(second_matrix)}")

# task 3
singular_matrix = np.array([[-2, 7, -3], [4, -14, 6], [-3, 7, 13]])
print(f"Определитель матрицы: {np.linalg.det(singular_matrix)}")
# Определитель матрицы равен 0, вторую строку матрицы можно выразить через первую, умножив ту на 2
# т.е они линейно зависимы, следовательно, данная матрица является вырожденной.

# task 4
find_rank_1 = np.array([[1, 2, 3], [1, 1, 1], [2, 3, 4]])
find_rank_2 = np.array([[0, 0, 2, 1], [0, 0, 2, 2], [0, 0, 4, 3], [2, 3, 5, 6]])
print(f"Ранг первой матрицы:{np.linalg.matrix_rank(find_rank_1)} \n"
      f"Ранг второй матрицы:{np.linalg.matrix_rank(find_rank_2)}"
      f"Определитель матрицы два равен {np.linalg.det(find_rank_2)}")

# task 5 *

mat_1 = [[1, 2], [5, 8], [3, 6]]
mat_2 = [[2, 4, 6], [3, 5, 8]]
result_line = []

for el in mat_1:
    if len(mat_1[0]) == len(mat_2):
       el = [mat_1[0][0] * mat_2[0][0] + mat_1[0][1] * mat_2[1][0]] + \
            [mat_1[0][0] * mat_2[0][1] + mat_1[0][1] * mat_2[1][1]] + \
            [mat_1[0][0] * mat_2[0][2] + mat_1[0][1] * mat_2[1][2]]
       result_line.append(el)
       el_2 = [mat_1[1][0] * mat_2[0][0] + mat_1[1][1] * mat_2[1][0]] + \
            [mat_1[1][0] * mat_2[0][1] + mat_1[1][1] * mat_2[1][1]] + \
            [mat_1[1][0] * mat_2[0][2] + mat_1[1][1] * mat_2[1][2]]
       result_line.append(el_2)

       el_3 = [mat_1[2][0] * mat_2[0][0] + mat_1[2][1] * mat_2[1][0]] + \
            [mat_1[2][0] * mat_2[0][1] + mat_1[2][1] * mat_2[1][1]] + \
            [mat_1[2][0] * mat_2[0][2] + mat_1[2][1] * mat_2[1][2]]
       result_line.append(el_3)

result_matrix = result_line[:3]
print(result_matrix)

a = np.array(mat_1)
b = np.array(mat_2)
print(a @ b)

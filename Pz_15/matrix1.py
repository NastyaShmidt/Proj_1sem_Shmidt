# Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.


import random

n = int(input('Количество столбцов: '))
m = int(input('Количество строк: '))
matrix = [[random.randint(1, 20) for x in range(n)]for y in range(m)]
print()
print('Исходная матрица:')
for q in matrix:
    print(q)
print()
for i in range(m):
    for j in range(n):
        if matrix[i][j] > 10:
            matrix[i][j] = 0
print('Матрица после замены:')
for q in matrix:
    print(q)
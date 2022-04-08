# В квадратной матрице все элементы, не лежащие на главной диагонали
# увеличить в 2 раза.


import random

n = int(input("Количество строк и столбцов: "))
m = n
matrix = [[random.randrange(1, 10) for x in range(n)] for y in range(m)]
print()
print("Исходная матрица:")
for i in matrix:
    print(i)
print()
for i in range(m):
    for j in range(n):
        if [i] != [j]:
            matrix[i][j] = matrix[i][j] * 2
print('Матрица после замены:')
for i in matrix:
    print(i)
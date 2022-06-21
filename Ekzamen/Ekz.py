# 1 ВАРИАНТ (1,2)
# Перенести в новую матрицу Matr1 элементы, которые не находятся в первых и
# последних сроках и столбцах матрицы Matr2 произвольного размера.

import numpy
from numpy import *

matr2 = array([[18, 20, 22, 17], [11, 18, 21, 18], [18, 17, 23, 22], [12, 22, 20, 18]])
print('Исходная матрица:')
for i in matr2:
    print(*i)
matr2 = delete(matr2, [0], 0)
matr2 = delete(matr2, [-1], 0)
matr2 = delete(matr2, s_[0], 1)
matr2 = delete(matr2, s_[-1], 1)
matr1 = matr2
print('Полученная матрица:')
for i in matr1:
    print(*i)

# 2 Возвести в квадрат отрицательные числа
from random import randint

width, heigth = int(input('Введите ширину матрицы: ')), int(input('Введите длину матрицы: '))

matrix = [[randint(-3, 3) for j in range(width)] for i in range(heigth)]
print('До:', matrix)

math_pow = lambda value: value < 0 and pow(value, 2)

for k, v in enumerate(matrix):
    for k1, v1 in enumerate(v):
    res = math_pow(v1)
if res:
    matrix[k][k1] = res

print('После', matrix)

# 2 ВАРИАНТ (3,4)
# В матрице найти минимальный и максимальные элементы.
# В матрице найти сумму отрицательных элементов в первой трети матрицы.

n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
min = [0, 0]
max = [0, 0]
for i in range(n):
    for j in range(len(matrix[0])):
        if matrix[i][j] < matrix[min[0]][min[1]]:
            min = [i, j]
        elif matrix[i][j] > matrix[max[0]][max[1]]:
            max = [i, j]
print(matrix[min[0]][min[1]], matrix[max[0]][max[1]])

n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
summ = 0
for i in range(int(round(len(matrix) / 3, 0))):
    for j in range(len(matrix[i])):
        if matrix[i][j] < 0:
            summ += matrix[i][j]
print(summ)

# 4 ВАРИАНТ(7,8)
# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.
# Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.

import random

i, j = 3, 3
mat = [[random.randrange(1, 15) for x in range(i)] for y in range(j)]
print('Первоночальная матрица \n', mat)
mat[0][1] = mat[0][1] * 2
mat[2][0] = mat[2][0] * 2
mat[2][1] = mat[2][1] * 2
mat[1][0] = mat[1][0] * 2
mat[0][2] = mat[0][2] * 2
mat[1][2] = mat[1][2] * 2

print('Матрица после вычислиений \n', mat)

import random

i, j = 3, 3
mat = [[random.randrange(-10, 15) for x in range(i)] for y in range(j)]
print(mat)
a = 0
for n in mat:
    for b in n:
        if b > 0:
            a += 1
if a > 1:
    print('TRUE')
else:
    print('FALSE')

# 5 ВАРИАНТ(9,10)
# В матрице элементы второго столбца возвести в квадрат.
# Сгенерировать матрицу, в которой нечетные элементы заменяются на 0.

import random

row = int(input("Введите количество строк: "))
column = int(input("Введите количество столбцов (минимум 3): "))
matrix = [[random.randint(-90, 90) for i in range(column)] for j in range(row)]
print("Матрица: ", matrix)
s = [matrix[j][1] * matrix[j][1] for j in range(row)]
a = [matrix[j].insert(1, s[j]) for j in range(row)]
b = [matrix[j].pop(2) for j in range(row)]
print(matrix)

import random

s = []
row = int(input("Введите количество строк: "))
column = int(input("Введите количество столбцов (минимум 3): "))
matrix = [[random.randint(-90, 90) for i in range(column)] for j in range(row)]
print(matrix)
s = [[0 for i in range(1)] for j in range(row)]
[[s[j].append(matrix[j][i]) if matrix[j][i] % 2 == 0 else s[j].append(0) for i in range(column)] for j in range(row)]
[[s[j].pop(0) for i in range(1)] for j in range(row)]
print(s)

# 7 ВАРИАНТ(13,14)
# В матрице элементы строки N (N задать с клавиатуры) увеличить на 3.
# В матрице элементы последнего столбца заменить на -1.

import random

n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
N = int(input('Введите номер строки: '))
matrix = [[random.randint(1, 10) for j in range(m)] for i in range(n)]
print('Исходная матрица: ')

for i in range(n):
    print(matrix[i])

matrix = [[matrix[i][j] + 3 if N == i else matrix[i][j] for j in range(m)] for i in range(n)]
print('Конечная: ')

for i in range(n):
    print(matrix[i])

import random

n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
matrix = [[random.randint(1, 10) for j in range(m)] for i in range(n)]
print('Исходная матрица: ')

for i in range(n):
    print(matrix[i])

matrix = [[-1 if j == m - 1 else matrix[i][j] for j in range(m)] for i in range(n)]
print('Конечная: ')

for i in range(n):
    print(matrix[i])

# 8 ВАРИАНТ(15,16)
# В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза.
# В матрице элементы последней строки заменить на 0.

import random

print('Введите количество строк и столбцов от 1 до 10.')
i, j = int(input('Столбцы: ')), int(input('Строки: '))
mat = [[random.randint(1, 10) for x in range(i)] for y in range(j)]

for i in mat:
    print(i)

n = int(input('Выберите столбец: '))

for i in range(j):
    mat[i][n - 1] *= 2

for i in mat:
    print(i)

import random

print('Введите количество строк и столбцов от 1 до 10.')
a, b = int(input('Столбцы: ')), int(input('Строки: '))
mat = [[random.randint(1, 10) for x in range(a)] for y in range(b)]

for i in range(a):
    mat[b - 1][i] = 0

for i in mat:
    print(i)

# 9 ВАРИАНТ (17,18)
# В матрице элементы второго столбца заменить элементами из одномерного
# динамического массива соответствующей размерности.
# В матрице найти среднее арифметическое положительных элементов, кратных 3.

import numpy as p
import random

i, j = 4, 4
matrix = p.matrix([[random.randrange(0, 10) for x in range(i)] for y in range(j)])
print("Матрица до изменения : \n", matrix)

mas = [random.randrange(0, 10) for x in range(i)]
print("Одномерный массив :", mas)

o = 0

while o < j:
    matrix[o, 1] = mas[o]
    o += 1

print("Матрица после изменения : \n", matrix)

# В матрице найти среднее арифметическое положительных элементов, кратных 3

import random

i, j = 3, 3
matrix = [[random.randrange(-10, 10) for x in range(i)] for y in range(j)]
print("Матрица имеет вид : ")
for i in matrix:
    print(i)

sum = 0
kol = 0

for n in matrix:
    for b in n:
        if b > 0:
            if b % 3 == 0:
                sum += b
                kol += 1

print("Сумма элементов кратных 3 =", sum)
print("Количество элементов кратных 3 =", kol)
if kol == 0:
    kol = 1
print("Среднее арифметическое положительных элементов, кратных 3 = ", sum / kol)

# 11 ВАРИАНТ(21, 22)
# В матрице найти сумму и произведение элементов строки N (N задать с клавиатуры).
# В матрице найти сумму элементов второй половины матрицы.

import random

k = int(input('Введите количество столбцов: '))
m = int(input('Введите количество строк: '))
n = int(input('Введите номер строки: '))
while n > m:
    try:
        print('Введен неверный номер строки.')
        n = int(input('Введите номер строки: '))
    except ValueError:
        pass
s = 0
p = 1
matr = [[random.randint(1, 10) for x in range(k)] for y in range(m)]
print()
print('Исходная матрица:')
for v in matr:
    print(v)
print()
for j in range(k):
    s += matr[n - 1][j]
    p *= matr[n - 1][j]
print('Сумма и произведение элементов выбранной строки:', '\n', s, p)

import random

k = int(input('Введите количество столбцов: '))
while k % 2 != 0:
    try:
        print('Количество столбцов должно быть четным.')
        k = int(input('Введите количество столбцов: '))
    except ValueError:
        pass
m = int(input('Введите количество строк: '))
s = 0
matr = [[random.randint(1, 10) for x in range(k)] for y in range(m)]
print()
print('Исходная матрица:')
for v in matr:
    print(v)
print()
h = int(k / 2)
for j in range(m):
    for i in range(h):
        s += matr[j][i - h]

print('Сумма элементов второй половины матрицы:', '\n', s)

# 12 ВАРИАНТ(23, 24)
# В матрице найти сумму и произведение элементов столбца N (N задать с клавиатуры).
# В матрице найти отрицательные элементы, сформировать из них новый массив. Вывести размер полученного массива.

import random

columns = 3
rows = 3

print("Матрица имеет вид:")
matrix = [[random.randint(1, 10) for x in range(rows)] for y in range(columns)]
for i in matrix:
    print(i)

N = int(input("Выберите столбец от 1 до 3: "))
sum = 0
multi = 1
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], "  i=", i, "    j=", j)
        if j == N - 1:
            sum += matrix[i][j]
            multi *= matrix[i][j]
            break

print("Cумма : ", sum)
print("Умножение : ", multi)

import random

columns = 6
rows = 5

print("Матрица имеет вид:")
matrix = [[random.randint(1, 10) for x in range(columns)] for y in range(rows)]
for i in matrix:
    print(i)

my_row = len(matrix) - 2

print("Минимальный элемент в предпоследней строке", min(matrix[my_row]))

# 13 ВАРИАНТ(25,26)
# Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов.
# В матрице найти максимальный положительный элемент, кратный 4.

from random import randint

numbers = []
k = randint(1, 5)
for i in range(k):
    numbers.append([])
for i in range(k):
    for j in range(k):
        numbers[i].append(randint(-100, 100))
for i in range(0, k, 2):
    average = int(sum(numbers[i]) / len(numbers[i]))
    print(average)

from random import randint

numbers = []
k = randint(1, 5)
for i in range(k):
    numbers.append([])
for i in range(k):
    for j in range(k):
        numbers[i].append(randint(-100, 100))
maximum = [0, 0]
for i in range(k):
    for j in range(len(numbers[i])):
        if numbers[i][j] % 4 == 0 and numbers[i][j] > 0:
            if numbers[maximum[0]][maximum[1]] < numbers[i][j]:
                maximum[0], maximum[1] = i, j
if maximum == [0, 0] and numbers[maximum[0]][maximum[1]] % 4 > 0:
    print('В матрице нет элементов, кратных 4.')
else:
    print(numbers)
    print('Элемент ' + str(maximum[0] + 1) + ' ряда ' + str(maximum[1] + 1) + ' столбца — ' + str(
        numbers[maximum[0]][maximum[1]]) + '.')

# 14 ВАРИАНТ(27,28)
# Для каждого столбца матрицы с четным номером найти сумму ее элементов.
# В матрице найти минимальный элемент в предпоследнем столбце.

import random


def func1(list):
    sum = 0
    for i in list:
        sum += i
    return sum


a = 9
b = 3

matrix = [[random.randint(1, 10) for y in range(a)] for x in range(b)]
matrix_reversed = [[0 for y in range(b)] for x in range(a)]
for i in matrix:
    print(i)
    print("\n")

print('Столбцы матрицы: ')

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix_reversed[j][i] = matrix[i][j]
for i in matrix_reversed:
    print(i)

print('\n', 'Четные столбцы матрицы: ')
arr = []
for i in range(len(matrix_reversed)):
    if i % 2 == 0:
        print(matrix_reversed[i])
        arr.append(func1(matrix_reversed[i]))

print("\n")
print('Сумма элементов: ', arr)

import random

a = int(input('Введите количество строк: '))
b = int(input('Введите количество столбцов: '))
matrix = [[random.randint(1, 10) for y in range(a)] for x in range(b)]
for i in matrix:
    print(i)

n = a - 2
arr = [matrix[i][n] for i in range(len(matrix))]

print('Минимальный элемент предпоследнего столбца: ', min(arr))

# 15 ВАРИАНТ(29,30)
# В матрице найти суммы элементов каждого столбца и поместить их в новый массив.
# Выполнить замену элементов второй строки исходной матрицы на полученные суммы.
# В матрице найти минимальный элемент в предпоследней строке.

import random

rows, columns = 4, 4

matrix = ([[random.randrange(5, 10) for x in range(rows)] for y in range(columns)])
print('Начальная матрица: ')
for i in matrix:
    print(i)

# В матрице найти суммы элементов каждого столбца и поместить их в новый массив.
matrix_sum = []
for i in range(len(matrix[0])):
    stowbtsy = 0
    for j in range(len(matrix)):
        stowbtsy += matrix[j][i]
    matrix_sum.append(stowbtsy)
print('Сумма элементов всех столбцов: ')
print(matrix_sum, '\n')

# Выполнить замену элементов второй строки исходной матрицы на полученные суммы.
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == rows - 3:
            matrix[i][j] = matrix_sum[j]
print('Замена второй строки на полученные элементы: ')
for i in matrix:
    print(i)

# В матрице найти минимальный элемент в предпоследней строке.
print('Минимальный элемент в предпоследней строке: ', min(matrix[columns - 2]))

# 16 ВАРИАНТ(31,32)
# В матрице найти суммы элементов каждой строки и поместить их в новый массив.
# Выполнить замену элементов третьего столбца исходной матрицы на полученные суммы.
# В матрице найти сумму элементов второй половины матрицы.

import random

row = int(input("Введите количество строк: "))  # Входные данные
column = int(input("Введите количество столбцов (минимум 3): "))
matrix = [[random.randint(-90, 90) for i in range(column)] for j in range(row)]  # Задаём матрицу
print("Матрица: ", matrix)
s = [sum(matrix[j]) for j in range(row)]  # Находим суммы строк
print("Суммы строк: ", s)
a = [matrix[j].insert(2, s[j]) for j in range(row)]  # Редактируем матрицу
b = [matrix[j].pop(3) for j in range(row)]
print("Отредактированная матрица: ", matrix)

import random

row = int(input("Введите количество строк: "))  # Входные данные
column = int(input("Введите количество столбцов: "))
v = row / 2
matrix = [[random.randint(-90, 90) for i in range(column)] for j in range(row)]  # Задаём матрицу
print("Матрица: ", matrix)
a = [sum(matrix[j]) for j in range(row) if j >= v]  # Находим сумму второй половины матрицы
b = sum(a)
print("Сумма элементов второй половины матрицы: ", b)

# 20 ВАРИАНТ(39,40)
# В матрице найти сумму элементов первых двух строк.
# В матрице найти минимальный и максимальные элементы

import random

i = 4
j = 4
matrix = [[random.randrange(1, 10) for y in range(i)] for x in range(j)]

a = sum(matrix[i - 4])
b = sum(matrix[i - 3])

print("Исходная матрица: ", matrix)
print('Сумма элементов первых двух строк: ', a + b)

import random

arr = []

print("Введите размер матрицы")

i = int(input())
j = int(input())
matrix = [[random.randrange(1, 10) for y in range(i)] for x in range(j)]
print('Исходная матрица', matrix)

for i in matrix:
    arr.append(min(i))
print("Минимальный элемент матрицы: ", min(arr))

for i in matrix:
    arr.append(max(i))
print("Максимальный элемент матрицы: ", max(arr))

# 21 ВАРИАНТ(41,42)
# В матрице найти минимальный элемент в предпоследней строке.
# В квадратной матрице элементы на главной диагонали увеличить в 2 раза.

import random

i = int(input("Введите количество строк: "))
j = int(input("Введите количество столбцов: "))
m = [[random.randrange(1, 10) for y in range(j)] for x in range(i)]
for i in m:
    print(i)
k = len(m) - 2
print("Минимальный объект в предпоследней строке: ", min(m[k]))

import random

i = int(input("Введите количество строк и столбцов: "))
j = i
m1 = [[random.randrange(1, 10) for y in range(j)] for x in range(i)]
print("Получившаяся квадратная матрица:")
for i in m1:
    print(i)
m2 = [m1[i][i] for i in range(len(m1))]
m3 = [m1[i][i] * 2 for i in range(len(m1))]
print("Элементы главной диагонали: ", m2)
print("Элементы главной диагонали, увеличенные вдвое:", m3)

# 22 ВАРИАНТ(43,44)
# В матрице найти минимальный элемент в предпоследнем столбце.
# Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов.

import random

rows = int(input('Введите количество строк: '))
columns = int(input('Введите количество столбцов: '))
matrix = [[random.randint(1, 10) for y in range(rows)] for x in range(columns)]
for i in matrix:
    print(i)

n = rows - 2
for i in range(len(matrix)):
    matrix[i][n]
arr = [matrix[i][n] for i in range(len(matrix))]
print('Минимальный элемент в предпоследнем столбце', min(arr))

import random


def func1(list):
    flag = 0
    sum = 0
    for i in list:
        flag += 1
        sum += i
    res = sum / flag
    return res


rows = int(input('Введите количество строк: '))
columns = int(input('Введите количество столбцов: '))
matrix = [[random.randint(1, 10) for y in range(rows)] for x in range(columns)]
for i in matrix:
    print(i)

arr = []
for i in range(len(matrix)):
    if i % 2 != 0:
        arr.append(matrix[i])
print(arr, "\n")
for i in arr:
    print(func1(i))

# 26 ВАРИАНТ(20, 9)
# В матрице найти среднее арифметическое положительных элементов.
# В матрице элементы первого столбца возвести в куб.

import random

M = 3
matrix = [[random.randint(-2, 2) for j in range(M)] for i in range(M)]
print(matrix, sep='\n')
h = []
for i in matrix:
    for t in i:
        if t in i:
            if t > 0:
                h.append(t)
print('среднее арифметическое положительных элементов равно:', sum(h) / len(h))

import random
import np

M = 3
Matrix = [[random.randint(0, 2) for j in range(M)] for i in range(M)]
arr = np.array(Matrix)
temp = arr[:, 0]
print(Matrix, sep='\n')
print(np.power(temp, 3))

# 27 ВАРИАНТ(53,54)
# В матрице найти среднее арифметическое положительных элементов, кратных 3.
# В матрице элементы строки N (N задать с клавиатуры) увеличить на 3.

import random

M = 3
matrix = [[random.randint(-2, 2) for j in range(M)] for i in range(M)]
print(*matrix, sep='\n')

three = [[i for i in j if i % 3 == 0 and i >= 0] for j in matrix]
n = []
for i in matrix:
    for t in i:
        if t in i:
            if t > 0:
                n.append(t)
print(f"Положительные элементы матрицы, кратные трём: {n}")
print("Их среднее арифметическое значение:", sum(n) / len(n))

import random

st = int(input("Введите кол-во столбцов: "))
sr = int(input("Введите кол-во строк: "))
N = int(input("Введите номер строки N, ктр. увеличим на 3: "))
N -= 1
matrix = [[random.randint(1, 10) for x in range(st)] for y in range(sr)]

print("Исходная матрица: ")
for v in matrix:
    print(v)

for g in range(st):
    matrix[N][g] += 3

print("Матрица после замены столбца: ")
for v in matrix:
    print(v)

# 29 ВАРИАНТ(57,58)
# В матрице элементы последнего столбца заменить на -1.
# В матрице элементы третьей строки заменить элементами из одномерного динамического массива соответствующей размерности.

import random

i, j = 3, 3
print("Матрица: ")
matr = [[random.randint(1, 10) for x in range(i)] for y in range(j)]
for q in matr:
    print(q)
print("Элементы последнего столбца заменены на -1")
for i in range(j):
    matr[i][j - 1] = [-1 for x in range(1)]
for q in matr:
    print(q)

import random

n = int(input('Введите количество столбцов: '))
m = int(input('Введите количество строк: '))

matr = [[random.randint(1, 10) for x in range(n)] for y in range(m)]
arr = [random.randint(1, 10) for i in range(m)]

print('\n', 'Массив:', '\n', arr, '\n')

print('Исходная матрица:')
for v in matr:
    print(v)

for i in range(m):
    for g in range(m):
        matr[2][g] = arr[i - g]

print()
print('Матрица после замены столбца:')
for v in matr:
    print(v)

# 30 ВАРИАНТ(59, 60)
# Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.
# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.

import random

n = int(input('Количество столбцов: '))
m = int(input('Количество строк: '))
matrix = [[random.randint(1, 20) for x in range(n)] for y in range(m)]
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

# 31 ВАРИАНТ(61,62)
# Сгенерировать матрицу, в которой нечетные элементы заменяются на 0.
# В матрице элементы второго столбца заменить элементами из одномерного динамического массива соответствующей размерности.

import random

n = int(input('Введите количество столбцов: '))
m = int(input('Введите количество строк: '))
matr = [[random.randint(1, 10) for x in range(n)] for y in range(m)]
print()
print('Исходная матрица:')
for v in matr:
    print(v)
print()
for i in range(m):
    for j in range(n):
        if matr[i][j] % 2 != 0:
            matr[i][j] = 0
print('Матрица после замены нечетных элементов:')
for v in matr:
    print(v)

import random

n = int(input('Введите количество столбцов: '))
m = int(input('Введите количество строк: '))

matr = [[random.randint(1, 10) for x in range(n)] for y in range(m)]
arr = [random.randint(1, 10) for i in range(m)]

print('\n', 'Массив:', '\n', arr, '\n')

print('Исходная матрица:')
for v in matr:
    print(v)

for i in range(m):
    for g in range(m):
        matr[i][1] = arr[g - i]

print()
print('Матрица после замены столбца:')
for v in matr:
    print(v)

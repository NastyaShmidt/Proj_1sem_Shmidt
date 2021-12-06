import random

N = input("Введите размер списка: ")
k = int(input("Введите k: "))
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Введено неверное значение.")
        N = input("Введите размер списка: ")

L = [random.randint(0, 10) for i in range(N)]    # Заполнение списка случайными числами в диапозоне от 0 до 10.
print(L)
s = k
for i in range(N):
    while s < N:
        L[s] = L[i]
        L[i] = 0
        i += 1
        s += 1
print(L)

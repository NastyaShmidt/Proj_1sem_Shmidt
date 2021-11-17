# Даны четыре целых числа, одно из которых отлично от трех других,
# равных между собой. Определить порядковый номер числа,
# отличного от остальных.

a = input("Введите 1-ое число: ")
while type(a) != int:   #Обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Введено неверное число!")
        a = input("Введите 1-ое число: ")

b = input("Введите 2-ое число: ")
while type(b) != int:   #Обработка исключений
    try:
        b = int(b)
    except ValueError:
        print("Введено неверное число!")
        b = input("Введите 2-ое число: ")

c = input("Введите 3-ое число: ")
while type(c) != int:   #Обработка исключений
    try:
        c = int(c)
    except ValueError:
        print("Введено неверное число!")
        c = input("Введите 3-е число: ")

d = input("Введите 4-ое число: ")
while type(d) != int:   #Обработка исключений
    try:
        d = int(d)
    except ValueError:
        print("Введено неверное число!")
        d = input("Введите 4-е число: ")

if (b == c) and (b == d) and (c == d):
    print("Номер числа, отличного от остальных - 1.")
elif (a == c) and (c == d) and (a == d):
    print("Номер числа, отличного от остальных - 2.")
elif (a == b) and (b == d) and (a == d):
    print("Номер числа, отличного от остальных - 3.")
elif (a == c) and (b == c) and (a == b):
    print("Номер числа, отличного от остальных - 4.")
else:
    print("Введено более 1 числа отличного от других.")

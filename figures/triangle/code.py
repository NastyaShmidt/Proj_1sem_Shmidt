import math
def triangle_perimetr():
    print('1: Ввести свои стороны. 2: Использовать стандартные стороны.')
    n = int(input('Выберите 1 или 2: '))
    while (n != 1) and (n != 2):
        try:
            print('Такого варианта нет')
            n = int(input('Выберите 1 или 2: '))
        except ValueError:
            pass
    if n == 1:
        a = int(input('Введите сторну a: '))
        b = int(input('Введите сторну b: '))
        c = int(input('Введите сторну c: '))
    else:
        a = d_a
        b = d_b
        c = d_c
    p = a + b + c
    print('Периметр треугольника = ', p)


def triangle_area():
    print('1: Ввести свои стороны. 2: Использовать стандартные стороны.')
    n = int(input('Выберите 1 или 2: '))
    while (n != 1) and (n != 2):
        try:
            print('Такого варианта нет')
            n = int(input('Выберите 1 или 2: '))
        except ValueError:
            pass
    if n == 1:
        a = int(input('Введите сторну a: '))
        b = int(input('Введите сторну b: '))
        c = int(input('Введите сторну c: '))
    else:
        a = d_a
        b = d_b
        c = d_c
    pp = (a + b + c) / 2
    s = math.sqrt(pp*(pp-a)*(pp-b)*(pp-c))
    print("Площадь теугольника = ", s)


d_a = 7
d_b = 2
d_c = 8
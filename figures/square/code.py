def square_perimetr(d_a=15):
    a = input("Введите сторону квадрата: ")
    while type(a) != int:
        try:
            a = int(a)
        except ValueError:
            a = d_a
    p = a*4
    print('Периметр квадрата = ', p)


def square_area(d_a=15):
    a = input("Введите сторону квадрата: ")
    while type(a) != int:
        try:
            a = int(a)
        except ValueError:
            a = d_a
    s = a**2
    print("Площадь квадрата = ", s)
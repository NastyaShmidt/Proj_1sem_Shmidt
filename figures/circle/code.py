def circle_perimetr(default_radius=5):
    a = input("Введите радиус окружности: ")
    while type(a) != int:
        try:
            a = int(a)
        except ValueError:
            a = default_radius
    pi = 3.14
    p = 2*pi*a
    print('Длина окружности = ', p)


def circle_area(default_radius=5):
    a = input("Введите радиус окружности: ")
    while type(a) != int:
        try:
            a = int(a)
        except ValueError:
            a = default_radius
    pi = 3.14
    s = pi*a**2
    print("Площадь окружности: ", s)
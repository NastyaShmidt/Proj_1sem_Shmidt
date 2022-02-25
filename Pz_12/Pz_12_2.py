# Разработать программу с применением пакета tk, взяв в качестве условия
# одну задачу из пз №3-8.
# Даны целые числа a,b,c, являющиеся сторонами некоторого треуголника.
# Проверить истинность высказывания:
# «Треугольник со сторонами a,b,c является равносторонним».


from tkinter import *

def count_num(event):
    t = 0

    a = int(num1.get())
    b = int(num2.get())
    c = int(num3.get())

    if a == b == c:
        t += 1

    if t == 1:
        true['text'] = " Треугольник со сторонами a,b,c является равносторонним - истина. "
    else:
        folse['text'] = " Треугольник со сторонами a,b,c является равносторонним - ложь. "


root = Tk()
root.title("Проверка истинности высказывания")
root.geometry("450x200")


Label(text="Введите размер стороны a треугольника: ").place(x=5, y=5)
num1 = Entry()
num1.place(x=250, y=5)


Label(text="Введите размер стороны b треугольника: ").place(x=5, y=25)
num2 = Entry()
num2.place(x=250, y=25)

Label(text="Введите размер стороны с треугольника: ").place(x=5, y=45)
num3 = Entry()
num3.place(x=250, y=45)

button1 = Button(text="Обработать")
button1.place(x=170, y=80)

true = Label()
true.place(x=30, y=120)

folse = Label()
folse.place(x=30, y=120)


button1.bind('<Button-1>', count_num)


root.mainloop()
# Средствами языка Python сформировать два текстовых файла(.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать новый
# текстовый файл(.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Элементы первого и второго файлов:
# Количество элементов первого и второго файлов:
# Индекс минимального элемента первого файла:
# Индекс максимального элемента второго файла:
# Элементы кратные 4 первого и второго файлов:

import random

x = 0
y = 0
a = []
b = []
f1 = open("One.txt","w", encoding="utf8")
for i in range(10):
    a.append(random.randint(-10,10))
    f1.write(str(a[i]))
    f1.write(" ")
    x += 1
f1.close()

f2 = open("Two.txt","w", encoding="utf8")
for i in range(10):
    b.append(random.randint(-10,10))
    f2.write(str(b[i]))
    f2.write(" ")
    y += 1
f2.close()

f1 = open("One.txt")
s = f1.read()

f2 = open("Two.txt")
q = f2.read()

c = a + b
g = s + q
k = x + y

f3 = open("Three.txt","w", encoding="utf8")
f3.write("Элементы первого и второго файлов: ")
f3.write(str(g))
f3.write("\n")

f3.write("Количество элементов первого и второго файлов: ")
f3.write(str(k))
f3.write("\n")

f3.write("Индекс минимального элемента первого файла: ")
min(a)
f3.write(str(a.index(min(a))))
f3.write('\n')

f3.write("Индекс максимального элемента второго файла: ")
max(b)
f3.write(str(b.index(max(b))))
f3.write("\n")

f3.write("Элементы кратные 4 первого и второго файлов: ")
for i in a:
    if i % 4 == 0:
        a.append(i)
for i in b:  if i % 4 == 0:
        b.append(i)
f3.write(" ")
f3.close()



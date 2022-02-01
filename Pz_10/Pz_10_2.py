# Из предложенного текстового файла (text18-30.txt) вывести на экран его содержимое,
# количество знаков препинания. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно поставив после последней строки автора и название произведения.

f1 = open("18-30.txt", "r", encoding="utf8")
res = f1.read()
p = ["!", ";", ":", "?", ",", ".", "/", "\\", "-", "_", '…', '—']
v = 0

for it in res:
    for i in p:
        if i == it:
            v += 1
f1.close()

print("Содержимое файла:")
print()
print(res)
print()
print("Количество знаков препинания:", v)

f2 = open("i.txt", "w", encoding="utf8")
f2.write(res)
f2.write("\n")
f2.write("\n")
f2.write("М. Ю. Лермонтов")
f2.write("\n")
f2.write("Бородино")

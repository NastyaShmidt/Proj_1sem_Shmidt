# Дана строка, состоящая из русских слов,
# набранных заглавными буквами и разделенных пробелами (одним или несколькими).
# Найти количество слов, которые начинаются и заканчиваются одной и той же буквой.

S0 = input("Введите строку: ")
S0 = S0.upper()
S = S0.split()
p = 0
print("Исходная строка:", S0)
for i in range(len(S)):
    if S[i][0] in S[i][len(S[i])-1]:
        p += 1
print("Количество слов, которые начинаются и заканчиваются одной и той же буквой:", p)

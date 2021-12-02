# Дан список A размера N. Сформировать новый список B того же размера по следующему правилу:
# элемент Bк равен сумме элементов списка A с номерами от 1 до K.

import random

A = []
p = 0
b = random.randint(0,10)
while p < b:
    A.append(random.randint(0,10))
    p+=1

print(A)

a = len(A)

B = []
d = 0
i = 1
while d <= a-1:
    B.append(sum(A[0: i]))
    d+=1
    i+=1
print(B)

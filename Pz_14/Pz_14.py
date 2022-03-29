# В исходном текстовом файле (radio_stations.txt) найти все домены
# из URL-адресов

import re

p = re.compile(r"[/:]+")
s = re.compile(r"[\w]+[.][\w]+[.][\w]+")
with open('radio_stations.txt', 'r', encoding='utf-8') as file:
    text = file.read()
reg = re.split(p,text)
print("Выбранные домены: ")
print(s.findall(str(reg)))
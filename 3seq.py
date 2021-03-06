'''
(МОДУЛЬ 3) В проекте создать новый модуль 3seq.py. Задание:

Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4
'''

import re
str1 = input('Введите элементы первого списка: ')
str2 = input('Введите элементы второго списка: ')

# считаем, что элементы  - это буквы и цифры, все остальное разделители:
list1 = re.findall(r'[a-zA-Zа-яёА-ЯЁ\d]+' , str1)
list2 = re.findall(r'[a-zA-Zа-яёА-ЯЁ\d]+' , str2)

print('Элементы первого списка: ', ', '.join(list1))
print('Элементы второго списка: ', ', '.join(list2))

new_list1 = []
[new_list1.append(i) for i in list1 if i not in list2]
print('Удалить из первого списка элементы из второго списка: ', ' , '.join(new_list1))
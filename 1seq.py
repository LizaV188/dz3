'''
(МОДУЛЬ 1) Создать новый проект, в нем создать модуль 1seq.py. Задание:
Пользователь вводит количество элементов будущего списка
После этого по очереди по одной вводит любые цифры
Сохранить цифры в список
Отсортировать список по возрастанию и вывести на экран
Пример работы: Введите количество элементов: 3
Введите 1 элемент: 5
Введите 2 элемент: 2
Введите 3 элемент: 4
Вывод: [2, 4, 5]
'''

# предполагаю, что пользователь вводит только цифры, не делаю проверки на это, чтобы не загромождать код


list_num = []
q_num = int(input('Введите количество элементов списка: '))
for i in range(q_num):
    num = input('Введите '+str(i+1)+' элемент: ')
    list_num.append(num)
print('Вывод: ', sorted(list_num))


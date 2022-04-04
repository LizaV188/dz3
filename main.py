"""
1. Из всех методов списка (list) выбрать 5 тех, которые по вашему мнению используются чаще всего
2. Написать их через запятую с параметрами
3. Повторить процедуру для словарей (dict), множеств (set), строк (str)
"""

# list
# list.append(x), list.insert(i, x), list.remove(x), list.sort([key=функция]), list.reverse()

l = [10, 2, 300, 8, 'b', 2]
print(l)
l.append('7')   # добавить в конец списка
print(l)
l.insert(4, 3)  # вставить на место с индексом 4
print(l)
l.remove(2)     # удалить элемент с индексом 2
print(l)

def len_str(i):
    return len(str(i))

l.sort(key=len_str)  # сортировка, например, по длине строки
print(l)

l.reverse()
print(l)

# словари
# dict.keys(), dict.values(), dict.items(), dict.update([other]), dict.fromkeys(seq[, value])

keys_test = {'a':1, 'b':50, 'c':101}
print(keys_test.keys())
print(keys_test.values())
print(keys_test.items())

keys_test.update({'a':2})
print(keys_test.items())

keys_test1 = dict.fromkeys([1,2,3,4,5], 0)      # создание словаря из списка ключей
print(keys_test1)

# множества
# set.copy(), set.union(other, ...) или set | other (объединение),
# set.intersection(other, ...) или set & other (пересечение)
# set.difference(other, ...) или set - other (вычитание)
# set.isdisjoint(other) (истина, если нет общих элементов)
set1 = {1,2,3}
set2 = {2,4,5}
print(set1|set2)
print(set1&set2)
print(set1-set2)
print(set1.isdisjoint(set2))

# строки
# S.split(символ), S.join(список) (сборка строки из списка с разделителем S)
# S.find(str, [start],[end]) (поиск подстроки в строке)
# S.isdigit(), S.replace(str1, str2)

ss = 'dsf'
print(ss.replace('ds','aaa'))
print(ss)
print(ss.find('f'))
print('-'.join('12345'))
print(ss.split('s'))
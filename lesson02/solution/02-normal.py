# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
import math

numbers = [2, -5, 8, 9, -25, 25, 4]
squares = []

for x in numbers:
    if x > 0:
        square = math.sqrt(x)
        if square % 1 == 0:
            squares.append(int(square))

print(squares)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
date = '02.01.2013'

days = {
    1: 'первое',
    2: 'второе',
    3: 'третье',
}

months = {
    1: 'января',
    2: 'февраля',
    3: 'марта',
}

day, month, year = date.split('.')

print("{} {} {} года".format(
    days[int(day)], months[int(month)], year
))

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random

n = 10
random_numbers = []

# for x in range(n):
#     random_numbers.append(random.randint(-100, 100))

# generator method
random_numbers = [random.randint(-100, 100) for x in range(n)]

print(random_numbers)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
source_numbers = [1, 2, 4, 5, 6, 2, 5, 2]

non_repeat_numbers = list(set(source_numbers))
unique_numbers = []

for x in source_numbers:
    if source_numbers.count(x) == 1:
        unique_numbers.append(x)

print("Source: {} \nNumbers: {} \nUnique: {}".format(
    source_numbers,
    non_repeat_numbers,
    unique_numbers
))

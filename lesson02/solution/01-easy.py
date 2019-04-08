# 01-1# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ['apple', 'banana', 'kiwi', 'watermelon']
align_step = len(max(fruits, key=len))

for index, item in enumerate(fruits, start=1):
    print("{}. {:>{}}".format(
        index, item, align_step
    ))

# another solution
for item in fruits:
    print("{}. {:>{}}".format(
        fruits.index(item), item, align_step
    ))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

first = [4, 8, 15, 16, 23, 42]
second = [4, 9, 15, 17, 22, 23] # 4, 15, 23

for x in second:
    if x in first:
        first.remove(x)

print(first)

# easy method (only hashable type)
print(list(set(first) - set(second)))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
numbers = [4, 8, 15, 16, 23, 42]
new_numbers = []

for x in numbers:
    if x % 2 == 0:
        new_numbers.append(x / 4)
    else:
        new_numbers.append(x * 2)

print(new_numbers)

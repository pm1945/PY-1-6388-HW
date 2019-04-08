# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5

# вычислите и выведите y
equation_items = equation.split()[2:]

x = 2.5
k = float(equation_items[0][:-1])
b = float(equation_items[2])
# y = kx + b
result = (k * x) + b

# print('({} * {}) + {} = {}'.format(k, x, b, result))
print(f'({k} * {x}) + {b} = {result}') # only Python 3.6+

# SECOND METHOD
equation = equation.replace('x', f' * {x}')
equation = equation[equation.find('=') + 2:]

result = eval(equation)

print(equation, '=', result)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

# SOLUTION
day, month, year = date.split('.')
is_valid = True

months = {
    # month: days count
    1: 31, 2: 30, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31,
}

if len(day) == 2 and len(month) == 2 and len(year) == 4:
    day = int(day)
    month = int(month)
    year = int(year)

    if month < 1 or month > 12:
        is_valid = False
    else:
        if day < 1 or day > months[month]:
            is_valid = False
        else:
            if year < 1 or year > 9999:
                is_valid = False
else:
    is_valid = False

print(f"Date validation status: {is_valid}")

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

room = 15

if room > 0 and room <= 2000000000:
    loop_index = 1
    floor_index = 1
    room_index = 1

    # start global loop
    while room_index <= room:
        print("----------")

        # generate floors
        for _ in range(loop_index):
            new_floor = []

            # generate rooms
            for x in range(loop_index):
                new_floor.append(room_index)
                room_index += 1

            # show new floor content
            print(f'Floor #{floor_index}, contains {loop_index} rooms: {new_floor}')

            # check room exists
            if room in new_floor:
                room_position = new_floor.index(room) + 1
                print(f'Room #{room} was founded on #{floor_index} floor at {room_position} position')
                break

            # increment next floor index
            floor_index += 1
        
        loop_index += 1
else:
    print('Invalid room number')

# GeekBrains math solution -> https://geekbrains.ru/posts/babylon_task

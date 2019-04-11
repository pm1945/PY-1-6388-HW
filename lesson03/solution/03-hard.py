# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


def calculate_fraction(expression):
    # преобразование дроби в число
    def fraction_to_number(fraction):
        fraction = fraction.split()
        number = 0

        if len(fraction) > 1:
            integer = int(fraction[0])
            fraction = list(map(int, fraction[1].split('/')))

            number = integer + (fraction[0] / fraction[1])
        else:
            fraction = fraction[0]

            if fraction.find('/') is not -1:
                fraction = list(map(int, fraction.split('/')))
                number += fraction[0] / fraction[1]
            else:
                number = int(fraction)

        return number

    # преобразование числа в дробь
    def number_to_fraction(number):
        integer = int(number // 1)
        fraction = round(number % 1, 9)

        if fraction > 0:
            power = 10

            while (fraction * power) % 1 > 0:
                power *= 10

            fraction = [int(fraction * power), power]

            if len(str(fraction[0])) >= 9:
                fraction = [fraction[0] / fraction[0], fraction[1] / fraction[0]]

            result = [integer, fraction]
        else:
            result = [integer]

        return result

    # нахождение НОД (наибольший общий делитель)
    def greatest_common_divisor(a, b):
        border = min(list(map(int, [a, b])))

        for x in range(border, 1, -1):
            if a % x == 0 and b % x == 0:
                return x

        return 1

    # упрощение дроби
    def simplify_fraction(fraction):
        if len(fraction) > 1:
            gcd = greatest_common_divisor(fraction[1][0], fraction[1][1])

            fraction[1] = list(map(
                lambda x: int(x / gcd),
                fraction[1]
            ))

        return fraction

    operator = ' + ' if expression.find(' + ') is not -1 else ' - '
    left, right = expression.split(operator)

    a, b = list(map(fraction_to_number, [left, right]))

    if operator == ' + ':
        result = a + b
    else:
        result = a - b

    result = number_to_fraction(result)
    result = simplify_fraction(result)

    return result


# print(calculate_fraction('2 + 2'))          # 4
# print(calculate_fraction('2 + 5/10'))       # 2 1/2
# print(calculate_fraction('5/6 - 3/6'))      # 1/3
# print(calculate_fraction('2 3/4 + 1 3/4'))  # 4 1/2
# print(calculate_fraction('1 4/5 + 2 3/4'))  # 4 11/20
# print(calculate_fraction('-2/3 - -2'))      # 1 1/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
import os


def calculate_workers():
    local_path = os.path.join(os.path.curdir, '03', 'data')

    workers = []

    def normalize_worker(worker):
        worker['salary'] = int(worker['salary'])
        worker['hours'] = int(worker['hours'])
        worker['complete'] = int(worker['complete'])

        return worker

    with open(os.path.join(local_path, 'workers')) as f:
        lines = f.readlines()[1:]

        for line in lines:
            worker_keys = ['name', 'surname', 'salary', 'job_title', 'hours']
            worker = dict(zip(worker_keys, line.split()))

            workers.append(worker)

    with open(os.path.join(local_path, 'hours_of')) as f:
        lines = f.readlines()[1:]
        workers_info = []

        for line in lines:
            worker_keys = ['name', 'surname', 'complete']
            worker = dict(zip(worker_keys, line.split()))

            for item in workers:
                if item['name'] == worker['name']:
                    item['complete'] = worker['complete']

    workers = list(map(normalize_worker, workers))

    for w in workers:
        hour_cost = w['salary'] / w['hours']

        if w['complete'] < w['hours']:
            uncomplete = w['hours'] - w['complete']
            w['total'] = w['salary'] - (hour_cost * uncomplete)
        elif w['complete'] > w['hours']:
            over_complete = w['complete'] - w['hours']
            hour_cost *= 2
            w['total'] = w['salary'] + (hour_cost * over_complete)

        w['total'] = round(w['total'], 2)

        print(w)


calculate_workers()


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

def write_fruits():
    local_path = os.path.join(os.curdir, '03', 'data')
    f_path = os.path.join(local_path, 'fruits')

    if not os.path.exists(f_path):
        os.mkdir(f_path)

    with open(os.path.join(local_path, 'fruits.txt')) as f:
        fruits_content = list(filter(lambda x: len(x) > 2, f.readlines()))

    letters = {}

    for letter in range(ord('А'), ord('Я') + 1):
        letters[chr(letter)] = f"fruit_{chr(letter)}"

        filename = os.path.join(f_path, letters[chr(letter)])
        if os.path.exists(filename):
            os.remove(filename)

    for fruit in fruits_content:
        first_letter = fruit[0]
        filename = os.path.join(f_path, letters[first_letter])

        with open(filename, mode='a') as f:
            f.write(fruit)

# write_fruits()

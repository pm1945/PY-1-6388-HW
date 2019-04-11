# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    current, next_item = 1, 1
    numbers = []

    for _ in range(m + 1):
        numbers.append(current)
        current, next_item = next_item, current + next_item

    return numbers[n:m]


print(fibonacci(10, 20))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    sort = list.copy(origin_list)
    sort_len = len(sort)

    for _ in range(sort_len):
        for x in range(sort_len - 1):
            if sort[x] > sort[x + 1]:
                sort[x], sort[x + 1] = sort[x + 1], sort[x]

    return sort


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_filter(function, collection):
    new_collection = []

    for item in collection:
        if function(item):
            new_collection.append(item)

    return new_collection


list_to_check = [1, 2, 3, 4]

print(
    my_filter(
        lambda x: x % 2 == 0,
        list_to_check
    )
)


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
def check_values(a1, a2, a3, a4):
    """
    По свойству диагоналей четырехугольника ABCD — параллелограмм, 
    если координаты середин отрезков АС и BD, совпадают
    """
    x1 = (a1['x'] + a3['x']) / 2
    x2 = (a2['x'] + a4['x']) / 2

    y1 = (a1['y'] + a3['y']) / 2
    y2 = (a2['y'] + a4['y']) / 2

    if x1 == x2 and y1 == y2:
        return True
    else:
        return False


def input_point(point_name='A'):
    point = list(map(
        float,
        input(f"Type {point_name} coords [x,y]: ").split(',')
    ))
    return {'x': point[0], 'y': point[1]}


point_a1 = input_point('A1')
point_a2 = input_point('A2')
point_a3 = input_point('A3')
point_a4 = input_point('A4')

print(check_values(point_a1, point_a2, point_a3, point_a4))

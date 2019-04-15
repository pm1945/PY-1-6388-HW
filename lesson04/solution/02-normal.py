# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO' \
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK' \
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn' \
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa' \
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete' \
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ' \
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb' \
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC' \
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB' \
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT' \
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu' \
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB' \
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa' \
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ' \
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

# with regexp
import re

pattern = r'[a-z]+'
items = re.findall(pattern, line)

print(items)

# without regex
upper_symbols = [chr(character) for character in range(ord('A'), ord('Z') + 1)]
line_list = list(line)

for index, item in enumerate(line_list[:]):
    if item in upper_symbols:
        line_list[index] = ' '

items = (''.join(line_list)).split()

print(items)

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm' \
         'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV' \
         'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA' \
         'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV' \
         'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW' \
         'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC' \
         'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR' \
         'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm' \
         'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn' \
         'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS' \
         'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf' \
         'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH' \
         'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN' \
         'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ' \
         'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

# with regexp
pattern = r'[a-z]{2}[A-Z]+[A-Z]{2}'

items = [item[2:-2] for item in re.findall(pattern, line_2)]

print(items)

# without regexp
items = []
lower_symbols = [chr(character) for character in range(ord('a'), ord('z') + 1)]
upper_symbols = [chr(character) for character in range(ord('A'), ord('Z') + 1)]

line_list = list(line_2)

index = 0

while index < len(line_list):
    item = line_list[index]

    if item not in upper_symbols:
        # пропускаем символы в нижнем регистре
        index += 1
        continue
    else:
        # устанавливаем границы проверки
        left_border = index - 2
        right_border = index + 1

        # цикл с проверкой существования индексов списка
        while left_border > -1 and right_border < len(line_list):
            # проверяем два левых символа на нижний регистр
            if line_list[left_border + 1] in lower_symbols and line_list[left_border] in lower_symbols:
                # находим первый символ в нижнем регистре после заглавных
                while right_border < len(line_list) and line_list[right_border] in upper_symbols:
                    right_border += 1
                else:
                    # считаем количество символов в строке 
                    # (больше 4, так как по два с каждой стороны лишние)
                    difference = right_border - left_border

                    if difference > 4:
                        # берем срез списка по индексам
                        slice_line = line_list[left_border + 2:right_border - 2]
                        # склеиваем в строку
                        slice_line = ''.join(slice_line)
                        # добавляем строку в список результатов
                        items.append(slice_line)

                    # ставим индекс на правую границу 
                    # для дальнейшего поиска без предыдущих элементов
                    index = right_border
                    break
            else:
                index += 1
                break

    index += 1

print(items)

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import os
import re
import random

filename = '03-3.txt'

if not os.path.exists(filename):
    # заполняем список из 2500 цифр (рандомно от 1 до 9)
    nums = [random.randint(1, 9) for _ in range(2500)]
    with open(filename, 'w') as f:
        # пишем строку в файл (будет одной строкой, так как нет \n)
        f.writelines(list(map(str, nums)))
else:
    print('File was loaded!')

    max_item = ''

    with open(filename) as f:
        # загружаем число в виде строки из файла
        file_content = f.readline()

    # проходим циклом от 1 до 9
    for x in range(1, 10):
        # создаем шаблон выражения (1+, 2+, 3+) для поиска групп чисел
        pattern = re.compile(str(x) + '+')
        # находим элемент, максимальный по длине из полученных
        item = max(re.findall(pattern, file_content), key=len)

        # перезаписываем число,
        # если оно больше по порядку (даже с такой же длиной)
        # 1111 >= 5555 будет 5555 (порядок выше)
        if len(max_item) <= len(item):
            max_item = item

    print(f"Largest sequence is: {max_item}")

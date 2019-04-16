# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits=0):
    if ndigits > 0:
        power = 10 ** ndigits
        number = (number * power) + 0.41  # 0.4
        number = (number // 1) / power
    else:
        remainder = number % 1
        number = (number + 1) - remainder if remainder > 0.5 else number - remainder
    return number


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 6))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_len = len(str(ticket_number))

    if ticket_len != 6:
        return False

    left = list(map(int, str(ticket_number)[:3]))
    right = list(map(int, str(ticket_number)[3:]))

    return sum(left) == sum(right)


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

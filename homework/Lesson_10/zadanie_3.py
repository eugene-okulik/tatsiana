# Задание №3
# Напишите программу: Есть функция которая делает одну из арифметических операций с переданными ей числами
# (числа и операция передаются в аргументы функции). Функция выглядит примерно так:
#
# def calc(first, second, operation):
#     if operation == '+':
#         return first + second
#     elif .....
# Программа спрашивает у пользователя 2 числа (вне функции)
#
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
#
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение

# List comprehension
# Дан такой кусок прайс листа:
#
# (Копируйте эту переменную (константу) в код прямо как есть)
#
# PRICE_LIST = '''тетрадь 50р
# книга 200р
# ручка 100р
# карандаш 70р
# альбом 120р
# пенал 300р
# рюкзак 500р'''
# При помощи list comprehension и/или dict comprehension превратите этот текст в словарь такого вида:
#
# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
# В выполнении не должно быть циклов.
#
# Обратите внимание, что цены в словаре имеют тип int (они не в кавычках)

def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


def verif_operation(func):
    def wrapper(first, second):
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        if first < 0 or second < 0:
            operation = '*'
        return func(first, second, operation)

    return wrapper


@verif_operation
def calc_decorator(first, second, operation):
    return calc(first, second, operation)


number_1 = float(input("Введите первое число: "))
number_2 = float(input("Введите второе число: "))

result = calc_decorator(number_1, number_2)
print("Результат:", result)

print("**********")
PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_dict = {
    item.split()[0]: int(item.split()[1].strip('р'))
    for item in PRICE_LIST.splitlines()
}

print(price_dict)

# Задание 2
# Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число
#
# На всякий случай, напомню, что превращать результат работы генератора в список - неправильно.

# !!! Евгений,я поменяла 100000-ое число на 10000
# так как при 100000 компьютер не справляется и выдает ошибку - нехватает ячеек))

def fibonacci(limit=100001):
    num1 = 0
    num2 = 1
    position = 1
    while position < limit:
        yield num1
        num1 = num2
        num2 = num1 + num2
        position += 1


# Array - pozicii kotorye nujno naiti
positions_to_find = [5, 200, 1000, 10000]

# def fibonacci - generiruet nujnoe kolvo chisel - do 100001 pozicii
# i potom s pomoshyu for my ishem interesuyushie nas posicii

position = 1
for number_fibonacci in fibonacci(100001):
    if position in positions_to_find:
        print(f"{position}-е число Фибоначчи: {number_fibonacci}")
    position += 1

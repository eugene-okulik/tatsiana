# Zadanie 2
# Map, filter
# Есть такой список:
# temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
# 30, 28, 24, 23]

# С помощью функции map или filter создайте из этого списка новый список с жаркими днями. Будем считать жарким всё,
# что выше 28.
#
# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.

temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
    30, 28, 24, 23
]

# def hot_tmp(x):
# return x > 28

# new_list = filter(hot_tmp,temperatures)
# print(list(new_list))

temperatures_new_array = filter(lambda x: x > 28, temperatures)
temperatures_new_array = list(temperatures_new_array)
print(temperatures_new_array)

print(max(temperatures_new_array))
print(min(temperatures_new_array))
print(sum(temperatures_new_array) / len(temperatures_new_array))

# Задание 1
# Дан такой список:
# person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
# С помощью распаковки создайте из этого списка переменные, содержащие соответствующие данные:
# name, last_name, city, phone, country

# Задание 2
# Допустим, какая-то программа возвращает результат своей работы в таком виде:
# результат операции: 42
# результат операции: 514
# результат работы программы: 9
# С помощью срезов и метода index получите из каждой строки с результатом число, прибавьте к полученному числу 10,
# результат сложения распечатайте.

# Задание 3
# Даны такие списки:
# students = ['Ivanov', 'Petrov', 'Sidorov']
# subjects = ['math', 'biology', 'geography']
# Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен выглядеть так:
# Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography

# Задание 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print("Name:", name, ", Last Name:", last_name, ", City:", city, ", Phone:", phone, ", Country:", country)

# Задание 2
list_res = [42, 514, 9]
print(list_res[::])
res_1 = list_res[0] + 10
print(res_1)
res_2 = list_res[1] + 10
print(res_2)
res_progr = list_res[2] + 10
print(res_progr)

# Задание 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

stud_1, stud_2, stud_3 = students
sub_1, sub_2, sub_3 = subjects

print(stud_1, ",", stud_2, ",", stud_3, "study these subjects:", sub_1, ",", sub_2, ",", sub_3, ".")

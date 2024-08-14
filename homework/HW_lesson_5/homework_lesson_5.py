# Задание 1
# Дан такой список:
# person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
#
# С помощью распаковки создайте из этого списка переменные, содержащие соответствующие данные:
# name, last_name, city, phone, country
#
# Задание 2
# Допустим, какая-то программа возвращает результат своей работы в таком виде:
#
# результат операции: 42
#
# результат операции: 514
#
# результат работы программы: 9
#
# С помощью срезов и метода index получите из каждой строки с результатом число,
# прибавьте к полученному числу 10, результат сложения распечатайте.
#
# Задание 3
# Даны такие списки:
#
# students = ['Ivanov', 'Petrov', 'Sidorov']
#
# subjects = ['math', 'biology', 'geography']
#
# Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен выглядеть так:
#
# Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography

# Задание 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

# person_raspakovannyi variant 1
# name = person[0]
# last_name = person[1]
# city = person[2]
# phone = person[3]
# country = person[4]
# print(name, last_name, city, phone, country)

# #person_raspakovannyi variant 2
name, last_name, city, phone, country = person
print("name = ", name, ", last_name = ", last_name, ", city = ", city, ", phone = ", phone, ", country = ", country)

# Задание 2
# Женя, кроме for ничего в голову не идет ((

list_dannye = [
    "результат операции: 42",
    "результат операции: 514",
    "результат работы программы: 9"
]

numbers_all = []

for line in list_dannye:
    if ":" in line:
        # Сначала находим индекс где начинается число в каждой строке - после : + пробел, и делаем срез оттуда
        ind = line.index(":") + 2
        num_str = line[ind::]
        # Proverka type
        # print(type(num_str))
        # Конвертируем в int
        num = int(num_str)
        # добавляем числа в наш новый список
        numbers_all.append(num)
print(numbers_all)

numbers_changed = []

for num in numbers_all:
    num = num + 10
    numbers_changed.append(num)
    print(num)
# print(numbers_changed)

# Задание 3

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
student_1, student_2, student_3 = students
subject_1, subject_2, subject_3 = subjects
print("Students " + student_1 + "," + student_2 + "," + student_3 + " study these subjects: " + subject_1 + ","
      + subject_2 + "," + subject_3)

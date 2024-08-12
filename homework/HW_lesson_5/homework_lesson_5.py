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
# С помощью срезов и метода index получите из каждой строки с результатом число, прибавьте к полученному числу 10, результат сложения распечатайте.
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
list_dannye = [
    "результат операции: 42",
    "результат операции: 514",
    "результат работы программы: 9"
]

element_1 = list_dannye[0]
element_1_number = list_dannye[0][20:]
element_2 = list_dannye[1]
element_2_number = list_dannye[1][20:]
element_3 = list_dannye[2]
element_3_number = list_dannye[2][-1]

print(int(element_1_number) + 10)
print(int(element_2_number) + 10)
print(int(element_3_number) + 10)

# Задание 3

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
student_1, student_2, student_3 = students
subject_1, subject_2, subject_3 = subjects
print("Students " + student_1 + "," + student_2 + "," + student_3 + " study these subjects: " + subject_1 + ","
      + subject_2 + "," + subject_3)

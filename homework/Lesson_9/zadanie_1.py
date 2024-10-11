# Задание 1
# Обработка даты
# Дана такая дата: "Jan 15, 2023 - 12:05:33"
#
# Преобразуйте эту дату в питоновский формат, после этого:
#
# 1. Распечатайте полное название месяца из этой даты
#
# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"

from datetime import datetime

date = "Jan 15, 2023 - 12:05:33"

python_date = datetime.strptime(date, "%b %d, %Y - %H:%M:%S")
print(python_date)

month_name = python_date.strftime("%B")
print("Полное название месяца: ", month_name)

formatted_date = python_date.strftime("%d.%m.%Y, %H:%M")
print("Дата в формате: ", formatted_date)

# Задание 1
# Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool.
# Спросите у пользователя salary. А bonus пусть назначается рандомом.
#
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
#
# Примеры результатов:
#
# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'

import random

# Ask salary
salary_user_input = int(input("What is your salary? "))

# bonus random from the list True, False
bonus = random.choice([True, False])

if bonus:
    # if bonus is True - vyberi randomnoe chislo ot 0 do 100 i dobav k salary_input
    random_bonus = random.randint(0, 100)
    salary_with_bonus = salary_user_input + random_bonus
else:
    salary_with_bonus = salary_user_input

# Resultat
print(f"{salary_user_input}, {bonus} - '${salary_with_bonus}'")

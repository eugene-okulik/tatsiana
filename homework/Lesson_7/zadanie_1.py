# Задание №1 - "Угадайка"
# Создайте такую программу:
# Программа хранит какую-либо цифру в переменной.
# Программа просит пользователя угадать цифру. Пользователь вводит цифру.
# Программа сравнивает цифру с той, что хранится в переменной.
# Если цифры не равны, программа пишет “попробуйте снова” и снова просит пользователя угадать цифру.
# Если пользователь угадывает цифру, программа пишет “Поздравляю! Вы угадали!” и завершается.
# Т.е. программа не завершается пока пользователь не угадает цифру.
# Подсказка: задание выполняется с помощью цикла while

number = 5
while True:
    input_user_number = int(input("Give me a your number, please: "))
    if input_user_number == "'exit":
        break
    elif input_user_number == "skip":
        continue
    elif input_user_number == number:

        print(f"Congratulation! The number is : {number}")
        break
    else:
        print("No! Try again!")

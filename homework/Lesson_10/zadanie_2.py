# Задание №2
# Создайте универсальный декоратор, который будет управлять тем, сколько раз запускается декорируемая функция
#
# Код, использующий этот декоратор может выглядеть, например, так:
#
# @repeat_me
# def example(text):
#     print(text)
#
# example('print me', count=2)
# В результате работы будет такое:
#
# print me
#
# print me
#
# Если есть время и желание погуглить и повозиться, то можно попробовать создать декоратор, который сможет
# обработать такой код:

# @repeat_me(count=2)
# def example(text):
#     print(text)
#
# example('print me')

def repeat_me(func):
    def wrapper(*args, count=1):
        if count > 0:
            func(*args)
            wrapper(*args, count=count - 1)

    return wrapper


@repeat_me
def example(text):
    print(text)


example("print me\n", count=2)

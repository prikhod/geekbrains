# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def user_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('zero division')
        return


def main():
    dividend = int(input('Введите делимое: '))
    divider = int(input('Введите делитель: '))
    print('Результат деления: ', user_div(dividend, divider))


if __name__ == '__main__':
    main()

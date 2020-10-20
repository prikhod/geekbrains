#  Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
#  Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
#  качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivisionErrorUser(Exception):
    def __init__(self, text_error):
        self.text_error = text_error


def main():
    while True:
        try:
            input_list = list(map(int, input('Введите делимое и делитель через пробел').split()))
            if len(input_list) != 2:
                break
            if input_list[1] == 0:
                raise ZeroDivisionErrorUser('Деление на ноль')
        except ZeroDivisionErrorUser as err:
            print(err)
        except ValueError as err:
            print('Неверный ввод:', err)
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()

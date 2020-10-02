# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.


def sum_list(lst):
    """ Сумма чисел

    Функция принимает список, возвращает сумму чисел из списка до первого разделителя(не числа)
    и флаг наличия разделителя.
    """
    result = 0
    for el in lst:
        if el.isdigit():
            result += int(el)
        else:
            return result, False
    return result, True


def main():
    is_continue = True
    result_sum = 0
    while is_continue:
        in_list = input('Введите числа через пробел: ').split(' ')
        result, is_continue = sum_list(in_list)
        result_sum += result
        print('Сумма чисел в строке: ', result)
    print('Сумма чисел в строках до разделителя', result_sum)  # в задании этого вывода нет


if __name__ == '__main__':
    main()

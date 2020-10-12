# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint
from functools import reduce


def write_numbs_to_file(file_name):
    with open(file_name, 'w') as f_obj:
        f_obj.write(' '.join(str(randint(0, 100000)) for _ in range(1, 1000)))


def sum_number_from_file(file_name):
    with open(file_name, 'r') as f_obj:
        str_numb = f_obj.read().split()
        print(reduce(lambda a, b: int(a) + int(b), str_numb))
        print(sum(map(int, str_numb)))
        #  сумма двумя способами посчитана


if __name__ == '__main__':

    write_numbs_to_file('5.5')
    sum_number_from_file('5.5')

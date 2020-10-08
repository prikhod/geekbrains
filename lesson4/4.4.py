# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать
# генератор списка. (Можно использовать list.count()).
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

from random import randint

def main():
####################ПЕРВЫЙ СПОСОБ###########################################

    # in_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    in_list = [randint(0, 1000) for i in range(1, 1000)]

    res = [el for el in in_list if in_list.count(el) == 1]
    print(res)

####################ВТОРОЙ СПОСОБ###########################################
    """ Заведем список индексов no_double_indexes исходного списка, будем проверять элементы исходного списка 
    на дублирование и удалять индексы из массива no_double_indexes.  Обойдем список, начиная проверять с еще
    непроверенных элементов (по диагонали), элементы по удаленным индексам проверять не будем
    """

    no_double_indexes = [el for el in range(0, len(in_list))]  # список индексов
    i = 0
    while i < len(no_double_indexes):
        i_in = i + 1
        len_change = False
        len_no_double_indexes = len(no_double_indexes)
        while i_in < len_no_double_indexes:
            if in_list[no_double_indexes[i]] == in_list[no_double_indexes[i_in]]:
                no_double_indexes.remove(no_double_indexes[i_in])
                len_no_double_indexes = len(no_double_indexes)
                len_change = True
            else:
                i_in += 1
        if len_change:
            no_double_indexes.remove(no_double_indexes[i])
        else:
            i += 1
    res = [in_list[i] for i in no_double_indexes]
    print(res)

####################ТРЕТИЙ СПОСОБ###########################################
    """ Будем идти по всему массиву и добавлять не дублирующиеся элементы в новый список
    """
    i = 0
    res = []
    len_list = len(in_list)
    while i < len_list:
        i_in = 0
        is_double = False
        while i_in < len_list:
            if in_list[i] == in_list[i_in] and i != i_in:
                is_double = True
            i_in += 1
        if not is_double:
            res.append(in_list[i])
        i += 1

    print(res)

####################ЧЕТВЕРТЫЙ СПОСОБ###########################################
    i = 0
    res = []
    len_list = len(in_list)
    for i, el in enumerate(in_list):
        is_double = False
        for i_in, el_in in enumerate(in_list):
            if el_in == el and i != i_in:
                is_double = True
        if not is_double:
            res.append(el)
    print(res)
####################ПЯТЫЙ СПОСОБ###########################################
    counts = {}
    for el in in_list:
        if el not in counts:
            counts[el] = 0
        counts[el] += 1
    res = [el for el in counts.keys() if counts[el] ==1]

    print(res)
"""Время выполнения: 
    0.012377024989982601 с count
    0.028858142269891685
    0.07359166106994962
    0.03938548205005645
"""


if __name__ == '__main__':
    main()

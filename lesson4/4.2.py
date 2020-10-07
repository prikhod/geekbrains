# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор списка.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].


def main():
    init_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 56]
    res = []

    ########ДВА ГЕНЕРАТОРА############
    gen = (el for el in init_list)
    gen2 = (el for el in init_list)
    next(gen2)
    for el in gen:
        try:
            new_el = next(gen2)
            if new_el > el:
                res.append(new_el)
        except StopIteration:
            break
    print(res)
    ########ДВА ГЕНЕРАТОРА КОНЕЦ#######
    res.clear()
    ########ЦИКЛ И ГЕНЕРАТОР ##########
    gen = (el for el in init_list)
    preverios_el = next(gen)
    while True:
        try:
            new_el = next(gen)
            if new_el > preverios_el:
                res.append(new_el)
            preverios_el = new_el
        except StopIteration:
            break
    print(res)
    ########ЦИКЛ И ГЕНЕРАТОР КОНЕЦ#######


if __name__ == '__main__':
    main()

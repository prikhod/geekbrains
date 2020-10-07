# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с
# индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Исходные списки можете инициализировать прямо в коде, но обязательно проверьте работоспособность,
# для пустого списка, списка из 1 элемента, списка с четным количеством элементов и с нечетным. (Опционально)
# Если получится, реализуйте обмен, как функцию.

def exchange_elements(in_list):
    if len(in_list) < 1:
        return None  # Если ничего сделать со списком не можем
    for num, element in enumerate(in_list):
        if not (num % 2) and num + 1 < len(in_list):  # Выбираем четный элемент списка и следим чтоб не выйти из листа
            in_list[num], in_list[num + 1] = in_list[num + 1], in_list[num]  # Меняем его на следующий нечетный


def main():
    list1 = [[],
             [0],
             [0, 1],
             [0, 1, 2],
             [0, 1, 2, 3],
             [0, 1, 2, 3, 4],
             [0, 1, 2, 3, 4, 5],
             [0, 1, 2, 3, 4, 5, 6]
             ]
    for element in list1:
        exchange_elements(element)
        print(element)


if __name__ == '__main__':
    main()

# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


def input_text_to_file(file_name):
    in_str = input('Введите строку текста: ')
    while in_str != '':
        with open(file_name, 'a') as f_obj:
            f_obj.write(f'{in_str}\n')
        in_str = input('Введите строку текста: ')


if __name__ == '__main__':
    input_text_to_file('hellotext.txt')

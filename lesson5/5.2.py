# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


def text_analize(file_name):
    with open(file_name, 'r') as f_obj:
        num_str = 0  # объявим заранее номер строки чтоб была возможность вывести их количество
        for num_str, string in enumerate(f_obj, 1):
            words = string.split()
            print(f'Количество слов в строке {num_str}: {len(words)}')
        print(f'Количество строк в файле: {num_str}')


if __name__ == '__main__':
    text_analize('5.2')

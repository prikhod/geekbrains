# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def int_func(text):
    return text.title()


def main():
    print(int_func('teXt'))
    in_list = input('Введи строку слов в нижнем регистре').split()
    print(' '.join([int_func(word) for word in in_list]))


if __name__ == '__main__':
    main()

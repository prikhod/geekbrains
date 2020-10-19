# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix: list):
        """ Обработаем случаи разной длины строк матрицы,
            валидность типа элементов
            и запишем в  self._max_len_numb максимальную длину числа для красивого вывода
            одномерные массивы [1, 2, 3] за матрицы не считаем
        """
        try:
            len_str = len(matrix[0])
            max_len_numb = 0
            for matrix_str in matrix:
                if len_str != len(matrix_str):
                    raise ValueError('Not valid matrix')
                for el in matrix_str:
                    if len(str(el)) > max_len_numb:
                        max_len_numb = len(str(el))
                    if not isinstance(el, int):
                        raise ValueError('Not valid value in matrix')
            self.matrix = matrix
            self._max_len_numb = max_len_numb
        except Exception:
            raise ValueError('Not valid matrix')

    def __len__(self):  # нужна будет для суммирования матриц
        return len(self.matrix), len(self.matrix[0])

    def __str__(self):
        res = ''
        template = '|' + ('{:' + str(self._max_len_numb + 2) + 'd}') * len(self.matrix[0]) + '|\n'
        # '|{:6d}{:6d}{:6d}|
        # '
        # вот такой например шаблон получился для моего примера
        for line in self.matrix:
            res += template.format(*line)
        return res

    def __add__(self, other):
        if self.__len__() != other.__len__():
            raise ValueError('Different length matrix')
        res = []
        for row1, row2 in self.matrix, other.matrix:
            res.append(list(map(lambda a, b: a + b, row1, row2)))
        return Matrix(res)


if __name__ == '__main__':
    matr = Matrix([[1, 2, 33], [44, 3, 4444]])
    matr2 = Matrix([[44, 3, 4444], [1, 2, 33]])
    matr3 = Matrix([[3, 4444], [2, 33]])
    print(matr)
    print(matr2)

    print(matr + matr2)
    matr = Matrix([[1], [2]])
    print(matr)
    matr = Matrix([[1, 2]])
    print(matr)
    matr = Matrix([[1]])
    print(matr)

    #  print(matr + matr3)

'''Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
'''

import math
from itertools import starmap
from copy import deepcopy

class Matrix:
    def __init__(self, matrix):
        self.matrix = list(matrix)
        self.__shape = (len(max(self.matrix, key=len)), len(self.matrix))
        if len(min(self.matrix, key=len)) != self.shape[0]:
            self.__reshape()

    @property
    def shape(self):
        return self.__shape

    def __reshape(self):
        for itm in self.matrix:
            tmp = self.shape[0] - len(itm)
            if tmp:
                itm.extend([0 for _ in range(tmp)])

    def __str__(self):
        max_len_itm = len(str(max(map(lambda item: max(item, key=lambda x: len(str(x))), self.matrix))))
        if not max_len_itm & 1:
            max_len_itm += 1
        if not max_len_itm & 0:
            max_len_itm += 3

        result = ''
        for line in self.matrix:
            result += ''.join([f'{itm:>{max_len_itm}}' for itm in line]) + '\n'
        return result


    def __add__(self, other):
        return list(map(lambda x, y: list(map(lambda z, w: z + w, x, y)), self.matrix, other.matrix))


a = Matrix([[31, 22, 0, 0], [37, 43, 0, 0], [51, 86, 0, 0]])
b = Matrix([[3, 5, 32, 0], [2, 4, 6, 0], [-1, 64, -8, 0]])
c = Matrix([[4, 5, 2, 6], [2, 4, 6, 4], [0, 0, 0, 0]])

x = Matrix(a + b)
print(a)
print(b)
print(c)
print(x)



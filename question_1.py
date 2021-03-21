r"""
Реализовать класс Matrix. Обеспечить перегрузку конструктора класса,
    который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
    Результатом сложения должна быть новая матрица.
"""
from itertools import zip_longest


class Matrix:
    def __init__(self, input_lst: list):
        self.__matrix = []
        len_input = len(input_lst[0])
        for item in input_lst:
            if type(item) != list:
                raise TypeError(f"'{item}' в '{input_lst}' не является списком")
            elif len_input < len(item):
                len_input = len(item)
        for i, line in enumerate(input_lst):
            self.__matrix.append([0] * len_input)
            for j, item in enumerate(line):
                self.__matrix[i][j] = item

    def __str__(self):
        max_len = 0
        str_items = []
        for i, line in enumerate(self.__matrix):
            str_items.append([])
            for item in line:
                str_item = item if type(item) == str else str(item)
                max_len = len(str_item) if len(str_item) > max_len else max_len
                str_items[i].append(str_item)
        matrix_str = 'Матрица:'
        for line in str_items:
            matrix_str += '\n| '
            for item in line:
                matrix_str += f'{item:>{max_len}} '
            matrix_str += '|'
        return matrix_str

    def __add__(self, other):
        if type(other) != Matrix:
            raise TypeError(f'{other}({type(other)}) не является матрицей')
        result = []
        for self_line, other_line in zip_longest(self.__matrix, other.__matrix, fillvalue=[0]):
            result.append([])
            for self_item, other_item in zip_longest(self_line, other_line, fillvalue=0):
                try:
                    summ = self_item + other_item
                    result[-1].append(summ)
                except TypeError:
                    str_s = self_item if type(self_item) == str else str(self_item)
                    str_o = other_item if type(other_item) == str else str(other_item)
                    result[-1].append(str_s + str_o)
        return Matrix(result)


def str_to_list():
    strng = input('Введите значения для матрицы:\n'
                  'пробел             - разделитель между элементами строки матрицы,\n'
                  'запятая с пробелом - разделитель между строками\n>>> ')
    lst = [item.split() for item in strng.split(', ')]
    for i, line in enumerate(lst):
        for j, item in enumerate(line):
            sign = item[0] if len(item) > 1 and item[0] == '+' or item[0] == '-' else ''
            item = item[1:] if sign else item
            lst[i][j] = int(sign + item) if item.isdigit() else sign + item
    return lst


try:
    matrix1 = Matrix(str_to_list())
    print(matrix1)
    matrix2 = Matrix(str_to_list())
    print(matrix2)
    print(f'Сумма двух матриц:\n{matrix1 + matrix2}')
except Exception as error:
    print(f'Ошибка ввода: {error}')

r"""
Реализовать класс Matrix. Обеспечить перегрузку конструктора класса,
    который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
    Результатом сложения должна быть новая матрица.
"""
from itertools import zip_longest


class Matrix:
    """Класс матрица"""
    def __init__(self, input_lst: list):
        """При инициации принимает список списков"""
        self.__matrix = []              # создаём параметр с пустым списком
        len_input = len(input_lst[0])   # ищем самый длинный список и проверяем чтобы это были именно списки
        for item in input_lst:
            if type(item) != list:
                raise TypeError(f"'{item}' в '{input_lst}' не является списком")
            elif len_input < len(item):
                len_input = len(item)
        for i, line in enumerate(input_lst):    # перегоняем в атрибут значения из списка, дополняя недостающее нулями
            self.__matrix.append([0] * len_input)
            for j, item in enumerate(line):
                self.__matrix[i][j] = item

    def __str__(self):
        """Перегружаем возвращаемую строку"""
        max_len = 0     # переменная для хранения макс длины элемента
        str_items = []  # переменная для строковых значений элементов
        for i, line in enumerate(self.__matrix):    # ищем самый длинный элемент + преобразовываем все элементы в str
            str_items.append([])
            for item in line:
                str_item = item if type(item) == str else str(item)
                max_len = len(str_item) if len(str_item) > max_len else max_len
                str_items[i].append(str_item)
        matrix_str = 'Матрица:'     # готовим строку для вывода
        for line in str_items:      # добавляем в нее элементы с добавлением оформления
            matrix_str += '\n| '
            for item in line:
                matrix_str += f'{item:>{max_len}} '
            matrix_str += '|'
        return matrix_str

    def __add__(self, other):
        """Перегружаем сложение. Здесь реализовано только в рамках сложения матриц"""
        if type(other) != Matrix:   # защита от дурака
            raise TypeError(f'{other}({type(other)}) не является матрицей')
        result = []                 # список для результата
        # цикл по строкам матриц. недостающие строки заполняются списком с нулём
        for self_line, other_line in zip_longest(self.__matrix, other.__matrix, fillvalue=[0]):
            result.append([])        # добавляем в результат строку
            # цикл по элементам строк матриц. недостающие элементы принимаются за ноль
            for self_item, other_item in zip_longest(self_line, other_line, fillvalue=0):
                try:
                    summ = self_item + other_item   # суммируем элементы строк
                    result[-1].append(summ)         # добавляем сумму в список результата
                except TypeError:               # если элементы несуммируемы приводим их к строке и складываем
                    str_s = str(self_item)
                    str_o = str(other_item)
                    result[-1].append(str_s + str_o)
        return Matrix(result)   # возвращаем преобразованный в матрицу список списков


def str_to_list():
    """Конструктор списка"""
    strng = input('Введите значения для матрицы:\n'
                  'пробел             - разделитель между элементами строки матрицы,\n'
                  'запятая с пробелом - разделитель между строками\n>>> ')
    lst = [item.split() for item in strng.split(', ')]  # распиливаем список на подсписки и элементы
    for i, line in enumerate(lst):                          # приводим то что возможно к int
        for j, item in enumerate(line):
            sign = item[0] if len(item) > 1 and item[0] == '+' or item[0] == '-' else ''
            item = item[1:] if sign else item
            lst[i][j] = int(sign + item) if item.isdigit() else sign + item
    return lst


# ИСПОЛНЯЕМАЯ ЧАСТЬ
try:
    matrix1 = Matrix(str_to_list())     # генерим первую матрицу
    print(matrix1)                      # выводим ее
    matrix2 = Matrix(str_to_list())     # генерим вторую матрицу
    print(matrix2)                      # выводим ее тоже
    print(f'Сумма двух матриц:\n{matrix1 + matrix2}')   # выводим сумму матриц
except Exception as error:              # на всякий случай перехватываем исключение
    print(f'Ошибка ввода: {error}')

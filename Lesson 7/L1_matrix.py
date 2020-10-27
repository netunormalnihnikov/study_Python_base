from random import randint


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ""
        for n_str, el_list in enumerate(self.matrix, 1):
            for n_el, el in enumerate(el_list, 1):
                result += (f"{el}\n" if n_str != len(self.matrix) else f"{el}") if n_el == len(el_list) else f"{el}\t"
        return result

    def __add__(self, other):
        while len(self.matrix) != len(other.matrix):
            """"Коррекция количества строк в матрице"""
            if len(self.matrix) < len(other.matrix):
                self.matrix.append([0 for _ in range(len(self.matrix[0]))])
            else:
                other.matrix.append([0 for _ in range(len(other.matrix[0]))])

        while len(self.matrix[0]) != len(other.matrix[0]):
            """"Коррекция количества столбцов в матрице"""
            if len(self.matrix[0]) > len(other.matrix[0]):
                for i in other.matrix:
                    i.append(0)
            else:
                for i in self.matrix:
                    i.append(0)

        """"Сумма матриц"""
        matrix_list = []
        for list_1, list_2 in zip(self.matrix, other.matrix):
            str_list = []
            for el_1, el_2 in zip(list_1, list_2):
                str_list.append(el_1 + el_2)
            matrix_list.append(str_list)
        return Matrix(matrix_list)


matrix_1 = Matrix([[randint(0, 100) for _ in range(5)] for _ in range(3)])
matrix_2 = Matrix([[randint(0, 100) for _ in range(3)] for _ in range(6)])

print(f"Матрица №1:\n{matrix_1}\n\nМатрица №2:\n{matrix_2}\n\nРезультат сложения матриц:\n{matrix_1 + matrix_2}")

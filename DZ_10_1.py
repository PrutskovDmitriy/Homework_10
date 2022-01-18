class Matrix:

    def __init__(self, data):
        self.data = data
        for line in self.data[:-1]:
            if len(line) != len(self.data[self.data.index(line) + 1]):
                raise ValueError('Количество элементов не совпадает')

    def __str__(self):
        return '\n'.join('\t'.join(str(num) for num in line) for line in self.data)

    def __add__(self, other):
        if len(self.data) != len(other.data):
            raise ValueError('Размерности не совпадают')
        else:
            for i in range(len(self.data)):
                if len(self.data[i]) != len(other.data[i]):
                    raise ValueError('Размерности не совпадают')
            item = [[int(self.data[line][num]) + int(other.data[line][num]) for num in \
                     range(len(self.data[line]))] for line in range(len(self.data))]
            return Matrix(item)


matrix_1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m1 = Matrix(matrix_1)
print(m1)
print()
matrix_2 = [[3, 5, 8, 3], [8, 3, 7, 1]]
m2 = Matrix(matrix_2)
print(m2)

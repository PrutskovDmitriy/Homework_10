class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, row_len):
        result = ['*' * row_len] * (self.nums // row_len)
        if self.nums % row_len:
            result.append('*' * (self.nums % row_len))
        return '\n'.join(result)

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        return f'Sum of cell is: {Cell(self.nums + other.nums)}'

    def __sub__(self, other):
        if self.nums < other.nums:
            raise ValueError('Ячеек в 1ой клетке меньше, чем во 2ой, вычитание невозможно')
        return f'Subtraction of cell is: {Cell(self.nums - other.nums)}'

    def __mul__(self, other):
        return f'Multiply of cell is: {Cell(self.nums * other.nums)}'

    def __floordiv__(self, other):
        return f'Floordiv of cell is: {Cell(self.nums // other.nums)}'


cell_1 = Cell(48)
cell_2 = Cell(32)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(4))

# Task 3

class Cell:
    def __init__(self, q: int):
        self.q = q

    def __add__(self, other):
        return Cell(self.q + other.q)

    def __sub__(self, other):
        if self.q >= other.q:
            return Cell(self.q - other.q)
        else:
            return f'Уменьшаяемая клетка слишком мала для данной операции, попробуйте другую'

    def __mul__(self, other):
        return Cell(self.q * other.q)

    def __truediv__(self, other):
        return Cell(round(self.q / other.q))

    def __str__(self):
        return f'New cell has value:\n{self.q}'

    def make_order(self, n):
        str = ''
        for x in range(self.q):
            str += '*'
            if (x + 1) % n == 0:
                str += '\n'
        return Cell(str)


cell_1 = Cell(52)
cell_2 = Cell(265)
cell_3 = Cell(14)
cell_4 = Cell(23)
cell_5 = Cell(111)
new_cell = cell_1 + cell_2 * cell_3 / cell_4 - cell_5
print(new_cell)
print(new_cell.make_order(12))
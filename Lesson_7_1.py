# Task 1

class Matrix:
    b = str()


    def __init__(self, l: list):
        self.l = l

    def __add__(self, other):
        l_new = []
        for i in range(len(self.l)):
            el_new = []
            for j in range(len(self.l[0])):
                result = self.l[i][j] + other.l[i][j]
                el_new.append(result)
            l_new.append(el_new)
        return Matrix(l_new)

    def __str__(self):
        for el in self.l:
            print(f'{el}')



l = [[1, 2, 3, 4], [15, -23, 212, -88], [22, 315, 1561, -8]]
m = [[2, 56, -88, 0], [258, -111, -26, 55], [-777, 242, -1, -23]]
k = [[1, 2, 3, 5], [0, -2, -1, 2], [23, 2, 185, 2]]
d = [[25, 26, -56, 0], [5, -12, -22, -33], [85, -7, 39, 586]]
matrix_1 = Matrix(l)
matrix_2 = Matrix(m)
matrix_3 = Matrix(k)
matrix_4 = Matrix(d)
matrix_add = matrix_1 + matrix_2 + matrix_3 + matrix_4
matrix_add.__str__()


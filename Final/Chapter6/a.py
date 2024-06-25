class a:
    def __init__(self, matrix) -> None:
        self.matrix = matrix

    def Duynhat(self):
        b = list(set(self.matrix))
        b.sort()
        return b
    
    def Hieu(self, b):
        c = list(set(self.matrix) - set(b))
        c.sort()
        return c
    
    def Giao(self, b):
        c = list(set(self.matrix) & set(b))
        c.sort()
        return c
    
    def Hop(self, b):
        c = list(set(self.matrix) | set(b))
        c.sort() 
        return c

matrix_a = [1, 5, 3, 7, 9, 4, 2]
matrix_b = [9, 6, 2, 3, 8]

obj_a = a(matrix_a)
result_c = obj_a.Giao(matrix_b)
print(result_c) 

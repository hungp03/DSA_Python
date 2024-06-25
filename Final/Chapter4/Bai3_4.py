class BieuThuc:
    def __init__(self):
        self.toan_hang_stack = []
        self.toan_tu_stack = []

    def thuc_hien_phep_tinh(self, toan_tu):
        b = self.toan_hang_stack.pop()
        a = self.toan_hang_stack.pop()

        if toan_tu == '+':
            self.toan_hang_stack.append(a + b)
        elif toan_tu == '-':
            self.toan_hang_stack.append(a - b)
        elif toan_tu == '*':
            self.toan_hang_stack.append(a * b)
        elif toan_tu == '/':
            self.toan_hang_stack.append(a // b)  # Sử dụng phép chia nguyên để đảm bảo kết quả là số nguyên

    def GiaTri(self, bt):
        operator_precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        i = 0

        while i < len(bt):
            if bt[i].isdigit():
                operand = 0
                while i < len(bt) and bt[i].isdigit():
                    operand = operand * 10 + int(bt[i])
                    i += 1
                self.toan_hang_stack.append(operand)
            elif bt[i] in operator_precedence:
                while (len(self.toan_tu_stack) > 0 and
                       operator_precedence[self.toan_tu_stack[-1]] >= operator_precedence[bt[i]]):
                    self.thuc_hien_phep_tinh(self.toan_tu_stack.pop())
                self.toan_tu_stack.append(bt[i])
                i += 1

        while len(self.toan_tu_stack) > 0:
            self.thuc_hien_phep_tinh(self.toan_tu_stack.pop())

        return self.toan_hang_stack.pop()

    def HauTo(self, bt):
        operator_precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        hau_to = []
        i = 0

        while i < len(bt):
            if bt[i].isdigit():
                operand = 0
                while i < len(bt) and bt[i].isdigit():
                    operand = operand * 10 + int(bt[i])
                    i += 1
                hau_to.append(str(operand))
            elif bt[i] in operator_precedence:
                while (len(self.toan_tu_stack) > 0 and
                    operator_precedence[self.toan_tu_stack[-1]] >= operator_precedence[bt[i]]):
                    hau_to.append(self.toan_tu_stack.pop())
                self.toan_tu_stack.append(bt[i])
            i += 1

        while len(self.toan_tu_stack) > 0:
            hau_to.append(self.toan_tu_stack.pop())

        return ' '.join(hau_to)


# Sử dụng đoạn mã với sửa đổi
bt = "3+4*2-6/3"

bieu_thuc = BieuThuc()
ket_qua = bieu_thuc.GiaTri(bt)
print("Giá trị của biểu thức {} là: {}".format(bt, ket_qua))


bt2 = "2 + 3 * 5"

bieu_thuc = BieuThuc()
ket_qua_hau_to = bieu_thuc.HauTo(bt2)
print("Biểu thức hậu tố của biểu thức {} là: {}".format(bt2, ket_qua_hau_to))

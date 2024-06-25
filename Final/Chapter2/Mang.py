class Mang:
    def __init__(self, matrix):
        self.matrix = matrix

    def MaTranVuong(self):
        n = len(self.matrix)
        if n != len(self.matrix[0]):
            return False
        return True

    def DoiXung(self):
        if not self.MaTranVuong():
            return "Không phải ma trận vuông"

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def TamGiacTren(self):
        if not self.MaTranVuong():
            return "Không phải ma trận vuông"

        for i in range(len(self.matrix)):
            for j in range(i):
                if self.matrix[i][j] != 0:
                    return False
        return True

    def TrungHang(self):
        if not self.MaTranVuong():
            return "Không phải ma trận vuông"

        for i in range(len(self.matrix)):
            for j in range(i+1, len(self.matrix)):
                if self.matrix[i] == self.matrix[j]:
                    return True
        return False

    def NhomHang(self):
        if not self.MaTranVuong():
            return "Không phải ma trận vuông"

        res = []
        for i in range(len(self.matrix)):
            for j in range(i+1, len(self.matrix)):
                if self.matrix[i] == self.matrix[j]:
                    res.append([i, j])
        return res

    def TamGiacDuoi(self):
        if not self.MaTranVuong():
            return "Không phải ma trận vuông"

        for i in range(len(self.matrix)):
            for j in range(i + 1, len(self.matrix)):
                if self.matrix[i][j] != 0:
                    return False
        return True

    def TrungCot(self):
        if not self.MaTranVuong():
            return "Không phải ma trận vuông"

        for i in range(len(self.matrix[0])):
            for j in range(i+1, len(self.matrix[0])):
                trung = True
                for k in range(len(self.matrix)):
                    if self.matrix[k][i] != self.matrix[k][j]:
                        trung = False
                        break
                if trung:
                    return True
        return False

    def MangNhomCot(self):
        if not self.MaTranVuong():
            return "Không phải ma trận vuông"

        for cot in range(len(self.matrix[0])):
            print("Nhóm cột", cot, ": ", end="")
            for hang in range(len(self.matrix)):
                if hang > 0 and self.matrix[hang][cot] == self.matrix[hang - 1][cot]:
                    print(self.matrix[hang][cot], end=" ")
                else:
                    print()
                    print(self.matrix[hang][cot], end=" ")
            print()

    def Dao(self):
        if not self.MaTranVuong():
            return "Không phải ma trận vuông"

        max_area = 0

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 1:
                    area = self.find_max_rectangle_area(i, j)
                    max_area = max(max_area, area)

        return max_area

    def find_max_rectangle_area(self, i, j):
        max_area = 0

        for x in range(i, len(self.matrix)):
            for y in range(j, len(self.matrix[x])):
                if self.matrix[x][y] == 1:
                    area = (x - i + 1) * (y - j + 1)
                    max_area = max(max_area, area)
                else:
                    break

        return max_area

matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

mang = Mang(matrix)

result_doi_xung = mang.DoiXung()
result_tam_giac_tren = mang.TamGiacTren()
result_trung_hang = mang.TrungHang()
result_nhom_hang = mang.NhomHang()
result_tam_giac_duoi = mang.TamGiacDuoi()
result_trung_cot = mang.TrungCot()
mang.MangNhomCot()
result_dao = mang.Dao()

print("Đối xứng:", result_doi_xung)
print("Tam giác trên:", result_tam_giac_tren)
print("Trùng hàng:", result_trung_hang)
print("Nhóm hàng:", result_nhom_hang)
print("Tam giác dưới:", result_tam_giac_duoi)
print("Trùng cột:", result_trung_cot)
print("Đảo:", result_dao)

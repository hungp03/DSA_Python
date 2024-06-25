def Nhan(a, b):
    # Chuyển đổi các mảng thành số nguyên
    a_num = int(''.join(map(str, a[1])))
    b_num = int(''.join(map(str, b[1])))

    # Áp dụng dấu
    if a[0] == 1:
        a_num = -a_num
    if b[0] == 1:
        b_num = -b_num

    result = a_num * b_num

    # Kiểm tra tràn số
    if result > 2147483647 or result < -2147483648:
        return [-1]

    # Trả về kết quả
    return result

a = [0, [1, 2, 3, 4, 5, 9, 4]]
b = [1, [6, 7, 8, 9, 0, 1, 3]]
print(Nhan(a,b))
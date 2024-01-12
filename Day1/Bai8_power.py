# Hàm tính x^y
def power(x, y):
    assert isinstance(y, int) and y >= 0, "y phải là một số nguyên không âm"
    # Tất cả các số mũ 0 đều bằng 1
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)

print(power(2.5,3))
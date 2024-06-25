def Cong(a, b):
    len_a = len(a)
    len_b = len(b)

    max_len = max(len_a, len_b) + 1  
    result = [-1] * max_len 

    carry = 0 
    for i in range(1, max_len + 1):
        digit_a = int(a[-i]) if i <= len_a else 0 
        digit_b = int(b[-i]) if i <= len_b else 0 

        sum_digit = digit_a + digit_b + carry
        carry = sum_digit // 10
        result[-i] = sum_digit % 10


    if carry == 1:
        return [-1] * (max_len + 1)
    else:
        return result if result[0] != 0 else result[1:]


a = [1, 2, 3]
b = [4, 5, 6]
print("Kết quả của a + b:", Cong(a, b))

c = [9, 9, 9]
d = [1, 1, 1]
print("Kết quả của c + d:", Cong(c, d))

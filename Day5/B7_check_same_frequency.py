def check_same_frequency(lst1, lst2):
    freq_l1 = {}
    freq_l2 = {}
    for el in lst1:
        # Mỗi lần duyệt qua element(el)
        # Dùng hàm get của dictionary để trả về giá trị hiện tại + 1
        # Hàm get(current_value, default_value)
        freq_l1[el] = freq_l1.get(el, 0) + 1

    # Tương tự với list2
    for el in lst2:
        freq_l2[el] = freq_l2.get(el, 0) + 1

    # Trả về kết quả đúng nếu 2 dict giống nhau
    return freq_l1 == freq_l2

list1 = [1,2,3,2,1]
list2 = [3,1,2,1,3]
print(check_same_frequency(list1, list2))
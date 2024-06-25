def common_elements(tup1, tup2):
    # Chuyển tuple cho trước thành set để lọc các phần tử trùng
    # VD: (1,1,2,3) => {1,2,3}
    # Dùng phép & để lấy các phần tử chung của 2 set
    # Ép kiểu tuple và trả về kết quả
    return tuple(set(tup1) & set(tup2))


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
result = common_elements(tuple1, tuple2)
print(result)

def openRussianDoll(doll):
    # Kiểm tra xem arg doll có phải là số nguyên dương không
    assert 0 <= doll == int(doll)
    # Khi chỉ có 1 doll, tức là tất cả doll đã được mở
    if doll == 1:
        print("All dolls are opened")
    # Nếu doll > 1, ta sẽ mở đến khi còn 1 doll bằng cách gọi lại hàm này với arg là doll -1
    else:
        openRussianDoll(doll-1)

openRussianDoll(5)





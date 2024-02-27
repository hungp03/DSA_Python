def insert_value_front(tple, value):
    # Cần có dấu phẩy `,` để Python nhận biết là tuple rồi mới nối tuple
    return (value,) + tple

input_tuple = (2,3,4)
value_to_insert = 1
output = insert_value_front(input_tuple, value_to_insert)
print(output)

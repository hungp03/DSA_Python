def tuple_elementwise_sum(t1, t2):
    if len(t1) != len(t2):
        return 'Độ dài 2 tuple không bằng nhau'
    return tuple(x + y for x, y in zip(t1, t2))


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple_elementwise_sum(tuple1, tuple2)
print(result)

print(tuple([1]) + (1,2,3))
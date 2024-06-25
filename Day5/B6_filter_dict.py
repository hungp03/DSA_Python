def filter_dict(md, condition):
    filtered_dict = {}
    for key, value in md.items():
        if condition(key, value):
            filtered_dict[key] = value
    return filtered_dict

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_result = filter_dict(my_dict, lambda k, v: v % 2 == 0)
print(filtered_result)

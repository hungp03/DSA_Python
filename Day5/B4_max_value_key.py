def max_value_key(my_dict):
    max_value = None
    max_key = None
    for k,v in my_dict.items():
        if max_value is None or v > max_value:
            max_value = v
            max_key = k
    return max_key
    # return max(my_dict, key=my_dict.get)

my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key(my_dict))
def reverse_dict(my_dict):
    rev_dict = {}
    for key, value in my_dict.items():
        rev_dict[value] = key
    return rev_dict

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dict(my_dict))
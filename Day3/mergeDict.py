from copy import deepcopy

def merge_dicts(dict1, dict2):
    res = deepcopy(dict1)
    for key, value in dict2.items():
        if key in res:
            res[key] += value
        else:
            res[key] = value
    print(res)

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)

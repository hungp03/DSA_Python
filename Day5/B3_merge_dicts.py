from copy import deepcopy

def merge_dicts(d1, d2):
    res = deepcopy(d1)
    for k,v in d2.items():
        if k in res:
            res[k] += v
        else:
            res[k] = v
    return res

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4,'d': 5}
print(merge_dicts(dict1, dict2))
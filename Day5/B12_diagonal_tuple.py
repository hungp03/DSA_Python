def get_diagonal(tuple_of_tups):
    return tuple(tuple_of_tups[i][i] for i in range(len(tuple_of_tups)))

input_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
diagonal = get_diagonal(input_tuple)
print(diagonal)
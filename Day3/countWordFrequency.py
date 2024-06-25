def count_word_frequency(lst):
    count_dict = {}
    for el in lst:
        if el in count_dict:
            count_dict[el] += 1
        else:
            count_dict[el] = 1
    print(count_dict)

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
count_word_frequency(words)

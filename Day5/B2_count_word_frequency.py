def count_word_frequency(words):
    count_word = {}
    for w in words:
        if w in count_word:
            count_word[w] += 1
        else:
            count_word[w] = 1
    return count_word

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
print(count_word_frequency(words))

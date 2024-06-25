def count_words_in_file(file_path):
    word_count = {}

    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.lower().split()
                for word in words:
                    if word.isalpha():
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1
    except FileNotFoundError:
        print("File not found.")
    
    return word_count

file_path = "test.txt"
print(count_words_in_file(file_path)['man'])

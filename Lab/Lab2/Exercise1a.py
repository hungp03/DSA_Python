def count_chars(word):
    word = word.lower()  # Chuyển tất cả các chữ cái trong từ về chữ thường
    
    char_count = {}
    for char in word:
        if char.isalpha():  # Chỉ xem xét các ký tự là chữ cái
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

string1 = 'Happiness'
output1 = count_chars(string1)
print(output1)

string2 = 'smiles'
output2 = count_chars(string2)
print(output2)

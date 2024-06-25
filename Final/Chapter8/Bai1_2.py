class Dictionary:
    def __init__(self) -> None:
        self.dictionary = {}
    
    def get_hash(self, word) -> str:
        return word[0]
    
    def add_word(self, word, synonyms=None, antonyms=None):
        key = self.get_hash(word)
        if key not in self.dictionary:
            self.dictionary[key] = {}
        self.dictionary[key][word] = {'sysnonyms':synonyms, 'antonyms':antonyms}

    def lookup_word(self, word):
        key = self.get_hash(word)
        if key in self.dictionary and word in self.dictionary[key]:
            return self.dictionary[key][word]
        else:
            return f'Từ "{word}" không có trong từ điển'
    
    def lookup_sysnonyms(self, word):
        key = self.get_hash(word)
        if key in self.dictionary and word in self.dictionary[key]:
            return self.dictionary[key][word]['sysnonyms']
        else:
            return f'Từ "{word}" không có trong từ điển'
    
    def lookup_antonyms(self, word):
        key = self.get_hash(word)
        if key in self.dictionary and word in self.dictionary[key]:
            return self.dictionary[key][word]['antonyms']
        else:
            return f'Từ "{word}" không có trong từ điển'
        
if __name__ == "__main__":
    d = Dictionary()
    d.add_word('vui vẻ', 'hạnh phúc', 'buồn bã')
    d.add_word('vắng mặt', 'trống', 'đầy đủ')
    print(d.lookup_word('vui vẻ'))
    print('Từ đồng nghĩa của "vui vẻ":', d.lookup_sysnonyms('vui vẻ'))
    print('Từ trái nghĩa của "vui vẻ":', d.lookup_antonyms('vui vẻ'))
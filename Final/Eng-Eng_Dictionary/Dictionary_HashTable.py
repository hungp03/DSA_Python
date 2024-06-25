class Meaning:
    def __init__(self, part_of_speech, definition, example):
        self.part_of_speech = part_of_speech
        self.definition = definition
        self.example = example
        self.next = None

class Node:
    def __init__(self, word) -> None:
        self.word = word
        self.left = None
        self.right = None
        self.meanings = None

    # Thêm nghĩa cho từ
    def add_meaning(self, part_of_speech, definition, example):
        new_meaning = Meaning(part_of_speech, definition, example)
        if self.meanings is None:
            self.meanings = new_meaning
        else:
            current = self.meanings
            prev = None
            while current is not None and current.part_of_speech < part_of_speech:
                prev = current
                current = current.next
            # Chèn vào đầu danh sách
            if prev is None:
                new_meaning.next = self.meanings
                self.meanings = new_meaning
            # Chèn vào giữa hoặc cuối danh sách
            else:
                new_meaning.next = current
                prev.next = new_meaning

class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, word):
        if self.root is None:
            self.root = Node(word)
        else:
            self.insertNode(self.root, word)

    def insertNode(self, node, word):
        # Từ có âm đầu đứng trước thì sang trái
        if word < node.word:
            # Chưa có nhánh trái
            if node.left is None:
                node.left = Node(word)
            # Đã có nhánh trái
            else:
                self.insertNode(node.left, word)
        # Nếu từ được xét là sau bảng chữ cái với node đang xét
        elif word > node.word:
            # Nếu chưa có nhánh phải
            if node.right is None:
                node.right = Node(word)
            else:
                self.insertNode(node.right, word)
    
    def lookup_word(self, word):
        return self.find(self.root, word)
    
    def find(self, node, word):
        if node is None:
            return None
        if node.word == word:
            return node
        if node.word > word:
            return self.find(node.left, word)
        if node.word < word:
            return self.find(node.right, word)
        
    def remove_word(self, word):
        return self.delete(self.root, word)
    
    def delete(self, node, word):
        if node is None:
            return None
        if word < node.word:
            return self.delete(node.left, word)
        if word > node.word:
            return self.delete(node.right, word)
        if node.word == word:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self.min_value_node(node.right)
            node.word = temp.word
            node.meanings = temp.meanings
            node.right = self._delete(node.right, temp.word)
        return node

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
class HashDictionary:
    # Khởi tạo hash table với 26 ô với mỗi ô là 1 BST()
    def __init__(self) -> None:
        self.hash_table = [BST() for _ in range(26)]
    
    def get_index(self, word):
        # ord() lấy mã Unicode của kí tự
        return ord(word[0].lower()) - ord('a')
    
    def lookup_word(self, word):
        idx = self.get_index(word)
        found_node = self.hash_table[idx].lookup_word(word)
        if found_node:
            meanings = []
            current = found_node.meanings
            while current is not None:
                meanings.append((current.part_of_speech, current.definition, current.example))
                current = current.next
            return meanings
        return None


    def add_word(self, word, part_of_speech, definition, example):
        idx = self.get_index(word)
        found_node = self.hash_table[idx].lookup_word(word)
        if found_node is None:
            self.hash_table[idx].insert(word)
            found_node = self.hash_table[idx].lookup_word(word)
        found_node.add_meaning(part_of_speech, definition, example)

    def remove_word(self, word):
        idx = self.get_index(word)
        self.hash_table[idx].remove_word(word)
        
def load_dictionary(file):
    hash_dict = HashDictionary()
    with open(file, 'r') as f:
        for line in f:
            word, part_of_speech, definition, example = line.strip().split('`$', 3)
            hash_dict.add_word(word, part_of_speech, definition, example)
    return hash_dict

def save_dictionary(hash_table ,filename):
    with open(filename, 'w') as f:
        for bst in hash_table.hash_table:
            _save_node(bst.root, f)

def _save_node(node, file):
    if node is not None:

        _save_node(node.left, file)
        
        current_meaning = node.meanings
        while current_meaning is not None:
            file.write(f"{node.word}`${current_meaning.part_of_speech}`${current_meaning.definition}`${current_meaning.example}\n")
            current_meaning = current_meaning.next
        
        _save_node(node.right, file)

def main():
    hash_dictionary = load_dictionary("N21DCCN035_Hash.txt")
    while True:
        print("\nTừ điển Anh-Anh")
        print("1. Thêm từ mới")
        print("2. Xóa từ")
        print("3. Tra cứu từ")
        print("4. Lưu từ điển")
        print("5. Nạp từ điển")
        print("6. Thoát")
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            word = input("Nhập từ: ")
            part_of_speech = input("Nhập loại từ: ")
            definition = input("Nhập nghĩa của từ: ")
            example = input("Nhập ví dụ: ")
            hash_dictionary.add_word(word, part_of_speech, definition, example)
        elif choice == '2':
            word = input("Nhập từ cần xóa: ")
            meanings = hash_dictionary.lookup_word(word)
            if meanings:
                hash_dictionary.remove_word(word)
                print(f"Đã xóa từ {word}.")
            else:
                print(f"Không tìm thấy từ {word}.")
            
        elif choice == '3':
            word = input("Nhập từ cần tra cứu: ")
            meanings = hash_dictionary.lookup_word(word)
            if meanings:
                for meaning in meanings:
                    print(f"Loại từ: {meaning[0]}, Nghĩa: {meaning[1]}, Ví dụ: {meaning[2]}")
            else:
                print(f'Không tìm thấy từ {word}')
        elif choice == '4':
            filename = input("Nhập tên file lưu: ")
            save_dictionary(hash_dictionary, filename)
            print("Đã lưu từ điển")
        elif choice == '5':
            filename = input("Nhập tên file nạp: ")
            hash_dictionary = load_dictionary(filename)
            print("Đã nạp từ điển")
        elif choice == '6':
            print("See you later!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

if __name__ == "__main__":
    main()
    

        
   

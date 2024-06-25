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

class BSTDictionary:
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
            node.right = self.delete(node.right, temp.word)
        return node

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

# Đọc dữ liệu từ file
def load_dictionary(file):
    bst = BSTDictionary()
    with open(file, 'r', encoding='utf-8') as fi:
        for line in fi:
            parts = line.strip().split("`$")
            word = parts[0]
            meaning = {'part_of_speech': parts[1], 'definition': parts[2], 'example': parts[3]}
            node = bst.lookup_word(word)
            # Tìm node chứa từ, nếu có thì thêm nghĩa, chưa có thì thêm vào cây sau đó thêm nghĩa
            if node:
                node.add_meaning(meaning['part_of_speech'], meaning['definition'], meaning['example'])
            else:
                bst.insert(word)
                node = bst.lookup_word(word)
                node.add_meaning(meaning['part_of_speech'], meaning['definition'], meaning['example'])
    return bst

# 4.Lưu từ điển vào file
def inorder_traversal(node, file):
    if node is not None:
        # Duyệt cây con bên trái
        inorder_traversal(node.left, file)
        
        # ghi thông tin từ và nghĩa của nút hiện tại vào file
        current = node.meanings
        while current is not None:
            file.write(f"{node.word}`${current.part_of_speech}`${current.definition}`${current.example}\n")
            current = current.next
        
        # Duyệt cây con bên phải
        inorder_traversal(node.right, file)

def save_dictionary(bst_dictionary, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        if bst_dictionary.root is not None:
            inorder_traversal(bst_dictionary.root, file)

def main():
    bst = load_dictionary("N21DCCN035_BST.txt")
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
            node = bst.lookup_word(word)
            if node:
                node.add_meaning(part_of_speech, definition, example)
            else:
                bst.insert(word)
                node = bst.lookup_word(word)
                node.add_meaning(part_of_speech, definition, example)
        elif choice == '2':
            word = input("Nhập từ cần xóa: ")
            if bst.remove_word(word):
                print("Đã xóa từ:", word)
            else:
                print(f'Không tìm thấy từ {word}')
        elif choice == '3':
            word = input("Nhập từ cần tra cứu: ")
            node = bst.lookup_word(word)
            if node:
                current = node.meanings
                while current is not None:
                    print(f"Loại từ: {current.part_of_speech}, Nghĩa: {current.definition}, Ví dụ: {current.example}")
                    current = current.next
            else:
                print(f'Không tìm thấy từ {word}')
        elif choice == '4':
            filename = input("Nhập tên file lưu: ")
            save_dictionary(bst, filename)
            print("Đã lưu từ điển")
        elif choice == '5':
            filename = input("Nhập tên file nạp: ")
            bst = load_dictionary(filename)
            print("Đã nạp từ điển")
        elif choice == '6':
            print("See you later!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

if __name__ == "__main__":
    main()



class Meaning:
    def __init__(self, part_of_speech, definition, example):
        self.part_of_speech = part_of_speech
        self.definition = definition
        self.example = example
        self.next = None

class Dictionary:
    def __init__(self, word) -> None:
        self.word = word
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

    # Hiển thị thông tin của từ
    def __str__(self) -> str:
        result = f"Từ: {self.word}\n"
        current = self.meanings
        while current is not None:
            result += f"Loại từ: {current.part_of_speech}, Nghĩa: {current.definition} - Ví dụ: {current.example}\n"
            current = current.next
        return result
    
# 5.Đọc dữ liệu từ file
def load_dictionary(file):
    dictionary = []
    with open(file, 'r') as fi:
        current_word = None
        for line in fi:
            parts = line.strip().split("`$")
            # kiểm tra current_word là None hoặc từ hiện tại không giống với từ đầu tiên trong phần của dòng đang xét
            if not current_word or current_word.word != parts[0]:
                # Nếu từ đang xét khác None, thêm nó vô dictionary
                if current_word:
                    dictionary.append(current_word)
                # Tạo một đối tượng Dictionary với các tham số meanings
                current_word = Dictionary(parts[0])
            current_word.add_meaning(parts[1], parts[2], parts[3])
        # Đảm bảo từ cuối cùng được thêm vào dictionary
        if current_word:
            dictionary.append(current_word)
    return dictionary

# 4.Lưu từ điển vào file
def save_dictionary(dictionary, file):
    with open(file, 'w', encoding='utf-8') as fi:
        for entry in dictionary:
            current = entry.meanings
            while current is not None:
                fi.write(f"{entry.word}`${current.part_of_speech}`${current.definition}`${current.example}\n")
                current = current.next


# 1.Thêm một từ điển vào list
def add_dictionary_entry(dictionary, word, part_of_speech, definition, example):
    # Duyệt qua list dictionary, nếu từ đã có thì thêm vào phần meanings
    for e in dictionary:
        if e.word == word:
            e.add_meaning(part_of_speech, definition, example)
            return
    # Chưa có từ trong dictionary thì tạo đối tượng mới
    new_entry = Dictionary(word)
    new_entry.add_meaning(part_of_speech, definition, example)
    # Thêm vào list từ điển
    dictionary.append(new_entry)

# 2.Xóa từ điển khỏi list
def remove_word(dictionary, word):
    is_removed = False
    for dictionary_obj in dictionary:
        if dictionary_obj.word == word:
            dictionary.remove(dictionary_obj)
            is_removed = True
            break
    if is_removed:
        print(f"Đã xóa từ '{word}' trong từ điển")
    else:
        print(f"Từ '{word}' không có trong từ điển")

# 3.Xem các nghĩa của từ điển trong list
def lookup_word(dictionary, word):
    found_word = False
    for dictionary_obj in dictionary:
        if dictionary_obj.word == word:
            print(dictionary_obj)
            found_word = True
            break
    if not found_word:
        print(f"Không tìm thấy từ: {word}")    


def main():
    dictionary = load_dictionary("N21DCCN035_array.txt")
    while True:
        print("\nTừ điển Anh-Anh:")
        print("1. Thêm từ mới")
        print("2. Xóa từ")
        print("3. Tra từ")
        print("4. Lưu từ điển")
        print("5. Nạp từ điển")
        print("6. Thoát")
        choice = input("Nhập lựa chọn: ")

        if choice == "1":
            word = input("Nhập từ cần thêm: ")
            part_of_speech = input("Loại từ: ")
            definition = input("Nghĩa: ")
            example = input("Ví dụ: ")
            add_dictionary_entry(dictionary, word, part_of_speech, definition, example)
        elif choice == "2":
            word = input("Nhập từ cần xóa: ")
            remove_word(dictionary, word)
        elif choice == "3":
            word = input("Nhập từ muốn tìm: ")
            lookup_word(dictionary, word)
        elif choice == "4":
            save_dictionary(dictionary, "N21DCCN035_array.txt")
            print("Đã lưu từ điển")
        elif choice == "5":
            dictionary = load_dictionary("N21DCCN035_array.txt")
            print("Đã nạp từ điển")
        elif choice == "6":
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại")


if __name__ == "__main__":
    main()
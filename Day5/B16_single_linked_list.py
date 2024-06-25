class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        # Khởi tạo head và tail
        self.head = None
        self.tail = None
        # Độ dài
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        # Duyệt đến cuối dslk
        while temp_node:
            result += str(temp_node.data)
            # Nếu còn node tiếp theo
            if temp_node.next:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        # Nếu chưa có node nào, gắn tail và head là node đó
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # Nếu có rồi thì gắn vào tail
        else:
            self.tail.next = new_node
            self.tail = new_node
        # Tăng độ dài của dslk lên 1
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        # Chưa có node thì khởi tạo head và tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # Đã có node -> gắn node mới vào head, new_node trỏ tới head
        else:
            new_node.next = self.head
            self.head = new_node
        # Tăng độ dài thêm 1
        self.length += 1
    
    def insert(self, index, value):
        new_node = Node(value)
        # Nếu index = 0 thì dùng prepend
        if index == 0:
            self.prepend(value)
        # index = length => dùng append
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            temp_node = self.head
            # Duyệt đến node trước vị trí
            for _ in range(index - 1):
                temp_node = temp_node.next
            # Gắn next của new node là next của temp
            # VD: 1 - 2 - 3 - 5, chèn 4 vào vị trí 3
            # Gắn next của 4 là 5, sau đó gắn next của 3 là 4
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length += 1
    
    # Hàm này tương tự hàm __str__
    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def search(self, target):
        current = self.head
        index = 0
        # Duyệt tuần tự từ đầu ds
        while current:
            if current.data == target:
                return index
            current = current.next
            index += 1
        # Không tìm thấy thì trả về -1
        return -1
    
    def get(self, index):
        # Lấy index tương tự như các kiểu khác (-1 là cuối cùng)
        if index == -1:
            return self.tail
        # Ngoại lệ
        elif index < -1 or index >= self.length:
            return None
        current = self.head
        # Duyệt từ đầu đến index để lấy node cần tìm
        for _ in range(index):
            current = current.next
        return current
    
    def set_value(self, index, value):
        # Dùng get để lấy node đang cần
        temp = self.get(index)
        # Nếu temp không phải None
        if temp:
            temp.data = value
            return True
        # Trả về false nếu không set thành công
        return False
    
    def pop_first(self):
        # ds trống, không làm gì cả
        if self.length == 0:
            return None
        popped_node = self.head
        # Nếu ds có 1 node duy nhất => gắn head và tail là None
        if self.length == 1:
            self.head = self.tail = None
        # Ngược lại, gán head trỏ đến node tiếp theo
        # Cắt bỏ liên kết của head cũ
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        # Trả về kq của node đã xóa
        return popped_node
    
    
    
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            # Duyệt đến node kế cuối
            while temp.next is not self.tail:
                temp = temp.next
            # Gắn node kế cuối là tail, loại bỏ liên kết đến node cuối cùng
            temp.next = None
            self.tail = temp
        self.length -= 1
        return popped_node
    

    def remove(self, index):
        if index < -1 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == -1 or index == self.length-1:
            return self.pop()
        # node liền trước node cần xóa
        prev_node = self.get(index-1)
        # popped_node là node ta muốn xóa
        popped_node = prev_node.next
        # gán node liền trước trỏ tới node sau node cần xóa
        prev_node.next = popped_node.next
        # Loại bỏ liên kết next của node đang xóa
        popped_node.next = None
        self.length -= 1
        return popped_node
    


sll = SingleLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
print(sll)
sll.remove(0)
print(sll)



# Old version        
"""
class SingleLinkedList:
    def __init__(self):
        self.head = None

    # Chèn vào cuối
    def append(self, data):
        new_node = Node(data)
        # Chưa có head => Khởi tạo head
        if not self.head:
            self.head = new_node
            return
        
        # Gắn last_node = head rồi duyệt từ đầu tới cuối
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        # Chèn new_node vào cuối DSLK
        last_node.next = new_node

    # Hiển thị DSLK
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end='->')
            current_node = current_node.next
        print('Null')
     
    # Lấy độ dài của DSLK
    def get_size(self):
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.next
        return length
    
    # Chèn đầu DSLK
    def insert_front(self, data):
        new_node = Node(data)
        # Gắn next của new_node là head
        new_node.next = self.head
        # Gắn node head = new_node
        self.head = new_node

    # Chèn vị trí bất kỳ, quy ước vị trí đầu là 0
    def insert(self, data, pos):
        # Kiểm tra các trường hợp ngoại lệ
        if pos < 0 or pos > self.get_size():
            print('Vị trí không hợp lệ')
            return

        if pos == self.get_size():
            self.append(data)
            return

        if pos == 0:
            self.insert_front(data)
            return

        # Duyệt tới node trước pos
        node_tmp = self.head
        for i in range(pos - 1):
            node_tmp = node_tmp.next

        new_node = Node(data)
        new_node.next = node_tmp.next
        node_tmp.next = new_node
    
    # Xóa node đầu
    def pop_front(self):
        if self.head is None:
            print("DSLK rỗng, không cần xóa!")
            return
        self.head = self.head.next

    # Xóa node cuối
    def pop_back(self):
        if self.head is None:
            print("DSLK rỗng, không cần xóa!")
            return
        
        # Nếu chỉ có 1 node, thì đặt head = None
        if self.head.next is None:
            self.head = None
            return
        
        node_tmp = self.head
        # Duyệt đến node kế cuối
        while node_tmp.next.next is not None:
            node_tmp = node_tmp.next
        
        # Gắn con trỏ node cuối là None
        node_tmp.next = None

    # Xóa vị trí bất kỳ, quy ước ban đâu index = 0
    def delete(self, pos):
        # Kiểm tra các trường hợp ngoại lệ
        if pos < 0 or pos > self.get_size():
            print('Vị trí không hợp lệ')
            return

        if pos == 0:
            self.pop_front()
            return

        node_tmp = self.head
        # Truy vấn đến node trước node cần xóa
        for i in range(pos-1):
            node_tmp = node_tmp.next

        # Nếu node cần xóa là node cuối cùng
        # VD: 1->2->3->4->None(Null)
        # Ta đã truy vấn đến node 3, next sẽ trỏ đến 4, xét next của 4 có None không
        # Khi None (trường hợp này là None), ta gắn next của node 3 là None
        # Tức là 3 bây giờ là node cuối cùng (1->2->3->None) 
        if node_tmp.next.next is None:
            node_tmp.next = None
        else:
        # Xóa node ở vị trí pos
        # VD: 1->2->3->4, xóa node 2
        # Gắn next của node 1 trỏ đến node 3
            node_tmp.next = node_tmp.next.next

"""
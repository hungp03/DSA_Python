class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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


dslk = SingleLinkedList()
dslk.append(1)
dslk.append(2)
dslk.insert_front(0)
dslk.insert(6,2)
dslk.delete(2)
dslk.display()
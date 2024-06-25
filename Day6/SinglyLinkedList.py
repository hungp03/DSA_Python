class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ================================================================
# 1. Create Simple Singly Linked List
class SinglyLinkedList:
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
    
    # ================================================================
    # 2. Insertion at the Beginning of a Singly Linked List
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

    # ================================================================
    # 3. Insertion at the End of a Singly Linked List
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
    
    # ================================================================
    # 4. Deletion from a Singly Linked List
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
    
    # ================================================================
    # 5. Reverse a Singly Linked List
    def reverse(self):
    # prev: Node trước node current
    # mặc định là None vì current đang là node head
    # next_node: node sau current
        prev = None
        current = self.head
    # Trỏ next_node đến node kế sau current
    # Node kế sau current trỏ về prev
    # prev trỏ tới current và current chuyển tới node tiếp theo
    # VD: 1 - 2 - 3 - 4
    # B1: prev = 1, current = 2
    # B2: prev = 2, current = 3
    # B3: prev = 3, current = 4
    # B4: prev = 4, current = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
    # current = None thì gắn head = prev -> 4 - 3 - 2 -1
        self.head = prev
        # self.head, self.tail = self.tail, self.head

    
    # ================================================================
    # 6. Middle of a Singly Linked List
    def find_middle(self):
        # Nếu dslk không có thì trả về none
        if self.head is None:
            return None
        if self.length == 1:
            return self.head
        else:
            # Lấy data của node
            return self.get(self.length // 2).data
            # Lấy cả node
            # return self.get(self.length // 2)
        
    # ================================================================
    # 7. Remove Duplicates from a Singly Linked List
    def remove_duplicate(self):
        if self.head is None or self.length == 0:
            return None
        # Tạo 1 set chứa các node, mỗi giá trị chỉ xuất hiện 1 lần
        visited = set()

        current = self.head
        prev = None

        while current:
            # nếu node.data chưa xuất hiện trong set
            if current.data not in visited:
                visited.add(current.data)
                # Gán prev bằng node hiện đang duyệt 
                prev = current
                current = current.next
            # Nếu đã xuất hiện, loại bỏ node đang duyệt (prev trỏ tới node tiếp theo)
            else:
                prev.next = current.next
                current = current.next
                self.length -= 1
    
    # ================================================================
    # 8. Merge Two Sorted Linked List
    def merge_two_list(self, other):
        if self.head is None:
            return other.head
        if other.head is None:
            return self.head
        
        # Tạo một node tmp để bắt đầu duyệt
        tmp = Node(None)
        current = tmp

        ptr1, ptr2 = self.head, other.head

        # Duyệt qua cả hai danh sách và gộp
        while ptr1 and ptr2:
            if ptr1.data < ptr2.data:
                current.next = ptr1
                ptr1 = ptr1.next
            else:
                current.next = ptr2
                ptr2 = ptr2.next
            current = current.next

        if ptr1:
            current.next = ptr1
        else:
            current.next = ptr2

        return tmp.next
    
    # ================================================================
    # 9. Remove Duplicates
    def remove_duplicates_head(self, head_ll):
        if not head_ll:
            return None
        current = head_ll
        # Check 2 nút cạnh nhau xem có bằng nhau không
        while current and current.next:
            if current.data == current.next.data:
                # Nếu bằng, ta loại bỏ liên kết của nút curent và current.next
                # VD: 1-2-2-3 -> 1-2-3
                current.next = current.next.next
                self.length -= 1
            else:
                # Nếu không bằng, ta duyệt như bình thường
                current = current.next
        return head_ll

    # ================================================================
    # 10. Remove Linked List Elements Use head
    def remove_elements_head(self, head_ll, val):
        if not head_ll:
            return None

        current = head_ll
        # Duyệt qua dslk và loại bỏ node có giá trị bằng val
        while current and current.next:
            if current.next.data == val:
                current.next = current.next.next
                self.length -= 1
            else:
                current = current.next
        return head_ll
    
    # ================================================================
    # 11. Reverse linked list by head of list
    def reverse_linked_list(self, head_ll):
        if not head_ll:
            return None
        
        prev = None
        current = head_ll
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    # ================================================================
    # 12. Palindrome Linked List
    def is_palirome_linked_list(self, head_ll):
        if not head_ll:
            return None
        reverse_head = self.reverse_linked_list(head_ll)
        while head_ll and reverse_head:
            if head_ll.data != reverse_head.data:
                return False
            head_ll = head_ll.next
            reverse_head = reverse_head.next
        return True
    
    # ================================================================
    # 13. Middle of the Linked List
    def find_middle_use_head(self, head_ll):
        slow = head_ll
        fast = head_ll
        # Cho slow di chuyển 1 thì fast di chuyển 2
        # Khi fast đến cuối thì slow ở giữa
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
        
# ================================================================
# Bai 8
# ll1 = SinglyLinkedList()
# ll1.append(1)
# ll1.append(2)
# ll1.append(4)

# ll2 =  SinglyLinkedList()
# ll2.append(1)
# ll2.append(3)
# ll2.append(4)

# print("List 1:", ll1)
# print("List 2:", ll2)

# merged_list = SinglyLinkedList()
# merged_list.head = ll1.merge_two_list(ll2)
# print("Merged List:", merged_list)

# ================================================================
# Bai 9
# ll1 = SinglyLinkedList()
# ll1.append(1)
# ll1.append(2)
# ll1.append(2)
# ll1.append(4)
# print("Original List:", ll1)
# ll1.head = ll1.remove_duplicates_head(ll1.head)
# print("List after deleting duplicates:", ll1)

# ================================================================
# Bai 10
# ll = SinglyLinkedList()
# ll.append(1)
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(3)
# print("Original List:", ll)
# ll.head = ll.remove_elements_head(ll.head, 1)
# print("List after deleting node:", ll)
    
# ================================================================
# Bai 11
# ll = SinglyLinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.append(5)
# print("Original List:", ll)
# ll.head = ll.reverse_linked_list(ll.head)
# print("List after reverse:", ll)
    
# ================================================================
# Bai 12
# ll = SinglyLinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(2)
# ll.append(5)
# print(ll.is_palirome_linked_list(ll.head))
    
# ================================================================
# Bai 13
# ll = SinglyLinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(2)
# print(ll.find_middle_use_head(ll.head))
class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class DSLK:
    def __init__(self):
        self.head = None

    # Phương thức in ngược danh sách liên kết dùng đệ qui
    def in_nguoc_recursive(self, node):
        if node is None:
            return
        self.in_nguoc_recursive(node.next)
        print(node.info, end=' ')

    def in_nguoc_non_recursive(self):
        if self.head is None:
            return

        stack = []
        current = self.head

        while current:
            stack.append(current.info)
            current = current.next

        while stack:
            print(stack.pop(), end=' ')

    def dao_nguoc(self):
        if self.head is None:
            return

        stack = []
        current = self.head

        while current:
            stack.append(current)
            current = current.next

        self.head = stack.pop()
        temp = self.head

        while stack:
            temp.next = stack.pop()
            temp = temp.next

        temp.next = None

    def print(self):
        current = self.head
        while current:
            print(current.info, end=' ')
            current = current.next
        print()

dslk = DSLK()
dslk.head = Node(1)
dslk.head.next = Node(2)
dslk.head.next.next = Node(3)

print("In ngược danh sách liên kết dùng đệ qui:")
dslk.in_nguoc_recursive(dslk.head)
print()

print("In ngược danh sách liên kết không dùng đệ qui:")
dslk.in_nguoc_non_recursive()

dslk.dao_nguoc()

print("\nDanh sách liên kết sau khi đảo ngược:")
dslk.print()

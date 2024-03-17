class Node:
    def __init__(self, value):
        self.value = value
        self.next = None       

# Khi tạo Stack bằng DSLK thì thêm(push) ở đầu DSLK và xóa cũng vậy
class Stack:
    def __init__(self):
        self.top = None
        self.height = 0

    def __str__(self):
        res = ""
        temp = self.top
        while temp is not None:
            res += str(temp.value) + '\n'
            temp = temp.next
        return res.strip()

    def isEmpty(self):
        return self.height == 0
    
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        tmp = self.top
        self.top = self.top.next
        self.height -= 1
        tmp.next = None
        return tmp
    
    # peek: lấy phần tử đầu tiên trong Stack
    # là phần tử cuối cùng trong DSLK
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        tmp = self.top
        while tmp.next:
            tmp = tmp.next
        return tmp.value
    
    def delete(self):
        self.top = None
        self.height = 0
        
s = Stack()
s.push(7)
s.push(5)
s.push("asn")
print(s)
print(s.peek())


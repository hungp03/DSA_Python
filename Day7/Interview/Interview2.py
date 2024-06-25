class Node:
    def __init__(self, value, next=None, min_value=None):
        self.value = value
        self.next = next
        self.min_value = min_value

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
        if self.isEmpty():
            new_node = Node(value, min_value=value)
        else:
            new_node = Node(value, self.top, min(value, self.top.min_value))
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        self.height -= 1
        return value

    def min(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        return self.top.min_value

s = Stack()
s.push(5)
s.push(6)
s.push(3)
s.push(7)
print(s)
print("Min:", s.min())
s.pop()
s.pop()
print(s)
print("Min:", s.min())
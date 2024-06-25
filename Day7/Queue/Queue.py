class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def __str__(self):
        result = ""
        temp = self.first
        while temp is not None:
            result += str(temp.value) + " "
            temp = temp.next
        return result

    def isEmpty(self):
        return self.length == 0
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        tmp = self.first
        if self.length == 1:
            self.first = self.last = None
        else:
            self.first = self.first.next
            tmp.next = None
        self.length -= 1
        return tmp

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.first.value
    
    def delete(self):
        self.first = self.last = None
        self.length = 0
    
# q = Queue(6)
# q.enqueue(5)
# q.enqueue(10)
# print(q)
# print(q.isEmpty())
# print(q.peek())
# q.delete()
# print(q.isEmpty())

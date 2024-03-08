from SinglyLinkedList import SinglyLinkedList as sll

# Class LinkedListSolution coi như là class mở rộng của sll
class LinkedListSolution(sll):
    def partition(self, x):
        # Tư tưởng: tạo 2 dslk nhỏ, một ds chứa các node có giá trị nhỏ hơn x
        # ds còn lại chứa các node có giá trị lớn hơn hoặc bằng x
        smaller = sll()
        greater_and_equals = sll()

        current = self.head
        while current:
            if current.data < x:
                smaller.append(current.data)
            else:
                greater_and_equals.append(current.data)
            current = current.next
        
        if smaller.head:
            smaller.tail.next = greater_and_equals.head
            return smaller
        else:
            return greater_and_equals
        
    
ll = LinkedListSolution()
ll.append(6)
ll.append(11)
ll.append(8)
ll.append(15)
ll.append(10)
ll.append(7)
ll.append(12)

partition_ll = ll.partition(10)
print(partition_ll)

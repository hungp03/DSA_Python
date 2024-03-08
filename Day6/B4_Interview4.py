from SinglyLinkedList import SinglyLinkedList as sll

# Class LinkedListSolution coi như là class mở rộng của sll
class LinkedListSolution(sll):
    def sum_lists(self, other):
        self.reverse()
        other.reverse()
        num1, num2 = linked_list_tonum(self), linked_list_tonum(other)
        res = create_linked_list(num1 + num2)
        res.reverse()
        return res

# Hàm để tạo dslk từ một số
def create_linked_list(num):
    tmp = sll()
    for digit in str(num):
        tmp.append(int(digit))
    return tmp

# Hàm để chuyển đổi dslk thành số
def linked_list_tonum(ll):
    num = 0
    current = ll.head
    while current:
        num = num * 10 + current.data
        current = current.next
    return num


ll1 = LinkedListSolution()
ll1.append(7)
ll1.append(1)
ll1.append(6)

ll2 = LinkedListSolution()
ll2.append(5)
ll2.append(9)
ll2.append(2)


print(ll1.sum_lists(ll2))

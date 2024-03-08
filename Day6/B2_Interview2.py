from SinglyLinkedList import SinglyLinkedList as sll

# Class LinkedListSolution coi như là class mở rộng của sll
class LinkedListSolution(sll):
    # Hàm trả về phần tử thứ n từ tail ngược lại
    def fid_nth_last(self, n):
        # Nếu n lớn hơn length của dslk
        if n > self.length:
            return None
        # Tư tưởng: sử dụng độ dài của dslk - n để trả về index
        # Dùng hàm get để lấy node
        # VD: 1-2-3-4-5-6, length = 6, n = 2 thì index = 4 tương đương node 5
        idx = self.length - n
        return self.get(idx).data
    
# Test
ll = LinkedListSolution()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
print(ll.fid_nth_last(2))
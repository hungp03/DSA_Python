from SinglyLinkedList import SinglyLinkedList as sll

# Class LinkedListSolution coi như là class mở rộng của sll
class LinkedListSolution(sll):
    # Phương thức remove_duplicate đã bao gồm cả trường hợp không sắp xếp
    # Nhưng vẫn viết lại cho nhớ 😉
    def remove_duplicate_unsorted(self):
        # Ràng buộc
        if not self.head:
            return None
        # Tạo một set chứa giá trị duy nhất xuất hiện trong sll
        visited = set()

        current = self.head
        prev = None
        while current:
            # Nếu đã xuất hiện, loại bỏ node đang duyệt (prev trỏ tới node tiếp theo)
            if current.data in visited:
                self.length -= 1
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                current = current.next
                
             # nếu node.data chưa xuất hiện trong set
            else:
                visited.add(current.data)
                # Gán prev bằng node hiện đang duyệt 
                prev = current
                current = current.next

ll = LinkedListSolution()

ll.append(4)
ll.append(5)
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(3)
ll.append(4)
ll.remove_duplicate_unsorted()
print(ll)

# Tư tưởng: tạo 2 stack (1 dùng cho việc thêm vào queue)
# 1 dùng cho xóa khỏi queue
class Queue:
    def __init__(self):
        self.s_in = []
        self.s_out = []

    def __str__(self) -> str:
        tmp_in = [str(_) for _ in self.s_in]
        # print("in",list(tmp_in))
        tmp_out = [str(_) for _ in reversed(self.s_out)]
        # print("out", list(tmp_out))
        return " ".join(tmp_out + tmp_in)



    def enqueue(self, val):
        self.s_in.append(val)
    
    def dequeue(self):
        self.move()
        if not self.s_out:
            raise IndexError("Dequeue from empty queue")
        return self.s_out.pop()
    
    # chuyển dữ liệu từ stack in sang stack out
    # đảm bảo khi lấy thì s_out phải có dữ liệu
    def move(self):
        if not self.s_out:
            while self.s_in:
                self.s_out.append(self.s_in.pop())
            
    # hàm peek để lấy phần tử cuối cùng thêm vào
    def peek(self):
        self.move()
        if not self.stack_out:
            raise IndexError("Peek from empty queue")
        return self.stack_out[-1]
    
    def isEmpty(self):
        return len(self.s_in) == 0 and len(self.s_out) == 0
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q)
q.dequeue()
print(q)

    


# Triển khai 3 Stack từ 1 list bằng cách chia list làm 3 phần
class TripleStack:
    def __init__(self):
        self.list = []
        self.length = [0,0,0]
    
    # stack_num: số thứ tự của stack, bắt đầu từ 0
    # getTopIndex: xác định vị trí đầu tiên của stack trong list chung
    # VD: có 3 stack với length = [2,3,2], chọn stack 3
    # return 2 + 3 + 2 - 1 = 6 => index đầu tiên của stack 3(0 -1 -2) là 6
    def getTopIndex(self, stack_num):
        return sum(self.length[:stack_num + 1]) - 1

    def push(self, stack_num, val):
        index = self.getTopIndex(stack_num) + 1
        self.list.insert(index, val)
        self.length[stack_num] += 1
    
    def pop(self, stack_num):
        if self.length[stack_num] == 0:
            return f"Stack {stack_num} is empty"
        index = self.getTopIndex(stack_num)
        val = self.list.pop(index)
        self.length[stack_num] -= 1
        return val


if __name__ == "__main__":
    ts = TripleStack()
    ts.push(0, "abc")
    ts.push(1, "def")
    ts.push(2, "ghi")
    ts.push(2, "jkl")
    print(ts.pop(0)) 
    print(ts.pop(1))
    print(ts.pop(2))
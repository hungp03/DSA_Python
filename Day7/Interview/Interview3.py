# Phân tích đề bài:
# - Ta phải kiểm soát độ lớn của stack
# - Tư tưởng: tạo stack mới khi stack cũ vượt quá mức quy định
# - Tạo SetOfStacks sẽ bao gồm nhiều ngăn xếp con
# - Các phương thức pop, push sử dụng trong SetOfStacks như 1 stack duy nhất
class SetOfStacks:
    def __init__(self, threshold):
        # set ngưỡng tối đa cho 1 stack
        self.threshold = threshold
        # Danh sách các stack con
        self.stacks = [[]]
    
    def push(self, value):
        # kiểm tra stack cuối cùng đã max chưa
        if len(self.stacks[-1]) >= self.threshold:
            # Chèn 1 list (stack mới)
            self.stacks.append([])
        # Thêm value vào stack cuối cùng
        self.stacks[-1].append(value)
    
    def pop(self):
        # kiểm tra stack cuối cùng có rỗng không
        if not self.stacks[-1]:
            # Nếu có thì loại bỏ stack cuối
            self.stacks.pop()
        # Lấy giá trị từ ngăn xếp cuối cùng
        if self.stacks:
            return self.stacks[-1].pop()
        else:
            return "SetOfStack is Empty"
    
    def __str__(self):
        stack_strings = [f"Stack {i + 1}: {stack}" for i, stack in enumerate(self.stacks)]
        return "\n".join(stack_strings)
    

stacks = SetOfStacks(threshold=3)
stacks.push(1)
stacks.push(2)
stacks.push(3)
stacks.push(4)
stacks.push(5)
stacks.dp()
print(stacks)
print(stacks.pop()) 
print(stacks.pop()) 


class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    ## WRITE STACK CONSTRUCTOR HERE ##
    def __init__(self, value):
        self.top = Node(value)
        self.height = 1





my_stack = Stack(4)

print('Top:', my_stack.top.value)
print('Height:', my_stack.height)



"""
    EXPECTED OUTPUT:
    ----------------
    Top: 4
    Height: 1

"""
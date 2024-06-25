class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    ## WRITE QUEUE CONSTRUCTOR HERE ##
    def __init__(self, val):
        tmp = Node(val)
        self.first = tmp
        self.last = tmp
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next




my_queue = Queue(4)

my_queue.print_queue()



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""
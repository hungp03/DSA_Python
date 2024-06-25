class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        # Nếu cây rỗng -> gắn vào root
        if self.root is None:
            self.root = new_node
            return True
        
        tmp = self.root
        while tmp:
            if value == tmp.value:
                return False
            if value < tmp.value:
                if tmp.left is None:
                    tmp.left = new_node
                    return True
                tmp = tmp.left
            else:
                if tmp.right is None:
                    tmp.right = new_node
                    return True
                tmp = tmp.right
            
    def contains(self, value):
        tmp = self.root
        while tmp:
            if value == tmp.value:
                return True

            elif value < tmp.value:
                tmp = tmp.left
            else:
                tmp = tmp.right
        return False


def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=' ')
        inorder_traversal(node.right)
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(7)
bst.insert(12)
bst.insert(3)



print("Binary Search Tree: ", end="")
inorder_traversal(bst.root)
print("\n----------")
print(bst.contains(7))  # True
print(bst.contains(11))  # False
    
        
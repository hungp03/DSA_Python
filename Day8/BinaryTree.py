from queue import Queue

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None

def NLR(root):
    if not root:
        return
    print(root.data)
    NLR(root.leftChild)
    NLR(root.rightChild)


def LNR(root):
    if not root:
        return
    LNR(root.leftChild)
    print(root.data)
    LNR(root.rightChild)


def LRN(root):

    if not root:
        return
    LRN(root.leftChild)
    LRN(root.rightChild)
    print(root.data)
    
def levelOrderTraversal(root):
    if not root:
        return
    else:
        q = Queue()
        q.put(root)
        while not q.empty():
            r = q.get()
            print(r.data)
            if r.leftChild is not None:
                q.put(r.leftChild)
            if r.rightChild is not None:
                q.put(r.rightChild)
                
def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "The BT does not exist"
    else:
        q = Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            if root.data == nodeValue:
                return "Success"
            if (root.leftChild is not None):
                q.put(root.leftChild)
            
            if (root.rightChild is not None):
                q.put(root.rightChild)
        return "Not found"

def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        q = Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            if root.leftChild is not None:
                q.put(root.leftChild)
            else:
                root.leftChild = newNode
                return "Successfully Inserted"
            if root.rightChild is not None:
                q.put(root.rightChild)
            else:
                root.rightChild = newNode
                return "Successfully Inserted"

def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        q = Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            if (root.leftChild is not None):
                q.put(root.leftChild)
            
            if (root.rightChild is not None):
                q.put(root.rightChild)
        deepestNode = root
        return deepestNode

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        q = Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            if root is dNode:
                root = None
                return
            if root.rightChild:
                if root.rightChild is dNode:
                    root.rightChild = None
                    return
                else:
                    q.put(root.rightChild)
            if root.leftChild:
                if root.leftChild is dNode:
                    root.leftChild = None
                    return
                else:
                    q.put(root.leftChild)

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "The BT does not exist"
    else:
        q = Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            if root.data == node:
                dNode = getDeepestNode(rootNode)
                root.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "The node has been successfully deleted"
            if (root.leftChild is not None):
                q.put(root.leftChild)
            
            if (root.rightChild is not None):
                q.put(root.rightChild)
        return "Failed to delete"

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT has been successfully deleted" 
            

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild


LNR(newBT)
print('------------------')
levelOrderTraversal(newBT)
print(searchBT(newBT, "Coffee"))
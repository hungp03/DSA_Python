from collections import deque

class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None
    
class Cay:
    def __init__(self):
        self.root = None

    def SoNut(self, root):
        if root is None:
            return 0
        else:
            return self.SoNut(root.left) + self.SoNut(root.right) + 1

    def ChieuCao(self, root):
        if root is None:
            return 0
        else:
            return max(self.ChieuCao(root.left), self.ChieuCao(root.right)) + 1
    
    def SoNutLa(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        else:
            return self.SoNutLa(root.left) + self.SoNutLa(root.right)
    
    def SoNutTrungGian(self, root):
        if root is None or (root.left is None and root.right is None):
            return 0
        if root.left is not None and root.right is not None:
            return 1 + self.SoNutTrungGian(root.left) + self.SoNutTrungGian(root.right)
        else:
            return self.SoNutTrungGian(root.left) + self.SoNutTrungGian(root.right)
    
    def KiemTraBST(self, root, min_val=float('-inf'), max_val=float('inf')):
        if root is None:
            return True

        if root.info <= min_val or root.info >= max_val:
            return False

        return (self.KiemTraBST(root.left, min_val, root.info) and self.KiemTraBST(root.right, root.info, max_val))
    
    def KiemTraAVL(self):
        def KiemTraCayAVL(node):
            if node is None:
                return True

            chieucao_trai = self.ChieuCao(node.left)
            chieucao_phai = self.ChieuCao(node.right)

            if abs(chieucao_trai - chieucao_phai) > 1:
                return False

            return KiemTraCayAVL(node.left) and KiemTraCayAVL(node.right)

        return KiemTraCayAVL(self.root)
    
    def Chep(self):
        def SaoChep(node):
            if node is None:
                return None

            new_node = Node(node.info)
            new_node.left = SaoChep(node.left)
            new_node.right = SaoChep(node.right)

            return new_node

        new_cay = Cay()
        new_cay.root = SaoChep(self.root)
        return new_cay
    
    def _print_tree(self, node, level=0):
        result = ""
        if node.right:
            result += self._print_tree(node.right, level + 1)
        result += "\t" * level + str(node.info) + "\n"
        if node.left:
            result += self._print_tree(node.left, level + 1)
        return result

    def __str__(self):
        if self.root is None:
            return "Cây rỗng"
        return self._print_tree(self.root)
    
    def _so_sanh_cay(self, node1, node2):
        # Nếu cả hai nút đều là None --> giống nhau
        if node1 is None and node2 is None:
            return True
        # Nếu một trong hai nút là None, hoặc giá trị không bằng nhau --> không giống nhau
        if node1 is None or node2 is None or node1.info != node2.info:
            return False
        # So sánh các cây con của từng nút
        return (self._so_sanh_cay(node1.left, node2.left) and
                self._so_sanh_cay(node1.right, node2.right))

    def SoSanh(self, cay2):
        # Bắt đầu so sánh từ gốc của hai cây
        return self._so_sanh_cay(self.root, cay2.root)

    def _kiem_tra_cay_con(self, node1, node2):
        # Nếu cây con là None, là cây con của cây cha
        if node2 is None:
            return True
        # Nếu cây cha là None nhưng cây con không phải là Non
        if node1 is None:
            return False
        # Kiểm tra nếu node hiện tại của cây lớn giống cây con và kiểm tra tiếp các nhánh
        return (node1.info == node2.info and 
                self._kiem_tra_cay_con(node1.left, node2.left) and 
                self._kiem_tra_cay_con(node1.right, node2.right)) or \
               self._kiem_tra_cay_con(node1.left, node2) or \
               self._kiem_tra_cay_con(node1.right, node2)


    def CayCon(self, cay2):
        if self.root is None:
            return False
        return self._kiem_tra_cay_con(self.root, cay2.root)
    
cay = Cay()
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)

print("Số nút của cây là:", cay.SoNut(cay.root))
print("Chiều cao của cây là:", cay.ChieuCao(cay.root))
print("Số nút lá:", cay.SoNutLa(cay.root))
print("Số nút trung gian:", cay.SoNutTrungGian(cay.root))
if cay.KiemTraBST(cay.root):
    print("Cây là một cây BST")
else:
    print("Cây không phải là một cây BST")

if cay.KiemTraAVL():
    print("Cây là một cây AVL")
else:
    print("Cây không phải là một cây AVL")

cay_copy = cay.Chep()
print(cay_copy)

cay2 = Cay()
cay2.root = Node(1)
cay2.root.left = Node(2)
cay2.root.right = Node(3)
cay2.root.left.left = Node(4)
cay2.root.left.right = Node(5)

cay3 = Cay()
cay3.root = Node(1)
cay3.root.left = Node(2)
cay3.root.right = Node(3)
cay3.root.left.left = Node(4)
cay3.root.left.right = Node(6)

print(cay.SoSanh(cay2)) 
print(cay.SoSanh(cay3))

cay4 = Cay()
cay4.root = Node(2)
cay4.root.left = Node(4)
cay4.root.right = Node(5)

cay5 = Cay()
cay5.root = Node(2)
cay5.root.left = Node(6)

print(cay.CayCon(cay4)) 
print(cay.CayCon(cay5))

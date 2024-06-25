class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.next = None

class DaThuc:
    def __init__(self):
        self.head = Node(None, None)
        self.head.next = self.head  # Head vòng

    def Them(self, heso, somu):
        new_node = Node(heso, somu)
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def RutGon(self):
        current = self.head.next
        while current != self.head:
            temp = current.next
            while temp != self.head:
                if temp.SoMu == current.SoMu:
                    current.HeSo += temp.HeSo
                    prev = current
                    while prev.next != temp:
                        prev = prev.next
                    prev.next = temp.next
                temp = temp.next
            if current.HeSo == 0:
                prev = self.head
                while prev.next != current:
                    prev = prev.next
                prev.next = current.next
                current = prev
            current = current.next

    def DoiDau(self):
        current = self.head.next
        while current != self.head:
            current.HeSo = -current.HeSo
            current = current.next

    def Tich(self, dathuc2):
        result = DaThuc()
        
        current1 = self.head.next
        while current1 != self.head:
            current2 = dathuc2.head.next
            while current2 != dathuc2.head:
                heso_tich = current1.HeSo * current2.HeSo
                somu_tich = current1.SoMu + current2.SoMu
                result.Them(heso_tich, somu_tich)
                current2 = current2.next
            current1 = current1.next
        
        result.RutGon()
        
        return result

    def Cong(self, dathuc2):
        result = DaThuc()
        
        current1 = self.head.next
        current2 = dathuc2.head.next
        
        while current1 != self.head and current2 != dathuc2.head:
            if current1.SoMu == current2.SoMu:
                heso_tong = current1.HeSo + current2.HeSo
                result.Them(heso_tong, current1.SoMu)
                current1 = current1.next
                current2 = current2.next
            elif current1.SoMu < current2.SoMu:
                result.Them(current1.HeSo, current1.SoMu)
                current1 = current1.next
            else:
                result.Them(current2.HeSo, current2.SoMu)
                current2 = current2.next
        
        while current1 != self.head:
            result.Them(current1.HeSo, current1.SoMu)
            current1 = current1.next
        
        while current2 != dathuc2.head:
            result.Them(current2.HeSo, current2.SoMu)
            current2 = current2.next
        
        result.RutGon()
        
        return result

    def Chep(self):
        new_dathuc = DaThuc()
        
        current = self.head.next
        while current != self.head:
            new_dathuc.Them(current.HeSo, current.SoMu)
            current = current.next
        
        return new_dathuc

    def print(self):
        current = self.head.next
        while current != self.head:
            print(f"{current.HeSo}x^{current.SoMu}", end=" ")
            current = current.next
        print()

# dathuc = DaThuc()
# dathuc.Them(2, 3)
# dathuc.Them(-1, 2)
# dathuc.Them(5, 0)

# dathuc_copy = dathuc.Chep()

# print("Đa thức ban đầu:")
# dathuc.print()

# print("Đa thức sao chép:")
# dathuc_copy.print()

# dathuc.RutGon()
# print("Đa thức sau khi rút gọn:")
# dathuc.print()

# dathuc.DoiDau()
# print("Đa thức sau khi đổi dấu:")
# dathuc.print()

# dathuc2 = DaThuc()
# dathuc2.Them(3, 2)
# dathuc2.Them(1, 1)


# dathuc_tich = dathuc.Tich(dathuc2)
# print("Đa thức tích:")
# dathuc_tich.print()

# dathuc_tong = dathuc.Cong(dathuc2)
# print("Đa thức tổng:")
# dathuc_tong.print()

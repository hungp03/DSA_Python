class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.next = None

class DaThuc:
    def __init__(self):
        self.head = None

    def Them(self, heso, somu):
        new_node = Node(heso, somu)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def print(self):
        current = self.head
        while current is not None:
            print(f"{current.HeSo}x^{current.SoMu}", end=" ")
            current = current.next
        print()
    
    def RutGon(self):
        current = self.head
        while current is not None:
            temp = current.next
            while temp is not None:
                if temp.SoMu == current.SoMu:
                    current.HeSo += temp.HeSo
                    current.next = temp.next
                temp = temp.next
            if current.HeSo == 0:
                self.XoaSoHang(current.SoMu)
            current = current.next

    def XoaSoHang(self, somu):
        current = self.head
        if current.SoMu == somu:
            self.head = current.next
        else:
            while current.next is not None:
                if current.next.SoMu == somu:
                    current.next = current.next.next
                    break
                current = current.next

    def Cong(self, dathuc2):
        result = DaThuc()
        
        current1 = self.head
        while current1 is not None:
            result.Them(current1.HeSo, current1.SoMu)
            current1 = current1.next
        current2 = dathuc2.head
        while current2 is not None:
            result.Them(current2.HeSo, current2.SoMu)
            current2 = current2.next
        result.RutGon()
        
        return result
    
    def DoiDau(self):
        current = self.head
        while current is not None:
            current.HeSo = -current.HeSo
            current = current.next

    def Tich(self, dathuc2):
        result = DaThuc()
        
        current1 = self.head
        while current1 is not None:
            current2 = dathuc2.head
            while current2 is not None:
                heso_tich = current1.HeSo * current2.HeSo
                somu_tich = current1.SoMu + current2.SoMu
                result.Them(heso_tich, somu_tich)
                current2 = current2.next
            current1 = current1.next
        
        result.RutGon()
        
        return result
    
    def Chep(self):
        new_dathuc = DaThuc()
        
        current = self.head
        while current is not None:
            new_dathuc.Them(current.HeSo, current.SoMu)
            current = current.next
        
        return new_dathuc
    
# dathuc = DaThuc()
# dathuc.Them(2, 3)
# dathuc.Them(-1, 2)
# dathuc.Them(5, 0)
# dathuc.Them(3, 2)

# print("Đa thức trước khi rút gọn:")
# dathuc.print()

# # Rút gọn đa thức
# dathuc.RutGon()

# print("Đa thức sau khi rút gọn:")
# dathuc.print()

# dathuc2 = DaThuc()
# dathuc2.Them(3, 2)
# dathuc2.Them(1, 1)
# dathuc2.Them(-2, 0)

# # Cộng hai đa thức và in kết quả
# dathuc_tong = dathuc1.Cong(dathuc2)
# print("Đa thức tổng:")
# dathuc_tong.print()


# dathuc1 = DaThuc()
# dathuc1.Them(2, 3)
# dathuc1.Them(-1, 2)

# dathuc2 = DaThuc()
# dathuc2.Them(3, 2)
# dathuc2.Them(1, 1)

# # Nhân hai đa thức và in kết quả
# dathuc_tich = dathuc1.Tich(dathuc2)
# print("Đa thức tích:")
# dathuc_tich.print()
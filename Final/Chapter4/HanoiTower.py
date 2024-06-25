class HanoiTower:
    def move_tower(self, n, from_rod, to_rod, aux_rod):
        if n == 1:
            print(f"Di chuyển tầng 1 từ tháp {from_rod} đến tháp {to_rod}")
            return
        self.move_tower(n-1, from_rod, aux_rod, to_rod)
        print(f"Di chuyển tầng {n} từ tháp {from_rod} đến tháp {to_rod}")
        self.move_tower(n-1, aux_rod, to_rod, from_rod)

hanoi_tower = HanoiTower()

# Di chuyển tháp Hanoi có 3 tầng từ tháp 1 đến tháp 3 thông qua tháp trung gian 2
n = 3
hanoi_tower.move_tower(n, '1', '3', '2')

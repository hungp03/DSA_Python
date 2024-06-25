from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        if v in self.graph:
            for i in self.graph[v]:
                if i < len(visited) and not visited[i]:
                    self.DFSUtil(i, visited)


    # Duyệt qua bằng DFS, nếu đi qua tất cả các đỉnh trong 1 lần duyệt thì là đồ thị liên thông
    def LienThong(self):
        V = len(self.graph)
        visited = [False] * V

        i = 0  # Khai báo biến i ở đây

        for i in range(V):
            if len(self.graph[i]) > 0:
                break

        if i == V - 1:
            return True

        self.DFSUtil(i, visited)

        for i in range(V):
            if not visited[i] and len(self.graph[i]) > 0:
                return False

        return True


    # Đếm số lần duyệt bằng DFS (hoặc BFS) --> số thành phần
    def SoThanhPhan(self):
        V = len(self.graph)
        visited = [False] * V
        count = 0

        for i in range(V):
            if not visited[i]:
                self.DFSUtil(i, visited)
                count += 1

        return count
    
    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.isCyclicUtil(neighbor, visited, recStack):
                    return True
            elif recStack[neighbor]:
                return True

        recStack[v] = False
        return False

    # Sử dụng DFS duyệt qua và đưa những đỉnh đã đi vào 1 stack
    # Nếu duyệt lại mà thấy đỉnh đó đã xuất hiện trong stack mà chưa đi hết thì đồ thị có chu trình
    def ChuTrinh(self):
        V = len(self.graph)
        visited = [False] * V
        recStack = [False] * V

        for node in range(V):
            if not visited[node]:
                if self.isCyclicUtil(node, visited, recStack):
                    return True

        return False
    
    # Nếu đỉnh nằm trong Graph thì đỉnh đó thuộc đồ thị
    def ChuaDinh(self, v):
        return v in self.graph
    
    # def BacDinh(self, v):
    #     if self.ChuaDinh(v):
    #         return len(self.graph[v])
    #     else:
    #         return "Đỉnh không tồn tại"
        
    def BacDinh(self, v):
        if self.ChuaDinh(v):
            in_degree = sum(neighbor == v for node in self.graph for neighbor in self.graph[node])
            out_degree = len(self.graph[v])
            return in_degree, out_degree
        else:
            return "Đỉnh không tồn tại"
    
    def SoCungVao(self, v):
        count = 0
        for node in self.graph:
            for neighbor in self.graph[node]:
                if neighbor == v:
                    count += 1
        return count
    
    def SoCungRa(self, v):
        return len(self.graph[v])
    
    def DuongDi(self, v1, v2):
        if not (self.ChuaDinh(v1) and self.ChuaDinh(v2)):
            return False
        
        visited = set()

        def DFS(v):
            if v == v2:
                return True
            visited.add(v)
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    if DFS(neighbor):
                        return True
            return False

        return DFS(v1)
    
dt = Graph()
dt.addEdge(0, 1)
dt.addEdge(0, 2)
dt.addEdge(1, 2)
dt.addEdge(3, 4)

if dt.LienThong():
    print("Đồ thị là đồ thị liên thông")
else:
    print("Đồ thị không phải là đồ thị liên thông")

print("Số thành phần liên thông của đồ thị là:", dt.SoThanhPhan())

if dt.ChuTrinh():
    print("Đồ thị có chu trình")
else:
    print("Đồ thị không có chu trình")

v = 5

if dt.ChuaDinh(v):
    print(f"Đỉnh {v} tồn tại trong đồ thị")
else:
    print(f"Đỉnh {v} không tồn tại trong đồ thị")

vertex = 2

in_degree, out_degree = dt.BacDinh(vertex)
print(f"Bán bậc vào của đỉnh {vertex} là {in_degree}")
print(f"Bán bậc ra của đỉnh {vertex} là {out_degree}")

# in_degree = dt.SoCungVao(vertex)
# print(f"Số cung vào đỉnh {vertex} là {in_degree}")

if dt.DuongDi(1,2):
    print("Có đường đi từ đỉnh 1 đến 2")
else:
    print("Không có đường đi từ đỉnh 1 đến 2")

import time
import random



# 割
class Edge:
    def __init__(self, edge: list = None):
        if edge is None:
            self.edge = []
        else:
            self.edge = edge

    def add_edge(self, weight, begin, end):
        self.edge.append([weight,begin,end])

    def sort(self):
        self.edge.sort()

# 最小二叉堆

class Heap:
    def __init__(self, data:list = None):
        if data is None:
            self.heap = []
        else:
            self.heap = data

    def heap_print(self):
        for item in self.heap:
            print(item)

    def exact_min(self):
        min = self.heap[0]
        n = len(self.heap)
        self.swap(0, n-1)
        del self.heap[-1]
        self.heapify()

        return min

    def insert(self, data):
        self.heap.append(data)
        self.heapify()

    def heapify(self):
        n = len(self.heap)
        for idx in range(n-1, -1, -1):
            parent_idx = int((idx - 1)/ 2)
            if self.heap[idx][0] < self.heap[parent_idx][0]:
                self.swap(idx,parent_idx)

    def swap(self, idx0, idx1):
        temp = self.heap[idx0]
        self.heap[idx0] = self.heap[idx1]
        self.heap[idx1] = temp

class GraphWeight:
    def __init__(self, graph: dict = None):
        if graph is None:
            self.graph = {}
        else:
            self.graph = graph

        self.num = None

    #添加无向边
    def add_e_both(self, begin, end, weight):
        if begin in self.graph.keys():
            self.graph[begin].append([end,weight])
        else:
            self.graph[begin] = [[end,weight]]
        if end in self.graph.keys():
            self.graph[end].append([begin,weight])
        else:
            self.graph[end] = [[begin,weight]]

    #添加有向边
    def add_e_one(self, begin, end, weight):
        if begin in self.graph.keys():
            self.graph[begin].append([end,weight])
        else:
            self.graph[begin] = [[end,weight]]

    #打印邻接链表
    def print(self):
        for key in self.graph.keys():
            print(key,self.graph[key])

    def get_edge(self, searched):
        edges = []
        for searched_node in searched:
            for end in self.graph[searched_node]:
                if end[0] not in searched:
                    edges.append([end[1], searched_node, end[0]])
        return edges

def Prim(graph:GraphWeight, begin):
    #初始化
    visited = []
    heap = Heap()
    visited.append(begin)
    edges = graph.get_edge(visited)
    MST = GraphWeight()
    weight_all = 0
    for edge in edges:
        heap.insert(edge)
    #开始循环
    while len(visited) < len(graph.graph.keys()):
        min_edge = heap.exact_min()
        visited.append(min_edge[2])
        MST.add_e_both(min_edge[1],min_edge[2],min_edge[0])
        new_edges = graph.get_edge(visited)
        heap = Heap(new_edges)
        weight_all+= min_edge[0]
    return MST,weight_all


class UnionFind:
    def __init__(self):
        self.parent = {}
    def find(self, node):
        if node not in self.parent:
            self.parent[node] = node
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.parent[root2] = root1

def Kruskal(graph:GraphWeight):
    edges = Edge()
    weight_all = 0
    for begin in graph.graph.keys():
        for end in graph.graph[begin]:
            if begin < end[0]:
                edges.add_edge(end[1], begin, end[0])
    edges.sort()
    uf = UnionFind()
    MST = GraphWeight()
    for edge in edges.edge:
        weight = edge[0]
        begin = edge[1]
        end = edge[2]
        if uf.find(begin) != uf.find(end):
            uf.union(begin,end)
            MST.add_e_both(begin,end,weight)
            weight_all += weight
    return MST,weight_all




# my_graph = GraphWeight()
# my_graph.add_e_both(1,2,1)
# my_graph.add_e_both(2,4,3)
# my_graph.add_e_both(1,4,2)
# my_graph.add_e_both(1,3,4)
# my_graph.print()
#
# print("MST_Prim")
# Prim(my_graph,1).print()
#
# print("MST_Kruskal")
# Kruskal(my_graph).print()

# # 实验计时模块
# def generate_random_graph(n, density=0.5):
#     gw = GraphWeight()
#     for u in range(n):
#         for v in range(u + 1, n):
#             if random.random() < density:
#                 w = random.randint(1, 100)
#                 gw.add_e_both(u, v, w)
#     return gw
#
# def run_time_experiment():
#     sizes = [10, 20, 40, 80]
#     print("节点数\tPrim时间(s)\tKruskal时间(s)")
#     for n in sizes:
#         graph = generate_random_graph(n, density=0.4)
#
#         # Prim 计时
#         start = time.time()
#         prim_mst = Prim(graph, 0)  # 你原来的 Prim
#         prim_time = time.time() - start
#
#         # Kruskal 计时
#         start = time.time()
#         kruskal_mst = Kruskal(graph)  # 你原来的 Kruskal
#         kruskal_time = time.time() - start
#
#         print(f"{n}\t{prim_time:.6f}\t{kruskal_time:.6f}")
#
# # ================= 运行实验 =================
# if __name__ == "__main__":
#     run_time_experiment()
graph = GraphWeight()
n,m = input().split()
for i in range(0, int(m)):
    u,v,w = input().split()
    graph.add_e_both(int(u),int(v),int(w))
# graph.print()
# print("MST_Prim")
# MST,weight = Prim(graph,1)
# print(weight)
# MST.print()
# print("MST_Kruskal")
MST,weight = Kruskal(graph)
# MST.print()
print(weight)


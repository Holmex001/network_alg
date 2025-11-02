# 我要自己写图的结构
import queue

class Graph:
    # def __init__(self, graph: dict = None):
    #     if graph is None:
    #         self.graph = {}
    #     else:
    #         self.graph = graph
    #
    #     self.num = None
    def __init__(self, graph: dict = None):
        if graph is None:
            self.graph = {}          # 原邻接表：node -> [node, ...]
        else:
            self.graph = graph
        # 新增：边权记录  (u,v)->w
        self.weight = {}

    #添加无向边
    def add_e_both(self, begin, end):
        if begin in self.graph.keys():
            self.graph[begin].append(end)
        else:
            self.graph[begin] = [end]
        if end in self.graph.keys():
            self.graph[end].append(begin)
        else:
            self.graph[end] = [begin]

    #添加有向边
    def add_e_one(self, begin, end):
        if begin in self.graph.keys():
            self.graph[begin].append(end)
        else:
            self.graph[begin] = [end]

    def del_e(self, begin, end):
        if begin in self.graph.keys():
            if end in self.graph[begin]:
                self.graph[begin].remove(end)
                if self.graph[begin] == []:
                    self.graph.pop(begin)
                return

        print("不存在这条边")

    #打印邻接链表
    def print(self):
        for key in self.graph.keys():
            print(key,self.graph[key])

    def DFS(self, begin, pre, post):
        pre.append(begin)
        if begin not in self.graph.keys():
            self.graph[begin] = []
        for value in self.graph[begin]:
            if value not in pre and value not in post:
                pre.append(value)
                self.DFS(value, pre, post)
        post.append(begin)

        return post

    def BFS(self, begin):
        Q = queue.Queue()
        Q.put(begin)
        post = []

        while Q.empty() == 0:
            v = Q.get()
            for value in self.graph[v]:
                if value not in post:
                    Q.put(value)
            post.append(v)
        return post

    #找到有多少个连通的图
    def find_unconnected_numb(self):
        post = []
        notes = self.graph.keys()
        counter = 0

        for value in notes:
            if value not in post:
                post = self.BFS(value)
                counter += 1

        return counter

    #把图的边反向 Two Pass 的第一步
    def get_rev_graph(self):
        rev_graph = {}

        for note in self.graph.keys():
            begin = self.graph[note]
            end = note
            for beg in begin:
                if beg not in rev_graph.keys():
                    rev_graph[beg] = []
                if end not in rev_graph[beg]:
                    rev_graph[beg].append(end)

        return rev_graph

    def DFS_SSC(self, begin, pre, post, temp:'Graph'):
        pre.append(begin)
        temp.graph[begin] = []
        for value in self.graph[begin]:
            if value not in post:
                temp.add_e_one(begin,value)
            if value not in pre and value not in post:
                pre.append(value)
                self.DFS_SSC(value, pre, post, temp)
        post.append(begin)

        return post

    #找强连通分量 Two Pass
    def get_SSC(self,begin):
        rev_graph = self.get_rev_graph()
        rev_graph = Graph(rev_graph)
        post = []
        pre = []
        key = list(rev_graph.graph.keys())[0]
        post = rev_graph.DFS(key,pre,post)
        post.reverse()

        searched = []

        ssc_s = []
        temp_pre = []
        temp_post = []

        for value in post:
            if value not in searched:
                temp = Graph()
                self.DFS_SSC(value, temp_pre, temp_post, temp)
                ssc_s.append(temp)
                for post_value in temp_post:
                    searched.append(post_value)

        return ssc_s

    # 拓扑排序
    def topological_sort(self, begin, pre, post):
        self.DFS(begin, pre, post)
        post.reverse()

        return post

# ========== 以下为新增：带权接口 ==========

    def add_weighted_edge(self, u, v, w: int):
        """有向带权边"""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph[u]:
            self.graph[u].append(v)
        self.weight[(u, v)] = w

    def to_weighted_list(self) -> list:
        """
        把当前图转成  list[ list[(v,w), ...] ]  形式
        节点编号 0..n-1  连续
        """
        nodes = sorted(self.graph.keys())
        idx = {v: i for i, v in enumerate(nodes)}
        n = len(nodes)
        adj = [[] for _ in range(n)]
        for u in self.graph:
            for v in self.graph[u]:
                w = self.weight.get((u, v), 1)   # 默认权重 1（兼容老代码）
                adj[idx[u]].append((idx[v], w))
        return adj, nodes          # 返回邻接表 + 原始节点顺序


my_graph = Graph()
my_graph.add_e_one(1,3)
my_graph.add_e_one(2,3)
my_graph.add_e_one(1,4)
my_graph.add_e_one(3,4)
my_graph.add_e_one(4,2)

my_graph.print()
pre = []
post = []
# print(my_graph.DFS(1, pre, post ))
# Q = queue.Queue()
# post = []
# print(my_graph.BFS(1))
# print(my_graph.find_unconnected_numb())
#
# rev_graph = my_graph.get_rev_graph()
# rev_graph = Graph(rev_graph)
# rev_graph.print()
# my_graph.print()
#
# ssc_s = my_graph.get_SSC(1)
# size = len(ssc_s)
# for i in range(0, size):
#     print("SSC:",i)
#     ssc_s[i].print()
#
# print(my_graph.topological_sort(1, pre, post))











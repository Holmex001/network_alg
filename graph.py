# 我要自己写图的结构
import queue


class Graph:
    def __init__(self, graph: dict = None):
        if graph is None:
            self.graph = {}
        else:
            self.graph = graph

        self.num = None

    def add_e(self, begin, end):
        if begin in self.graph.keys():
            self.graph[begin].append(end)
        else:
            self.graph[begin] = [end]

        if end in self.graph.keys():
            self.graph[end].append(begin)
        else:
            self.graph[end] = [begin]

    def del_e(self, begin, end):
        if begin in self.graph.keys():
            if end in self.graph[begin]:
                self.graph[begin].remove(end)
                if self.graph[begin] == []:
                    self.graph.pop(begin)
                return

        print("不存在这条边")


    def print(self):
        for key in self.graph.keys():
            print(key,self.graph[key])

    def DFS(self, begin, pre, post):
        pre.append(begin)
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

    def get_DFS_num(self, begin, pre, post, note_num:dict): # 有问题
        if self.num == None:
            self.num = 1

        pre.append(begin)
        if begin not in note_num.keys():
            note_num[begin] = [None,None]
        note_num[begin][0] = self.num
        self.num += 1

        for value in self.graph[begin]:
            if value not in pre and value not in post:
                pre.append(value)
                if value not in note_num.keys():
                    note_num[value] = [None,None]
                note_num[value][0] = self.num
                self.num += 1
                self.get_DFS_num(value, pre, post, note_num)
        post.append(begin)
        if begin not in note_num.keys():
            note_num[begin] = [None,None]
        note_num[begin][1] = self.num
        self.num += 1

        return  note_num




    def find_unconnected_numb(self):
        post = []
        notes = self.graph.keys()
        counter = 0

        for value in notes:
            if value not in post:
                post = self.BFS(value)
                counter += 1

        return counter

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









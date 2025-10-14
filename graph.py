# 我要自己写图的结构

class Graph:
    def __init__(self):
        self.graph = {}

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

    def DFS(self, begin, extended, searched):
        extended.append(begin)
        for value in self.graph[begin]:
            if value not in extended or value not in searched:
                extended.append(value)
                self.DFS(value, extended, searched)
            searched.append(value)

        return searched

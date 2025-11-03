import copy

from graph import Graph

class SimpleGraph:
    def __init__(self, simple_graph: dict = None):
        if simple_graph is None:
            self.simple_graph = {}
        else:
            self.simple_graph = simple_graph

    def add_simple_edge(self, a, b):
        if a in self.simple_graph.keys():
            self.simple_graph[a].append(b)
        else:
            self.simple_graph[a] = [b]

        if b in self.simple_graph.keys():
            self.simple_graph[b].append(a)
        else:
            self.simple_graph[b] = [a]

    def is_circle_DFS(self, begin, pre, post, flag:0):
        pre.append(begin)
        for value in self.simple_graph[begin]:
            if value not in pre and value not in post:
                pre.append(value)
                self.is_circle_DFS(value, pre, post, flag)
            else:
                flag = 1
        post.append(begin)

        return flag



def Kruskal(my_graph: Graph):
    x = Graph()
    edges = my_graph.weight
    edges = sorted(edges.items(), key= lambda item: item[1])
    print(edges)

    for edge in edges:
        # print(edge[0][0])
        x_graph = copy.deepcopy(x.graph)
        pre_x = SimpleGraph(x_graph)
        pre_x.add_simple_edge(edge[0][0], edge[0][1])
        if pre_x.is_circle_DFS(edge[0][0],[],[], 0) == 0:
            x.add_no_direct_weighted_edge(edge[0][0], edge[0][1], edge[1])
    x.print_weighted_graph()

graph = Graph()
graph.add_no_direct_weighted_edge(1,2,1)
graph.add_no_direct_weighted_edge(1,3,2)
graph.add_no_direct_weighted_edge(2,3,3)
graph.add_no_direct_weighted_edge(2,4,1)
Kruskal(graph)
graph.print_weighted_graph()

# graph = SimpleGraph()
# graph.add_simple_edge(1,2)
# graph.add_simple_edge(2,3)
# graph.add_simple_edge(1,3)
# graph.add_simple_edge(1,4)
# print(graph.is_circle_DFS(1,[],[],0))



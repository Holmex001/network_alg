import fibonacci as fib
import graph as graph

if __name__ == '__main__':
    # print(fib.fib_3(5))
    my_graph = graph.Graph()
    my_graph.add_e(1,3)
    my_graph.add_e(2,3)
    my_graph.add_e(1,4)
    my_graph.print()
    searched = []
    print(my_graph.DFS(1, searched))



import queue

import fibonacci as fib
import graph as graph

if __name__ == '__main__':
    # print(fib.fib_3(5))
    my_graph = graph.Graph()
    my_graph.add_e(1,3)
    my_graph.add_e(2,3)
    my_graph.add_e(1,4)

    my_graph.print()
    pre = []
    post = []
    print(my_graph.DFS(1, pre, post ))
    Q = queue.Queue()
    post = []
    print(my_graph.BFS(1))
    print(my_graph.find_unconnected_numb())

    rev_graph = my_graph.get_rev_graph()
    rev_graph = graph.Graph(rev_graph)
    rev_graph.print()

    ssc_s = my_graph.get_SSC(1)
    print(ssc_s[0].print())


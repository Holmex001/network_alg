import heapq
from graph import Graph
from typing import List, Tuple

INF = 10 ** 18

def dijkstra_heap(g: Graph, src):
    adj, nodes = g.to_weighted_list()   # 0..n-1 连续编号
    n = len(adj)
    src_idx = nodes.index(src)
    dist = [INF] * n
    dist[src_idx] = 0
    heap = [(0, src_idx)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    # 把编号映射回原始节点名
    return {nodes[i]: dist[i] for i in range(n) if dist[i] < INF}

# ------------------简单测试------------------
if __name__ == "__main__":
    g = Graph()
    g.add_weighted_edge(1, 3, 4)
    g.add_weighted_edge(1, 4, 1)
    g.add_weighted_edge(2, 3, 2)
    g.add_weighted_edge(3, 4, 2)
    g.add_weighted_edge(4, 2, 3)
    print("heap:", dijkstra_heap(g, 1))
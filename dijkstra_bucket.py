from collections import deque
from graph import Graph
from typing import List

INF = 10 ** 18

def dijkstra_bucket(g: Graph, src):
    adj, nodes = g.to_weighted_list()
    n = len(adj)
    max_w = max(w for u in range(n) for _, w in adj[u]) if n else 0
    C = max_w
    bucket_size = n * C + 1
    buckets = [deque() for _ in range(bucket_size)]
    src_idx = nodes.index(src)
    dist = [INF] * n
    dist[src_idx] = 0
    buckets[0].append(src_idx)
    current = 0
    while current < bucket_size:
        while current < bucket_size and not buckets[current]:
            current += 1
        if current == bucket_size:
            break
        u = buckets[current].popleft()
        if dist[u] < current:
            continue
        for v, w in adj[u]:
            nd = dist[u] + w
            if nd < dist[v]:
                dist[v] = nd
                buckets[nd].append(v)
    return {nodes[i]: dist[i] for i in range(n) if dist[i] < INF}

# ------------------简单测试------------------
if __name__ == "__main__":
    g = Graph()
    g.add_weighted_edge(1, 3, 4)
    g.add_weighted_edge(1, 4, 1)
    g.add_weighted_edge(2, 3, 2)
    g.add_weighted_edge(3, 4, 2)
    g.add_weighted_edge(4, 2, 3)
    print("bucket:", dijkstra_bucket(g, 1))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dijkstra 性能对照实验 + 即时画图
python experiment.py
"""
import time
import random
import csv
from graph import Graph
from dijkstra_heap import dijkstra_heap
from dijkstra_bucket import dijkstra_bucket

# -------------------------------------------------
# 可调的实验参数
PARAM = {
    'num_group': 20,      # 每组 (n,density) 重复多少次
    'node_list': [100, 500, 1000, 2000],
    'density': [0.2, 0.5, 0.8],
    'max_w': 50,          # 边权上限
    'seed': 42
}
random.seed(PARAM['seed'])
# -------------------------------------------------

def random_instance(n: int, p: float, max_w: int) -> Graph:
    """生成无向带权图"""
    g = Graph()
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            if random.random() < p:
                w = random.randint(1, max_w)
                g.add_weighted_edge(u, v, w)
                g.add_weighted_edge(v, u, w)
    return g

def bench_one(g: Graph, src=1):
    """返回 (heap耗时/ms, bucket耗时/ms)"""
    t0 = time.perf_counter()
    dijkstra_heap(g, src)
    t_heap = (time.perf_counter() - t0) * 1000

    t0 = time.perf_counter()
    dijkstra_bucket(g, src)
    t_bucket = (time.perf_counter() - t0) * 1000

    return t_heap, t_bucket

# -------------------------------------------------
# 1. 实验主体：跑数据 + 写 CSV
def run_experiment():
    header = ['group', 'n', 'm', 'density', 't_heap_ms', 't_bucket_ms', 'speedup']
    rows = []
    gid = 0
    for n in PARAM['node_list']:
        for dens in PARAM['density']:
            for _ in range(PARAM['num_group']):
                g = random_instance(n, dens, PARAM['max_w'])
                m = sum(len(g.graph[u]) for u in g.graph) // 2
                th, tb = bench_one(g)
                speedup = th / tb if tb else 0
                rows.append([gid, n, m, f"{dens:.1f}", f"{th:.2f}", f"{tb:.2f}", f"{speedup:.2f}"])
                gid += 1
                print(f"group{gid:03d}  n={n:4d}  m={m:5d}  "
                      f"heap={th:7.2f}ms  bucket={tb:7.2f}ms  speedup={speedup:.2f}")

    with open("result.csv", "w", newline='') as f:
        csv.writer(f).writerows([header] + rows)
    print("\n实验完成，结果已写入 result.csv")
    return rows      # 返回原始数据供画图

# -------------------------------------------------
# 2. 零依赖可视化：终端直方图 + 加速比表格
def plot_on_the_fly():
    import csv
    from collections import defaultdict

    # 读数据
    with open('result.csv') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    # 转数值
    for r in data:
        r['n'] = int(r['n'])
        r['t_heap_ms'] = float(r['t_heap_ms'])
        r['t_bucket_ms'] = float(r['t_bucket_ms'])
        r['density'] = float(r['density'])

    # 按 (n, density) 求平均
    avg = defaultdict(lambda: {'heap': 0.0, 'bucket': 0.0, 'cnt': 0})
    for r in data:
        key = (r['n'], r['density'])
        avg[key]['heap'] += r['t_heap_ms']
        avg[key]['bucket'] += r['t_bucket_ms']
        avg[key]['cnt'] += 1
    for key in avg:
        avg[key]['heap'] /= avg[key]['cnt']
        avg[key]['bucket'] /= avg[key]['cnt']

    # ---------- 终端直方图 ----------
    def _bar(label, val, width=50):
        """简单文本条"""
        block = int(val / max_val * width)
        return f"{label:12s} |{'█' * block}{' ' * (width - block)}| {val:6.2f} ms"

    print("\n========== 平均耗时对比 ==========")
    for (n, dens), v in sorted(avg.items()):
        max_val = max(v['heap'], v['bucket']) or 1
        print(f"n={n:4d}  density={dens:.1f}")
        print(_bar("heap", v['heap']))
        print(_bar("bucket", v['bucket']))
        print("")

    # ---------- 加速比表格 ----------
    print("========== 加速比 (heap/bucket) ==========")
    dens_vals = sorted({d for _, d in avg.keys()})
    n_vals = sorted({n for n, _ in avg.keys()})
    header = ["n\\dens"] + [f"{d:.1f}" for d in dens_vals]
    print("".join(f"{h:>10s}" for h in header))
    for n in n_vals:
        row = [f"{n:4d}"] + [f"{avg[(n, d)]['heap']/avg[(n, d)]['bucket']:7.2f}"
                             for d in dens_vals]
        print("".join(f"{r:>10s}" for r in row))


# -------------------------------------------------
# 3. 主入口
if __name__ == "__main__":
    # data = run_experiment()
    plot_on_the_fly()
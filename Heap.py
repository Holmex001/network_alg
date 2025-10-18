# 最小二叉堆

class Heap:
    def __init__(self, data:list = None):
        if data is None:
            self.heap = []
        else:
            self.heap = data

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
            if self.heap[idx] < self.heap[parent_idx]:
                self.swap(idx,parent_idx)

    def swap(self, idx0, idx1):
        temp = self.heap[idx0]
        self.heap[idx0] = self.heap[idx1]
        self.heap[idx1] = temp

my_heap = Heap([1,2,3,4,5,6])
my_heap.heapify()
print(my_heap.heap)
my_heap.exact_min()
print(my_heap.heap)
my_heap.insert(1)
print(my_heap.heap)
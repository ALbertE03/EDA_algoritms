class Heap:
    def __init__(self):
        self.h = []
        self.heap_size = 0

    def __repr__(self):
        return f"Heap: {self.h}, Size: {self.heap_size}"

    def parent_index(self, child_idx):
        if child_idx > 0:
            return (child_idx - 1) // 2
        return None

    def left_child_idx(self, parent_idx):
        left_child_index = 2 * parent_idx + 1
        if left_child_index < self.heap_size:
            return left_child_index
        return None

    def right_child_idx(self, parent_idx):
        right_child_index = 2 * parent_idx + 2
        if right_child_index < self.heap_size:
            return right_child_index
        return None

    def max_heapify(self, index):
        left_child = self.left_child_idx(index)
        right_child = self.right_child_idx(index)
        largest = index

        if left_child is not None and self.h[left_child] > self.h[largest]:
            largest = left_child
        if right_child is not None and self.h[right_child] > self.h[largest]:
            largest = right_child

        if largest != index:
            self.h[largest], self.h[index] = self.h[index], self.h[largest]
            self.max_heapify(largest)

    def build_max_heap(self, collection):
        self.h = list(collection)
        self.heap_size = len(self.h)
        if self.heap_size > 1:
            for i in range(self.heap_size // 2 - 1, -1, -1):
                self.max_heapify(i)

    def extract_max(self):
        if self.heap_size == 0:
            raise Exception("Empty heap")
        max_value = self.h[0]
        self.h[0] = self.h[self.heap_size - 1]
        self.h.pop()
        self.heap_size -= 1
        if self.heap_size > 0:
            self.max_heapify(0)
        return max_value

    def insert(self, value):
        self.h.append(value)
        self.heap_size += 1
        idx = self.heap_size - 1
        while idx > 0:
            parent_idx = self.parent_index(idx)
            if self.h[parent_idx] >= self.h[idx]:
                break
            self.h[parent_idx], self.h[idx] = self.h[idx], self.h[parent_idx]
            idx = parent_idx

    def heap_sort(self):
        size = self.heap_size
        for j in range(size - 1, 0, -1):
            self.h[0], self.h[j] = self.h[j], self.h[0]
            self.heap_size -= 1
            self.max_heapify(0)
        self.heap_size = size


# Pruebas
for unsorted in [
    [0],
    [2],
    [3, 5],
    [5, 3],
    [5, 5],
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [2, 2, 3, 5],
    [0, 2, 2, 3, 5],
    [2, 5, 3, 0, 2, 3, 0, 3],
    [6, 1, 2, 7, 9, 3, 4, 5, 10, 8],
    [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5],
    [-45, -2, -5],
]:
    print(f"Array original: {unsorted}")

    heap = Heap()
    heap.build_max_heap(unsorted)
    print(f"Heap construido: {heap}")

    heap.heap_sort()
    print(f"Array ordenado: {heap.h}")
    print("-" * 50)

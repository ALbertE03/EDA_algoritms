class Node:
    def __init__(self, name, val):
        self.name = name
        self.val = val

    def __str__(self):
        return f"{self.__class__.__name__}({self.name}, {self.val})"

    def __lt__(self, other):
        return self.val < other.val


class MinHeap:
    def __init__(self, array):
        self.idx_of_element = {}
        self.heap_dict = {}
        self.heap = self.build_heap(array)

    def __getitem__(self, key):
        return self.get_value(key)

    def get_parent_idx(self, idx):
        return (idx - 1) // 2

    def get_left_child_idx(self, idx):
        return idx * 2 + 1

    def get_right_child_idx(self, idx):
        return idx * 2 + 2

    def get_value(self, key):
        return self.heap_dict[key]

    def build_heap(self, array):
        last_idx = len(array) - 1
        start_from = self.get_parent_idx(last_idx)

        for idx, node in enumerate(array):
            self.idx_of_element[node] = idx
            self.heap_dict[node.name] = node.val

        for i in range(start_from, -1, -1):
            self.sift_down(i, array)
        return array

    def sift_down(self, idx, array):
        while True:
            left = self.get_left_child_idx(idx)
            right = self.get_right_child_idx(idx)

            smallest = idx
            if left < len(array) and array[left] < array[smallest]:
                smallest = left
            if right < len(array) and array[right] < array[smallest]:
                smallest = right

            if smallest != idx:
                array[idx], array[smallest] = array[smallest], array[idx]
                (
                    self.idx_of_element[array[idx]],
                    self.idx_of_element[array[smallest]],
                ) = (
                    self.idx_of_element[array[smallest]],
                    self.idx_of_element[array[idx]],
                )
                idx = smallest
            else:
                break

    def sift_up(self, idx):
        p = self.get_parent_idx(idx)
        while p >= 0 and self.heap[p] > self.heap[idx]:
            self.heap[p], self.heap[idx] = self.heap[idx], self.heap[p]
            self.idx_of_element[self.heap[p]], self.idx_of_element[self.heap[idx]] = (
                self.idx_of_element[self.heap[idx]],
                self.idx_of_element[self.heap[p]],
            )
            idx = p
            p = self.get_parent_idx(idx)

    def peek(self):
        if self.is_empty():
            raise Exception("Heap is empty")
        return self.heap[0]

    def remove(self):
        if self.is_empty():
            raise Exception("Heap is empty")
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.idx_of_element[self.heap[0]], self.idx_of_element[self.heap[-1]] = (
            self.idx_of_element[self.heap[-1]],
            self.idx_of_element[self.heap[0]],
        )

        x = self.heap.pop()
        del self.idx_of_element[x]
        del self.heap_dict[x.name]
        if self.heap:
            self.sift_down(0, self.heap)
        return x

    def insert(self, node):
        self.heap.append(node)
        self.idx_of_element[node] = len(self.heap) - 1
        self.heap_dict[node.name] = node.val
        self.sift_up(len(self.heap) - 1)

    def is_empty(self):
        return len(self.heap) == 0

    def decrease_key(self, node, new_value):
        if node not in self.idx_of_element:
            raise Exception("Node not found in heap")
        if self.heap[self.idx_of_element[node]].val <= new_value:
            raise Exception("New value must be less than current value")
        node.val = new_value
        self.heap_dict[node.name] = new_value
        self.sift_up(self.idx_of_element[node])


r = Node("R", -1)
b = Node("B", 6)
a = Node("A", 3)
x = Node("X", 1)
e = Node("E", 4)

my_min_heap = MinHeap([r, b, a, x, e])

print("Heap inicial:")
for i in my_min_heap.heap:
    print(i)

print("\nValor mínimo (peek):", my_min_heap.peek())

print("\nEliminando el mínimo...")
removed_node = my_min_heap.remove()
print("Nodo eliminado:", removed_node)

print("\nHeap después de eliminar el mínimo:")
for i in my_min_heap.heap:
    print(i)

print("\nInsertando un nuevo nodo (Z, 0)...")
z = Node("Z", 0)
my_min_heap.insert(z)

print("\nHeap después de insertar Z:")
for i in my_min_heap.heap:
    print(i)

print("\nDecrementando la clave de B a 2...")
my_min_heap.decrease_key(b, 2)

print("\nHeap después de decrementar la clave de B:")
for i in my_min_heap.heap:
    print(i)

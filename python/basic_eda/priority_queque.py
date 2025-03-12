class Node:
    def __init__(self, info, priority) -> None:
        self.info = info
        self.priority = priority

    def __repr__(self):
        return f"({self.info}, {self.priority})"


class PriorityQueue:
    def __init__(self) -> None:
        self.elements = []

    def is_empty(self) -> bool:
        return not self.elements

    def put(self, info, priority) -> None:
        new_node = Node(info, priority)
        self.elements.append(new_node)
        self._sift_up(len(self.elements) - 1)

    def get(self):
        if self.is_empty():
            raise IndexError("No hay elementos en la cola de prioridad")
        # Intercambiamos el primer y último elemento
        self.elements[0], self.elements[-1] = self.elements[-1], self.elements[0]
        removed_node = self.elements.pop()  # Eliminamos el último elemento
        if self.elements:
            self._sift_down(0)  # Reorganizamos el heap
        return removed_node.info

    def _sift_up(self, idx):
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.elements[idx].priority >= self.elements[parent_idx].priority:
                break
            # Intercambiamos el nodo actual con su padre
            self.elements[idx], self.elements[parent_idx] = (
                self.elements[parent_idx],
                self.elements[idx],
            )
            idx = parent_idx

    def _sift_down(self, idx):
        while True:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            smallest = idx

            if (
                left_child_idx < len(self.elements)
                and self.elements[left_child_idx].priority
                < self.elements[smallest].priority
            ):
                smallest = left_child_idx

            if (
                right_child_idx < len(self.elements)
                and self.elements[right_child_idx].priority
                < self.elements[smallest].priority
            ):
                smallest = right_child_idx

            if smallest == idx:
                break

            # Intercambiamos el nodo actual con el hijo más pequeño
            self.elements[idx], self.elements[smallest] = (
                self.elements[smallest],
                self.elements[idx],
            )
            idx = smallest

    def size(self) -> int:
        return len(self.elements)

    def __repr__(self) -> str:
        return f"PriorityQueue({self.elements})"


# Pruebas
pq = PriorityQueue()
pq.put("Tarea 1", 3)
pq.put("Tarea 2", 1)
pq.put("Tarea 3", 2)

print("Cola de prioridad después de añadir elementos:", pq)
print("Tamaño de la cola de prioridad:", pq.size())

print("Elemento eliminado:", pq.get())
print("Cola de prioridad después de eliminar un elemento:", pq)
print("Tamaño de la cola de prioridad:", pq.size())

print("Elemento eliminado:", pq.get())
print("Cola de prioridad después de eliminar otro elemento:", pq)
print("Tamaño de la cola de prioridad:", pq.size())

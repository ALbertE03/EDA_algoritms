class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.back = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def appendleft(self, data):
        new_node = Node(data)
        if not self.head:

            self.head = new_node
            self.tail = new_node
        else:

            new_node.next = self.head
            self.head.back = new_node
            self.head = new_node
        self.size += 1

    def pop(self):
        if not self.tail:
            raise IndexError("No hay elementos en el deque")
        data = self.tail.data
        self.tail = self.tail.back
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return data

    def popleft(self):

        if not self.head:
            raise IndexError("No hay elementos en el deque")
        data = self.head.data

        self.head = self.head.next
        if self.head:
            self.head.back = None
        else:
            self.tail = None
        self.size -= 1
        return data

    def __str__(self):
        elementos = []
        actual = self.head
        while actual:
            elementos.append(str(actual.data))
            actual = actual.next
        return "[" + ", ".join(elementos) + "]"

    def size(self):
        return self.size


d = Deque()
d.append(1)
d.append(2)
d.appendleft(0)
d.append(22)
d.appendleft(12)
print("Deque después de añadir elementos:", d)
print("Tamaño del deque:", d.size())

print("Elemento eliminado por la izquierda:", d.popleft())
print("Deque después de eliminar por la izquierda:", d)
print("Tamaño del deque:", d.size())

print("Elemento eliminado por la derecha:", d.pop())
print("Deque después de eliminar por la derecha:", d)
print("Tamaño del deque:", d.size())

print("Elemento eliminado por la izquierda:", d.popleft())
print("Deque después de eliminar por la izquierda:", d)
print("Tamaño del deque:", d.size())

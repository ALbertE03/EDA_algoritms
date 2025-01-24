class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

    def __str__(self):
        return f"{self.valor}"


class Cola:
    def __init__(self):
        self.head = None
        self.size = 0

    def pop_left(self):
        head = self.head
        if not head:
            raise "No hay elementos"
        self.head = self.head.next
        self.size -= 1
        return head

    def __str__(self):
        a = "["
        actual = self.head
        while actual:
            a += str(actual.valor)
            if actual.next is not None:
                a += ","
            actual = actual.next
        a += "]"
        return a

    def add(self, valor):
        if not self.head:
            self.head = Nodo(valor)
            self.size += 1
            return

        actual = self.head
        while actual.next:
            actual = actual.next
        actual.next = Nodo(valor)
        self.size += 1

    def size():
        return self.size


c = Cola()

c.add(2)
c.add(4)
print(c)
print(c.pop_left())
print(c)

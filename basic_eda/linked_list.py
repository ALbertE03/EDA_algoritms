class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

    def __str__(self):
        return f"{self.valor}"


class Linked_List:
    def __init__(self):
        self.head = None
        self.size = 0

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

    def delete(self, valor):
        if not self.head:
            raise "no hay elementos para eliminar"

        if self.head.valor == valor:
            self.head = self.head.next
            self.head -= 1
            return

        actual = self.head
        while actual is not None:
            prev = actual
            actual = actual.next
            if actual is not None:
                if actual.valor == valor:
                    prev.next = actual.next
                    self.size -= 1
                    break
        else:
            raise "no hay na'"

    def buscar(self, valor):
        actual = self.head
        if not actual:
            return -1

        while actual:
            if actual.valor == valor:
                return actual
            actual = actual.next

        return -1


l = Linked_List()

l.add(2)
l.add(4)
l.add(29)
l.add(22)
l.add(22)
print(l)
print(l.size)
l.delete(4)
print(l)
print(l.size)
print(l.buscar(22))
l.delete(22)
l.delete(22)
print(l.size)
print(l.buscar(22))

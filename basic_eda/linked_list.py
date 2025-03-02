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
        self.size += 1
        nuevo_nodo = Nodo(valor)
        if not self.head:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo_nodo

    def __str__(self):
        elementos = []
        actual = self.head
        while actual:
            elementos.append(str(actual.valor))
            actual = actual.next
        return "[" + ", ".join(elementos) + "]"

    def delete(self, valor):
        if not self.head:
            raise ValueError("No hay elementos para eliminar")

        if self.head.valor == valor:
            self.head = self.head.next
            self.size -= 1
            return

        actual = self.head
        while actual.next:
            if actual.next.valor == valor:
                actual.next = actual.next.next
                self.size -= 1
                return
            actual = actual.next

        raise ValueError("El valor no se encuentra en la lista")

    def buscar(self, valor):
        actual = self.head
        while actual:
            if actual.valor == valor:
                return actual
            actual = actual.next
        return None

    def size(self):
        return self.size


l = Linked_List()

l.add(2)
l.add(4)
l.add(29)
l.add(22)
l.add(22)
print("Lista después de añadir elementos:", l)
print("Tamaño de la lista:", l.size())

l.delete(4)
print("Lista después de eliminar 4:", l)
print("Tamaño de la lista:", l.size())

nodo = l.buscar(22)
if nodo:
    print(f"Se encontró el nodo con valor {nodo.valor}")
else:
    print("Nodo no encontrado")

l.delete(22)
l.delete(22)
print("Lista después de eliminar 22 dos veces:", l)
print("Tamaño de la lista:", l.size())

nodo = l.buscar(22)
if nodo:
    print(f"Se encontró el nodo con valor {nodo.valor}")
else:
    print("Nodo no encontrado")

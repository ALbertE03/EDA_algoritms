class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.back = None

    def __str__(self):
        return f"{self.valor}"


class Pila:
    def __init__(self):
        self.tail = None
        self.size = 0

    def add(self, valor):
        new_nodo = Nodo(valor)
        if not self.tail:

            self.tail = new_nodo
        else:

            new_nodo.back = self.tail
            self.tail = new_nodo
        self.size += 1

    def pop(self):
        if not self.tail:
            raise IndexError("No hay elementos en la pila")
        aux = self.tail
        self.tail = self.tail.back
        self.size -= 1
        return aux

    def __str__(self):
        elementos = []
        actual = self.tail
        while actual:
            elementos.append(str(actual.valor))
            actual = actual.back
        return "[" + ", ".join(elementos) + "]"

    def size(self):
        return self.size


p = Pila()
p.add(2)
p.add(312)
p.add(-2)
p.add(123)
print("Pila después de añadir elementos:", p)
print("Tamaño de la pila:", p.size())

print("Elemento eliminado:", p.pop())
print("Pila después de eliminar un elemento:", p)
print("Tamaño de la pila:", p.size())

print("Elemento eliminado:", p.pop())
print("Pila después de eliminar otro elemento:", p)
print("Tamaño de la pila:", p.size())

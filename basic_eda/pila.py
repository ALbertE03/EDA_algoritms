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
        if not self.tail:
            self.tail = Nodo(valor)
            self.size += 1
            return
        new_nodo = Nodo(valor)
        aux = self.tail
        self.tail = new_nodo
        self.tail.back = aux
        self.size += 1

    def pop(self):
        if not self.tail:
            raise "no hay elementos"

        aux = self.tail
        self.tail = self.tail.back
        self.size -= 1
        return aux

    def __str__(self):
        a = "["
        actual = self.tail
        while actual:
            a += str(actual.valor)
            if actual.back is not None:
                a += ","
            actual = actual.back
        a += "]"
        return a


p = Pila()
p.add(2)
p.add(312)
p.add(-2)
p.add(123)
print(p)
print(p.pop())
print(p)

from collections import deque


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def max_level_sum(self):

        if self.raiz is None:
            return -1, 0

        max_sum = float("-inf")
        max_level = -1
        level = 0
        queue = deque([self.raiz])

        while queue:
            level_sum = 0
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.valor
                if node.izquierda:
                    queue.append(node.izquierda)
                if node.derecha:
                    queue.append(node.derecha)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

            level += 1

        return max_level, max_sum

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True  # o el nodo
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        return self._buscar_recursivo(nodo.derecha, valor)

    def altura(self):
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, nodo):
        if nodo is None:
            return 0
        altura_izquierda = self._altura_recursiva(nodo.izquierda)
        altura_derecha = self._altura_recursiva(nodo.derecha)
        return max(altura_izquierda, altura_derecha) + 1


arbol1 = ArbolBinario()
arbol1.insertar(5)
arbol1.insertar(3)
arbol1.insertar(7)
arbol1.insertar(1)
arbol1.insertar(9)
arbol1.insertar(2)
arbol1.insertar(10)
print("Altura del árbol:", arbol1.altura())

# print(arbol1.buscar(9))
print(arbol1.max_level_sum())

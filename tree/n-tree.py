from collections import deque


class Arbol:
    def __init__(self, elemento):
        self.elemento = elemento
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(Arbol(hijo))

    def dfs_search(self, value):
        if self.elemento == value:
            return self
        for child in self.hijos:
            result = child.dfs_search(value)
            if result:
                return result
        return None

    def bfs_search(self, value):
        """Búsqueda en anchura (BFS)."""
        queue = deque([self])
        while queue:
            current = queue.popleft()
            if current.elemento == value:
                return current
            for child in current.hijos:
                queue.append(child)
        return None

    def max_level_sum(self):
        if not self:
            return -1, 0

        max_sum = float("-inf")
        max_level = -1
        level = 1
        queue = deque([self])

        while queue:
            level_sum = 0
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.elemento
                for child in node.hijos:
                    queue.append(child)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

            level += 1

        return max_level, max_sum

    def buscar_subarbol(self, elemento):
        if self.elemento == elemento:
            return self
        for hijo in self.hijos:
            resultado = hijo.buscar_subarbol(elemento)
            if resultado:
                return resultado
        return None

    def profundidad(self):
        if not self.hijos:
            return 1
        return 1 + max((hijo.profundidad() for hijo in self.hijos), default=0)

    def grado(self):
        return max(
            len(self.hijos), max((hijo.grado() for hijo in self.hijos), default=0)
        )

    def preorden(self):
        print(self.elemento, end=" ")
        for hijo in self.hijos:
            hijo.preorden()

    def inorden(self):
        if self.hijos:
            self.hijos[0].inorden()
        print(self.elemento, end=" ")
        for hijo in self.hijos[1:]:
            hijo.inorden()

    def postorden(self):
        for hijo in self.hijos:
            hijo.postorden()
        print(self.elemento, end=" ")

    def __str__(self):
        return self._str_aux(0)

    def _str_aux(self, nivel):
        resultado = "  " * nivel + str(self.elemento) + "\n"
        for hijo in self.hijos:
            resultado += hijo._str_aux(nivel + 1)
        return resultado


arbol = Arbol(1)
arbol.agregar_hijo(2)
arbol.agregar_hijo(5)
arbol.hijos[0].agregar_hijo(3)
arbol.hijos[0].agregar_hijo(4)
arbol.hijos[1].agregar_hijo(6)
arbol.hijos[1].agregar_hijo(7)

print("Profundidad del árbol:", arbol.profundidad())
print("Grado del árbol:", arbol.grado())
print("Nivel con la suma máxima y su suma:", arbol.max_level_sum())

print("\nRecorrido Preorden:")
arbol.preorden()

print("\n\nRecorrido Inorden:")
arbol.inorden()

print("\n\nRecorrido Postorden:")
arbol.postorden()

print("\n\nÁrbol:")
print(arbol)

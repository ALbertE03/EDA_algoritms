from collections import deque


class Arbol:
    def __init__(self, elemento):
        self.elemento = elemento
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(Arbol(hijo))

    def dfs_search(self, value):
        if self.elemento == value:
            return True
        for child in self.hijos:
            result = child.dfs_search(value)
            if result:
                return result
        return False

    def preorden(self):

        print(self.elemento)
        for hijo in self.hijos:
            hijo.preorden()

    def inorden(self):
        for hijo in self.hijos:
            hijo.inorden()
        print(self.elemento)

    def postorden(self):
        for hijo in self.hijos:
            hijo.postorden()

    def bfs_search(self, value):
        queue = deque([self])
        while queue:
            current = queue.popleft()
            if current.elemento == value:
                return True
            for child in current.hijos:
                queue.append(child)
        return False

    def max_level_sum(self):

        if self is None:
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
        return 1 + max(hijo.profundidad() for hijo in self.hijos)

    def grado(self):
        return max(
            len(self.hijos), max((hijo.grado() for hijo in self.hijos), default=0)
        )


arbol = Arbol(1)
arbol.agregar_hijo(2)
arbol.agregar_hijo(5)
arbol.hijos[0].agregar_hijo(5)

print(arbol.profundidad())
print(arbol.grado())
print(arbol.max_level_sum())

print("\nRecorrido Preorden:")
arbol.preorden()

print("\nRecorrido Inorden:")
arbol.inorden()

print("\nRecorrido Postorden:")
arbol.postorden()

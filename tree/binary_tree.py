from collections import deque


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1


class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):

        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):

        if not nodo:
            return Nodo(valor)

        if valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor)
        else:
            nodo.derecha = self._insertar(nodo.derecha, valor)

        nodo.altura = 1 + max(
            self._get_altura(nodo.izquierda), self._get_altura(nodo.derecha)
        )
        return self._balancear(nodo)

    def _get_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def _get_balance(self, nodo):
        if not nodo:
            return 0
        return self._get_altura(nodo.izquierda) - self._get_altura(nodo.derecha)

    def _balancear(self, nodo):
        balance = self._get_balance(nodo)

        if balance > 1 and nodo.izquierda and valor < nodo.izquierda.valor:
            return self._rotar_derecha(nodo)

        if balance < -1 and nodo.derecha and valor > nodo.derecha.valor:
            return self._rotar_izquierda(nodo)

        if balance > 1 and nodo.izquierda and valor > nodo.izquierda.valor:
            nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)

        if balance < -1 and nodo.derecha and valor < nodo.derecha.valor:
            nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)

        return nodo

    def _rotar_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha

        x.derecha = y
        y.izquierda = T2

        y.altura = 1 + max(self._get_altura(y.izquierda), self._get_altura(y.derecha))
        x.altura = 1 + max(self._get_altura(x.izquierda), self._get_altura(x.derecha))

        return x

    def _rotar_izquierda(self, x):

        y = x.derecha
        T2 = y.izquierda

        y.izquierda = x
        x.derecha = T2

        x.altura = 1 + max(self._get_altura(x.izquierda), self._get_altura(x.derecha))
        y.altura = 1 + max(self._get_altura(y.izquierda), self._get_altura(y.derecha))

        return y

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if not nodo:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar(nodo.izquierda, valor)
        else:
            return self._buscar(nodo.derecha, valor)

    def altura(self):

        return self._altura(self.raiz)

    def _altura(self, nodo):

        if not nodo:
            return 0
        altura_izquierda = self._altura(nodo.izquierda)
        altura_derecha = self._altura(nodo.derecha)
        return max(altura_izquierda, altura_derecha) + 1

    def max_level_sum(self):

        if not self.raiz:
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

    def __str__(self):
        levels = []
        queue = deque([(self.raiz, 0)])
        while queue:
            current_node, level = queue.popleft()

            if current_node is None:
                continue

            while len(levels) <= level:
                levels.append([])

            levels[level].append(current_node.valor)

            queue.append((current_node.izquierda, level + 1))
            queue.append((current_node.derecha, level + 1))

        result_str = ""
        for i in range(len(levels)):
            result_str += "Nivel {}: {}\n".format(
                i, " ".join(str(x) for x in levels[i])
            )

        return result_str.strip()

    def inorden(self):
        result = []
        self._inorden(self.raiz, result)
        return " ".join(map(str, result))

    def _inorden(self, nodo, result):
        if not nodo:
            return
        self._inorden(nodo.izquierda, result)
        result.append(nodo.valor)
        self._inorden(nodo.derecha, result)

    def preorden(self):
        result = []
        self._preorden(self.raiz, result)
        return " ".join(map(str, result))

    def _preorden(self, nodo, result):
        if not nodo:
            return
        result.append(nodo.valor)
        self._preorden(nodo.izquierda, result)
        self._preorden(nodo.derecha, result)

    def postorden(self):

        result = []
        self._postorden(self.raiz, result)
        return " ".join(map(str, result))

    def _postorden(self, nodo, result):

        if not nodo:
            return
        self._postorden(nodo.izquierda, result)
        self._postorden(nodo.derecha, result)
        result.append(nodo.valor)


arbol_avl = ArbolAVL()
valores_a_insertar = [10, 20, 30, 40, 50, 25]

for valor in valores_a_insertar:
    arbol_avl.insertar(valor)

print("Altura del árbol:", arbol_avl.altura())
print("Suma máxima por nivel:", arbol_avl.max_level_sum())

print(arbol_avl)
print(arbol_avl.inorden())

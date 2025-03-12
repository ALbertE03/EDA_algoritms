from collections import deque


class grafo:
    def __init__(self):
        self.grafo = {}
        self.time = 0
        self.aristas_puentes = []
        self.puntos_articulacion = []

    def agregar_arista(self, u, v):
        if u not in self.grafo:
            self.grafo[u] = []
        if v not in self.grafo:
            self.grafo[v] = []
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def dfs(self):
        """
        La complejidad temporal de DFS es:

        Θ(V + E) con G representado en una Lista de Adyacencia.
        Θ(|V|^2) con G representado en una Matriz de Adyacencia.

        """

        def dfs_visit(graph, u, visited, predecessors, CC, i):
            visited.add(u)
            self.time += 1
            d[u] = low[u] = self.time
            for v in graph[u]:
                if v not in visited:
                    predecessors[v] = u
                    dfs_visit(graph, v, visited, predecessors, CC, i)
                    low[u] = min(low[u], low[v])
                    if (
                        low[v] >= d[u]
                    ):  # si lo mas alto que se puede llegar en los descendietes de v es a u  => u es un punto de articulación
                        print(f"{u} es un punto de articulación")
                        self.puntos_articulacion.append(u)
                elif predecessors[u] != v:
                    low[u] = min(low[u], d[v])
            if predecessors[u] is not None and low[u] == d[u]:
                print(f"<{predecessors[u]}, {u}> es una arista puente")
                self.aristas_puentes.append((predecessors[u], u))
            CC[u] = i
            return

        visited = set()
        predecessors = {}
        CC = {}
        i = 1
        d = {}
        low = {}
        for u in self.grafo:
            if u not in visited:
                predecessors[u] = None
                dfs_visit(self.grafo, u, visited, predecessors, CC, i)
                i += 1

        return (
            predecessors,
            CC,
        )  # arbol de recubrimiento de dfs y componente conexa a la que pertenece cada nodo

    def bfs(
        self, inicio
    ):  # es para saber la distancia minima entre todos los nodos en una misma componente conexa
        # complejidad  O(V+E)
        cola = deque([inicio])
        distacia = {nodo: float("inf") for nodo in self.grafo}
        distacia[inicio] = 0
        arbol_de_recu = {node: None for node in self.grafo}
        while cola:
            nodo = cola.popleft()
            for vecino in self.grafo[nodo]:
                if distacia[vecino] == float("inf"):
                    distacia[vecino] = distacia[nodo] + 1
                    arbol_de_recu[vecino] = nodo
                    cola.append(vecino)
        return (
            distacia,
            arbol_de_recu,
        )  # Se añade un array arbol_de_recu que representará un árbol de cubrimiento o abarcador (generado por el BFS) con raíz en inicio utilizando la técnica de referencia al padre. En él, estarán todos los vértices alcanzables desde inicio


grafo = grafo()
grafo.agregar_arista(0, 1)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(1, 3)
grafo.agregar_arista(3, 4)
grafo.agregar_arista(2, 4)
grafo.agregar_arista(3, 5)


print(grafo.dfs())

from collections import deque


def orden_topologico(grafo):
    grado_entrada = {nodo: 0 for nodo in grafo}
    for nodo in grafo:
        for vecino in grafo[nodo]:
            grado_entrada[vecino] += 1

    cola = deque([nodo for nodo in grafo if grado_entrada[nodo] == 0])
    orden = []

    while cola:
        nodo = cola.popleft()
        orden.append(nodo)

        for vecino in grafo[nodo]:
            grado_entrada[vecino] -= 1
            if grado_entrada[vecino] == 0:
                cola.append(vecino)

    return orden


def camino_mas_corto_dag(grafo, inicio):
    # complejidad V+E
    orden = orden_topologico(grafo)

    distancias = {nodo: float("inf") for nodo in grafo}
    distancias[inicio] = 0

    for nodo in orden:
        if distancias[nodo] != float("inf"):
            for vecino, peso in grafo[nodo].items():
                if distancias[nodo] + peso < distancias[vecino]:  # relax
                    distancias[vecino] = distancias[nodo] + peso

    return distancias


grafo = {"A": {"B": 1, "C": 4}, "B": {"C": 2, "D": 5}, "C": {"D": 1}, "D": {}}

inicio = "A"
distancias = camino_mas_corto_dag(grafo, inicio)
print(f"Distancias desde el nodo {inicio}: {distancias}")

import heapq


def dijkstra(grafo, inicio):
    # complejidad |E|log|V|
    distancias = {nodo: float("inf") for nodo in grafo}

    distancias[inicio] = 0

    cola = [(0, inicio)]

    while cola:

        distancia_actual, nodo_actual = heapq.heappop(cola)

        if distancia_actual > distancias[nodo_actual]:
            continue

        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso  # relax

            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola, (distancia, vecino))

    return distancias


grafo = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1},
}

inicio = "A"
distancias = dijkstra(grafo, inicio)
print(f"Distancias desde el nodo {inicio}: {distancias}")

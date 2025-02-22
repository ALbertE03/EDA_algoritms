def bellman_ford(grafo, inicio):

    distancias = {nodo: float("inf") for nodo in grafo}
    distancias[inicio] = 0

    n = len(grafo)

    for _ in range(n - 1):  # relax
        for nodo in grafo:
            for vecino, peso in grafo[nodo].items():
                if distancias[nodo] + peso < distancias[vecino]:
                    distancias[vecino] = distancias[nodo] + peso

    # Verificar si hay ciclos negativos
    for nodo in grafo:
        for vecino, peso in grafo[nodo].items():  # relax
            if distancias[nodo] + peso < distancias[vecino]:
                raise ValueError("El grafo contiene un ciclo negativo")

    return distancias


grafo = {
    "A": {"B": -1, "C": 4},
    "B": {"C": 3, "D": 2, "E": 2},
    "C": {},
    "D": {"B": 1, "C": 5},
    "E": {"D": -3},
}

inicio = "A"
try:
    distancias = bellman_ford(grafo, inicio)
    print(f"Distancias desde el nodo {inicio}: {distancias}")
except ValueError as e:
    print(e)

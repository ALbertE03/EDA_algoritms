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

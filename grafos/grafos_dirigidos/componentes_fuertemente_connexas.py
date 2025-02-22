from collections import defaultdict


def kosaraju(grafo):
    # complejidad E+V
    def dfs(nodo, visitados, stack):
        visitados.add(nodo)
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                dfs(vecino, visitados, stack)
        stack.append(nodo)

    def transponer_grafo(grafo):
        grafo_transpuesto = defaultdict(list)
        for nodo in grafo:
            for vecino in grafo[nodo]:
                grafo_transpuesto[vecino].append(nodo)
        return grafo_transpuesto

    def dfs_transpuesto(nodo, visitados, componente):
        visitados.add(nodo)
        componente.append(nodo)
        for vecino in grafo_transpuesto[nodo]:
            if vecino not in visitados:
                dfs_transpuesto(vecino, visitados, componente)

    visitados = set()
    stack = []
    for nodo in grafo:
        if nodo not in visitados:
            dfs(nodo, visitados, stack)

    # Transponer el grafo
    grafo_transpuesto = transponer_grafo(grafo)

    visitados = set()
    componentes = []
    while stack:
        nodo = stack.pop()
        if nodo not in visitados:
            componente = []
            dfs_transpuesto(nodo, visitados, componente)
            componentes.append(componente)

    return componentes


grafo = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A", "D"],
    "D": ["E"],
    "E": ["F"],
    "F": ["D"],
    "G": ["F", "H"],
    "H": ["I"],
    "I": ["J"],
    "J": ["G", "K"],
    "K": [],
}

componentes = kosaraju(grafo)
print("Componentes fuertemente conexas:")
for i, componente in enumerate(componentes):
    print(f"Componente {i + 1}: {componente}")

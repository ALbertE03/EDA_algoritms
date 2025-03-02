class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return  # x e y ya están en el mismo conjunto

        # Unión por rango
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def __repr__(self):
        return f"Parent: {self.parent}\nRank: {self.rank}"


ds = DisjointSet(10)


ds.merge(0, 1)
ds.merge(2, 3)
ds.merge(4, 5)
ds.merge(6, 7)
ds.merge(8, 9)

# Verificamos conexiones
print("¿0 y 1 están conectados?", ds.is_connected(0, 1))  # True
print("¿2 y 4 están conectados?", ds.is_connected(2, 4))  # False

# Unimos más conjuntos
ds.merge(1, 9)
ds.merge(3, 5)

# Verificamos conexiones después de más uniones
print("¿0 y 9 están conectados?", ds.is_connected(0, 9))  # True
print("¿2 y 4 están conectados?", ds.is_connected(2, 4))  # True

# Representación del Disjoint Set
print("\nEstado final del Disjoint Set:")
print(ds)

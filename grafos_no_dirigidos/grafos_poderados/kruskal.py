class Graph:
    def __init__(self, n):
        self.vertices = n
        self.graph = []
        self.MST = None

    def add_edge(self, from_vertice, to, weight):
        self.graph.append([from_vertice, to, weight])

    def setOF(self, parent, i):
        if parent[i] == i:
            return i

        return self.setOF(parent, parent[i])

    def merge(self, parent, rank, a, b):
        a_root = self.setOF(parent, a)
        b_root = self.setOF(parent, b)

        if rank[a_root] < rank[b_root]:
            parent[a_root] = b_root
        elif rank[a_root] > rank[b_root]:
            parent[b_root] = a_root

        else:
            parent[b_root] = a_root
            rank[a_root] += 1

    def KruskalMTS(self):
        MST = []
        e = 0
        r = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        while r < self.vertices - 1:

            f = self.graph[e][0]
            to = self.graph[e][1]
            weight = self.graph[e][2]
            e += 1
            a = self.setOF(parent, f)
            b = self.setOF(parent, to)
            if a != b:
                r += 1
                MST.append([p, to, weight])
                self.merge(parent, rank, a, b)

        self.MST = MST

    def __str__(self):
        aux = ""
        for a, b, peso in self.MST:
            aux += str(a) + f"->{b}"
        return aux

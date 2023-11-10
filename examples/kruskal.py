"""Kruskal's algorithm is an efficient algorithm for constructing a minimum
spanning tree of a weighted connected undirected graph."""


from dsu_data_structure import DSU


# O(E * log(E) + E + E * V)
def kruskal(vertices, edges):
    edges = sorted(edges, key=lambda t: t[2]) # O(E * log(E))
    dsu = DSU(vertices)

    min_tree = []
    for edge in edges: # O(E)
        v, u, w = edge
        if not dsu.same(v, u): # O(1)
            dsu.union(v, u) # O(V)
            min_tree.append(edge)

    return min_tree


def main():
    # edge = (v, u, w=weight)

    vertices_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    edges_1 = [
        ('A', 'B', 7),
        ('A', 'D', 5),
        ('B', 'C', 8),
        ('B', 'D', 9),
        ('B', 'E', 7),
        ('C', 'E', 5),
        ('D', 'E', 15),
        ('D', 'F', 6),
        ('E', 'F', 8),
        ('E', 'G', 9),
        ('F', 'G', 11),
    ]
    print("# 1")
    print(kruskal(vertices_1, edges_1))

    vertices_2 = ['A', 'B', 'C', 'D', 'E']
    edges_2 = [
        ('A', 'E', 1),
        ('C', 'D', 2),
        ('A', 'B', 3),
        ('B', 'E', 4),
        ('B', 'C', 5),
        ('E', 'C', 6),
        ('E', 'D', 7),
    ]
    print("# 2")
    print(kruskal(vertices_2, edges_2))


if __name__ == "__main__":
    main()
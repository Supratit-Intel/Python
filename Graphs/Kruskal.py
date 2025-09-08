def kruskal(edges, num_vertices):
    # edges: list of (weight, u, v)
    parent = list(range(num_vertices))
    rank = [0] * num_vertices

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True

    mst = []
    edges = sorted(edges)
    for w, u, v in edges:
        if union(u, v):
            mst.append((u, v, w))
    return mst


if __name__ == '__main__':
    edges = [(1, 0, 1), (2, 1, 2), (3, 0, 2)]
    print(kruskal(edges, 3))
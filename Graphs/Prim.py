def prim(graph):
    # graph: adjacency dict mapping u -> {v: weight}
    import heapq
    start = next(iter(graph))
    visited = set([start])
    edges = []
    for v, w in graph[start].items():
        heapq.heappush(edges, (w, start, v))

    mst = []
    while edges and len(visited) < len(graph):
        w, u, v = heapq.heappop(edges)
        if v in visited:
            continue
        visited.add(v)
        mst.append((u, v, w))
        for to, wt in graph[v].items():
            if to not in visited:
                heapq.heappush(edges, (wt, v, to))
    return mst


if __name__ == '__main__':
    g = {'A': {'B': 1, 'C': 3}, 'B': {'A': 1, 'C': 1}, 'C': {'A': 3, 'B': 1}}
    print(prim(g))
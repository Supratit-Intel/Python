def dijkstra(graph, start):
    import heapq

    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        dist_u, u = heapq.heappop(pq)
        if dist_u > distances[u]:
            continue
        for v, w in graph[u].items():
            nd = dist_u + w
            if nd < distances[v]:
                distances[v] = nd
                heapq.heappush(pq, (nd, v))

    return distances


if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    print(dijkstra(graph, 'A'))
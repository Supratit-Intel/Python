def bellman_ford(graph, start):
    # graph as list of edges or dict; expecting dict: node->list of (neighbor, weight)
    # Convert to edge list
    edges = []
    vertices = set()
    for u in graph:
        vertices.add(u)
        for v, w in graph[u].items():
            vertices.add(v)
            edges.append((u, v, w))

    dist = {v: float('infinity') for v in vertices}
    dist[start] = 0

    for _ in range(len(vertices) - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break

    # Detect negative cycle
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return dist


if __name__ == '__main__':
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': -3},
        'C': {}
    }
    print(bellman_ford(graph, 'A'))
def floyd_warshall(graph):
    # graph: dict of dicts with weights; returns dict of dicts shortest paths
    nodes = list(graph.keys())
    dist = {u: {v: float('infinity') for v in nodes} for u in nodes}
    for u in nodes:
        dist[u][u] = 0
        for v, w in graph[u].items():
            dist[u][v] = w

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


if __name__ == '__main__':
    graph = {
        'A': {'B': 3, 'C': 8},
        'B': {'A': 3, 'C': 2},
        'C': {'A': 8, 'B': 2}
    }
    print(floyd_warshall(graph))
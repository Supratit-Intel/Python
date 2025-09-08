def topological_sort(graph):
    # Kahn's algorithm; graph: node -> list of neighbors
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] = in_degree.get(v, 0) + 1

    queue = [u for u in in_degree if in_degree[u] == 0]
    order = []
    while queue:
        u = queue.pop(0)
        order.append(u)
        for v in graph.get(u, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    if len(order) != len(in_degree):
        raise ValueError('Graph has at least one cycle')
    return order


if __name__ == '__main__':
    g = {'A': ['B'], 'B': ['C'], 'C': []}
    print(topological_sort(g))
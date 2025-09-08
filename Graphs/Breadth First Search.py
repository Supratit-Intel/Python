def bfs(graph, start):
    """Return BFS traversal order as a list starting from `start`.

    graph: dict mapping node -> list of neighbors
    start: starting node
    """
    visited = set()
    queue = [start]
    order = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            queue.extend(neighbor for neighbor in graph.get(vertex, []) if neighbor not in visited)

    return order


if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    print(bfs(graph, 'A'))
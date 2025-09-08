def dfs(graph, start):
    """Return DFS traversal order (preorder) as a list starting from `start`.

    Uses recursion.
    """
    visited = set()
    order = []

    def _dfs(u):
        visited.add(u)
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                _dfs(v)

    _dfs(start)
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
    print(dfs(graph, 'A'))
# Graph Algorithms

This directory contains simple, self-contained implementations of common graph algorithms. Each file exposes a small function and a short example under `if __name__ == "__main__"`.

## Algorithms

This folder contains the following algorithm implementations (file names match the scripts in this directory).

- Breadth First Search — `Breadth First Search.py`
	- Purpose: Layer-by-layer traversal from a start node. Useful for reachability and shortest unweighted paths.
	- Interface: `bfs(graph, start)` where `graph` is a dict node -> list(neighbors).

- Depth First Search — `Deapth First Search.py`
	- Purpose: Depth-first traversal (preorder) for component discovery, cycle detection, and traversal order.
	- Interface: `dfs(graph, start)` where `graph` is a dict node -> list(neighbors).
	- Note: Filename contains a small typo (`Deapth`) to match the present script; consider renaming to `Depth First Search.py` if desired.

- Dijkstra's Algorithm — `Dijkstra.py`
	- Purpose: Single-source shortest paths for graphs with non-negative edge weights.
	- Interface: `dijkstra(graph, start)` where `graph` is a dict node -> dict(neighbor -> weight).

- Bellman-Ford — `Bellman Ford.py`
	- Purpose: Single-source shortest paths supporting negative weights and cycle detection.
	- Interface: `bellman_ford(graph, start)` where `graph` is a dict node -> dict(neighbor -> weight) or equivalent.

- Floyd–Warshall — `Floyd Warshall.py`
	- Purpose: All-pairs shortest paths for dense graphs; returns a matrix/dict of distances between all node pairs.
	- Interface: `floyd_warshall(graph)` where `graph` is a dict node -> dict(neighbor -> weight).

- Kruskal's Algorithm — `Kruskal.py`
	- Purpose: Minimum spanning tree (MST) using edge-sorting and a disjoint-set (union-find).
	- Interface: `kruskal(edges, num_vertices)` where `edges` is a list of (weight, u, v) tuples.

- Prim's Algorithm — `Prim.py`
	- Purpose: Minimum spanning tree using a priority queue starting from an arbitrary node.
	- Interface: `prim(graph)` where `graph` is a dict node -> dict(neighbor -> weight).

- Topological Sort — `Topological Sort.py`
	- Purpose: Produce a linear ordering of nodes for a DAG.
	- Interface: `topological_sort(graph)` where `graph` is a dict node -> list(neighbors).

- A* Search — `A Star.py`
	- Purpose: Heuristic-guided shortest path search (best-first). Useful when a heuristic h(n) is available to guide the search.
	- Interface: `a_star(start, goal, h, neighbors)` where `neighbors(node)` yields (neighbor, cost) pairs and `h(node)` is the heuristic.

For example usage and I/O expectations, see the example blocks at the top of each script in this directory.

## Performance

This section lists time and space complexity for the algorithms above (typical implementations used in this folder).

- Breadth First Search (BFS)
	- Time: O(V + E) — visits each vertex and edge at most once.
	- Space: O(V) — for the visited set and queue.

- Breadth First Search (BFS)
	- Time: O(V + E) — visits each vertex and edge at most once.
	- Space: O(V) — for the visited set and queue.

- Depth First Search (DFS)
	- Time: O(V + E) — explores each vertex and edge once.
	- Space: O(V) — recursion stack or explicit stack plus visited set.

- Dijkstra's Algorithm
	- Time: O((V + E) log V) with a binary heap (Python's heapq). For sparse graphs this is roughly O(E log V).
	- Space: O(V) — to store distance estimates and the priority queue.

- Bellman-Ford
	- Time: O(V * E) — relaxes edges V-1 times.
	- Space: O(V) — distance table.

- Floyd–Warshall
	- Time: O(V^3) — three nested loops over nodes.
	- Space: O(V^2) — distance matrix.

- Kruskal's Algorithm
	- Time: O(E log E) dominated by sorting edges (or O(E log V)).
	- Space: O(V) for union-find structures and output MST.

- Prim's Algorithm
	- Time: O(E log V) with a binary heap; O(V^2) with adjacency matrix naive implementation.
	- Space: O(V) for the visited set and priority queue.

- Topological Sort
	- Time: O(V + E) — Kahn's algorithm or DFS-based approach.
	- Space: O(V) — in-degree map and output order.

- A* Search
	- Time: Depends on heuristic; worst-case comparable to Dijkstra (O((V + E) log V)).
	- Space: O(V) — open/closed sets and g/h score tables.

---
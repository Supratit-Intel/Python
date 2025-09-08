def a_star(start, goal, h, neighbors):
    # neighbors(node) -> list of (neighbor, cost)
    import heapq
    open_set = [(h(start), 0, start, None)]  # (f, g, node, parent)
    came_from = {}
    g_score = {start: 0}

    while open_set:
        f, g, current, parent = heapq.heappop(open_set)
        if current == goal:
            # reconstruct path
            path = [current]
            while parent is not None:
                path.append(parent)
                parent = came_from.get(parent)
            return path[::-1]
        if current in came_from:
            # already expanded
            continue
        came_from[current] = parent
        for neighbor, cost in neighbors(current):
            tentative_g = g + cost
            if tentative_g < g_score.get(neighbor, float('infinity')):
                g_score[neighbor] = tentative_g
                heapq.heappush(open_set, (tentative_g + h(neighbor), tentative_g, neighbor, current))
    return None


if __name__ == '__main__':
    # tiny example on a line
    def neighbors(u):
        return [(u+1, 1)] if u < 5 else []
    def h(u):
        return 5 - u
    print(a_star(0, 5, h, neighbors))
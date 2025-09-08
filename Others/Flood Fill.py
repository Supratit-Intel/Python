def flood_fill(grid, x, y, new_color):
    n, m = len(grid), len(grid[0])
    old = grid[x][y]
    if old == new_color:
        return
    def dfs(i, j):
        if i < 0 or j < 0 or i >= n or j >= m:
            return
        if grid[i][j] != old:
            return
        grid[i][j] = new_color
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            dfs(i+di, j+dj)
    dfs(x, y)
    return grid

if __name__ == '__main__':
    g = [[1,1,1],[1,1,0],[1,0,1]]
    print(flood_fill(g, 1, 1, 2))
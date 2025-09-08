def rat_in_maze(maze):
    n = len(maze)
    sol = [[0]*n for _ in range(n)]
    def is_safe(x,y):
        return 0<=x<n and 0<=y<n and maze[x][y]==1
    def solve(x,y):
        if x==n-1 and y==n-1:
            sol[x][y]=1
            return True
        if is_safe(x,y):
            sol[x][y]=1
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                if solve(x+dx,y+dy):
                    return True
            sol[x][y]=0
        return False
    if solve(0,0):
        return sol
    return None

if __name__ == '__main__':
    maze = [[1,0,0],[1,1,0],[0,1,1]]
    print(rat_in_maze(maze))
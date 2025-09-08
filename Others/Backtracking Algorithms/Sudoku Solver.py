def solve_sudoku(board):
    n = 9
    def find_empty():
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    return i,j
        return None
    def valid(num, pos):
        r,c = pos
        for i in range(n):
            if board[r][i]==num and i!=c:
                return False
            if board[i][c]==num and i!=r:
                return False
        br = (r//3)*3
        bc = (c//3)*3
        for i in range(br, br+3):
            for j in range(bc, bc+3):
                if board[i][j]==num and (i,j)!=pos:
                    return False
        return True
    empty = find_empty()
    if not empty:
        return True
    r,c = empty
    for num in range(1,10):
        if valid(num, (r,c)):
            board[r][c]=num
            if solve_sudoku(board):
                return True
            board[r][c]=0
    return False

if __name__ == '__main__':
    board = [[0]*9 for _ in range(9)]
    solve_sudoku(board)
    print(board)
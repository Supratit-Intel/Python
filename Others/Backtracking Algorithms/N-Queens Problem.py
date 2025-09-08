def solve_n_queens(n):
    solutions = []
    board = [-1]*n
    def safe(r, c):
        for i in range(r):
            if board[i] == c or abs(board[i]-c) == r-i:
                return False
        return True
    def backtrack(r):
        if r == n:
            solutions.append(board.copy())
            return
        for c in range(n):
            if safe(r, c):
                board[r] = c
                backtrack(r+1)
    backtrack(0)
    return solutions

if __name__ == '__main__':
    print(solve_n_queens(4))
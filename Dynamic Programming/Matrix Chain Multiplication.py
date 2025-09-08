def matrix_chain_order(p):
    """Compute minimum multiplication cost for matrix chain.

    p: list of matrix dimensions such that matrix Ai has dimensions p[i-1] x p[i]
    Returns minimal cost and optional split table.
    """
    n = len(p) - 1
    m = [[0] * (n+1) for _ in range(n+1)]
    s = [[0] * (n+1) for _ in range(n+1)]
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s

if __name__ == '__main__':
    p = list(map(int, input('Enter dimensions (space-separated): ').split()))
    m, s = matrix_chain_order(p)
    print('Minimum cost:', m[1][len(p)-1])
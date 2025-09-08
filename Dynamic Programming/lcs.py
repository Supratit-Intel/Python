def longest_common_subsequence(x, y):
    m = len(x)
    n = len(y)
    
    # Create a 2D array to store lengths of longest common subsequence.
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # The length of the longest common subsequence is in dp[m][n]
    return dp[m][n]

# Example usage
if __name__ == "__main__":
    x = "AGGTAB"
    y = "GXTXAYB"
    print("Length of LCS is", longest_common_subsequence(x, y))
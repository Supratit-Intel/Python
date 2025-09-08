def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


# Example usage
if __name__ == "__main__":
    n = int(input("Enter the position of Fibonacci number to compute: "))
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
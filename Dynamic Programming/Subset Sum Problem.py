def subset_sum(arr, target):
    """Return True if there exists a subset summing to target."""
    dp = [False] * (target+1)
    dp[0] = True
    for num in arr:
        for s in range(target, num-1, -1):
            dp[s] = dp[s] or dp[s-num]
    return dp[target]

if __name__ == '__main__':
    arr = list(map(int, input('Enter numbers: ').split()))
    target = int(input('Enter target: '))
    print(subset_sum(arr, target))
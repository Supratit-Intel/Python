def lis(arr):
    """Return length of Longest Increasing Subsequence and one LIS.

    Uses dynamic programming O(n^2) implementation for clarity.
    """
    if not arr:
        return 0, []
    n = len(arr)
    dp = [1] * n
    prev = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
    length = max(dp)
    idx = dp.index(length)
    seq = []
    while idx != -1:
        seq.append(arr[idx])
        idx = prev[idx]
    return length, seq[::-1]

if __name__ == '__main__':
    arr = list(map(int, input('Enter numbers: ').split()))
    length, seq = lis(arr)
    print('Length:', length)
    print('Sequence:', seq)
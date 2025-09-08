def coin_change(coins, amount):
    """Return fewest number of coins to make amount or -1 if impossible.

    Uses bottom-up DP.
    """
    dp = [0] + [float('inf')] * amount
    for coin in coins:
        for x in range(coin, amount+1):
            dp[x] = min(dp[x], dp[x-coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == '__main__':
    coins = list(map(int, input('Enter coin denominations: ').split()))
    amount = int(input('Enter amount: '))
    print(coin_change(coins, amount))
def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0:2] = [False, False]
    p = 2
    while p*p <= n:
        if is_prime[p]:
            for i in range(p*p, n+1, p):
                is_prime[i] = False
        p += 1
    return [i for i, val in enumerate(is_prime) if val]

if __name__ == '__main__':
    print(sieve(int(input('n: '))))
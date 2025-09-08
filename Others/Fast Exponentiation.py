def pow_fast(x, n):
    result = 1
    base = x
    exp = n
    while exp > 0:
        if exp & 1:
            result *= base
        base *= base
        exp >>= 1
    return result

if __name__ == '__main__':
    x = int(input('Base: '))
    n = int(input('Exponent: '))
    print(pow_fast(x, n))
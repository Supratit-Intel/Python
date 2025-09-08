def manacher(s):
    """Return longest palindromic substring using Manacher's algorithm."""
    t = '#'.join('^{}$'.format(s))
    n = len(t)
    p = [0] * n
    center = right = 0
    for i in range(1, n-1):
        mirror = 2*center - i
        if i < right:
            p[i] = min(right - i, p[mirror])
        while t[i + (1 + p[i])] == t[i - (1 + p[i])]:
            p[i] += 1
        if i + p[i] > right:
            center, right = i, i + p[i]
    max_len = max(p)
    center_index = p.index(max_len)
    start = (center_index - max_len) // 2
    return s[start:start + max_len]


if __name__ == '__main__':
    s = input('String: ')
    print(manacher(s))
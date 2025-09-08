def naive_search(text, pattern):
    """Return starting indices where pattern occurs in text (naive)."""
    n, m = len(text), len(pattern)
    res = []
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            res.append(i)
    return res


if __name__ == '__main__':
    text = input('Text: ')
    pattern = input('Pattern: ')
    print(naive_search(text, pattern))
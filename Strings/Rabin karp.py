def rabin_karp(text, pattern):
    d = 256
    q = 101
    M, N = len(pattern), len(text)
    p = t = 0
    h = 1
    for i in range(M - 1):
        h = (h * d) % q
    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(N - M + 1):
        if p == t and text[i:i + M] == pattern:
            print(f"Pattern found at index {i}")
        if i < N - M:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            if t < 0:
                t += q


if __name__ == "__main__":
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    rabin_karp(text, pattern)
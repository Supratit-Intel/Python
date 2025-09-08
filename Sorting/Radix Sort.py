def radix_sort(arr):
    
    if not arr:
        return []
    positives = [x for x in arr if x >= 0]
    negatives = [-x for x in arr if x < 0]

    def _lsd_sort(a):
        if not a:
            return []
        out = a[:]
        exp = 1
        max_val = max(out)
        while exp <= max_val:
            buckets = [[] for _ in range(10)]
            for num in out:
                digit = (num // exp) % 10
                buckets[digit].append(num)
            out = [x for bucket in buckets for x in bucket]
            exp *= 10
        return out

    sorted_pos = _lsd_sort(positives)
    sorted_neg = _lsd_sort(negatives)
    sorted_neg = [-x for x in reversed(sorted_neg)]
    return sorted_neg + sorted_pos


if __name__ == "__main__":
    try:
        arr = list(map(int, input("Enter array elements: ").split()))
    except Exception:
        arr = []
    print(radix_sort(arr))
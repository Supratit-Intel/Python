def counting_sort(arr):
    
    if not arr:
        return []
    min_v = min(arr)
    max_v = max(arr)
    offset = -min_v
    size = max_v - min_v + 1
    count = [0] * size
    for x in arr:
        count[x + offset] += 1
    for i in range(1, size):
        count[i] += count[i - 1]
    out = [0] * len(arr)
    for x in reversed(arr):
        idx = x + offset
        count[idx] -= 1
        out[count[idx]] = x
    return out


if __name__ == "__main__":
    try:
        arr = list(map(int, input("Enter array elements: ").split()))
    except Exception:
        arr = []
    print(counting_sort(arr))
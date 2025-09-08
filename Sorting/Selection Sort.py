def selection_sort(arr):

    a = arr[:]
    n = len(a)
    for end in range(n - 1, 0, -1):
        max_idx = 0
        for i in range(1, end + 1):
            if a[i] > a[max_idx]:
                max_idx = i
        a[end], a[max_idx] = a[max_idx], a[end]
    return a


if __name__ == "__main__":
    try:
        arr = list(map(int, input("Enter array elements: ").split()))
    except Exception:
        arr = []
    print(selection_sort(arr))
def binary_search_sub(arr, target, left, right):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def exponential_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == target:
        return 0
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    return binary_search_sub(arr, target, i // 2, min(i, n - 1))


if __name__ == "__main__":
    try:
        arr = list(map(int, input("Enter sorted array elements: ").split()))
        target = int(input("Enter target: "))
    except Exception:
        arr, target = [], None
    print(exponential_search(arr, target))
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        # probe position
        pos = low + int((float(high - low) / (arr[high] - arr[low])) * (target - arr[low]))
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1


if __name__ == "__main__":
    try:
        arr = list(map(int, input("Enter sorted array elements: ").split()))
        target = int(input("Enter target: "))
    except Exception:
        arr, target = [], None
    print(interpolation_search(arr, target))
import math


def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n)) if n else 0
    prev = 0
    while prev < n and arr[min(n - 1, prev + step - 1)] < target:
        prev += step
    # linear search within block
    for i in range(prev, min(prev + step, n)):
        if arr[i] == target:
            return i
    return -1


if __name__ == "__main__":
    try:
        arr = list(map(int, input("Enter sorted array elements: ").split()))
        target = int(input("Enter target: "))
    except Exception:
        arr, target = [], None
    print(jump_search(arr, target))
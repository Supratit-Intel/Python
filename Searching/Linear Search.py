def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


if __name__ == "__main__":
    try:
        arr = list(map(int, input("Enter array elements: ").split()))
        target = int(input("Enter target: "))
    except Exception:
        arr, target = [], None
    print(linear_search(arr, target))
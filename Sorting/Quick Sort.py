def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    try:
        arr = list(map(int, input("Enter array elements: ").split()))
    except Exception:
        arr = []
    print(quick_sort(arr))
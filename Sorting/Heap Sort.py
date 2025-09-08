def sift_down(arr, n, index):
    largest = index
    left_child = 2 * index + 1
    right_child = 2 * index + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        sift_down(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        sift_down(arr, i, 0)
    return arr


if __name__ == '__main__':
    try:
        arr = list(map(int, input("Enter array elements: ").split()))
    except Exception:
        arr = []
    print(heap_sort(arr))
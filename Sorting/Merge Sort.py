def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    sorted_arr = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_arr.append(left[left_index])
            left_index += 1
        else:
            sorted_arr.append(right[right_index])
            right_index += 1

    sorted_arr.extend(left[left_index:])
    sorted_arr.extend(right[right_index:])

    return sorted_arr


if __name__ == "__main__":
    try:
        arr = list(map(int, input("Enter array elements: ").split()))
    except Exception:
        arr = []
    sorted_arr = merge_sort(arr)
    print(sorted_arr)
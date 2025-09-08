def max_subarray(arr):
    max_ending = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending = max(x, max_ending + x)
        max_so_far = max(max_so_far, max_ending)
    return max_so_far

if __name__ == '__main__':
    print(max_subarray(list(map(int, input('Enter numbers: ').split()))))
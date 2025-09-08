# Sorting Algorithms

This directory contains implementations of various sorting algorithms. Each algorithm is designed to sort an array of elements in ascending order. Below is a brief overview of the algorithms included in this folder:

## Algorithms

1. **Quick Sort** (`Quick Sort.py`):
   - A divide-and-conquer algorithm that selects a 'pivot' element and partitions the array into two sub-arrays according to whether elements are less than or greater than the pivot. It recursively sorts the sub-arrays.

2. **Merge Sort** (`Merge Sort.py`):
   - Another divide-and-conquer algorithm that divides the array into halves, sorts each half, and then merges the sorted halves back together. It is known for its efficiency and stability.

3. **Heap Sort** (`Heap Sort.py`):
   - This algorithm uses a binary heap data structure to sort elements. It first builds a max heap from the input data and then repeatedly extracts the maximum element from the heap, rebuilding the heap until all elements are sorted.

4. **Bubble Sort** (`Bubble Sort.py`):
   - A simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. Best for small lists or educational purposes.

5. **Selection Sort** (`Selection Sort.py`):
   - Repeatedly selects the minimum (or maximum) element from the unsorted portion and moves it to the beginning (or end). Simple but O(n^2) time complexity.

6. **Insertion Sort** (`Insertion Sort.py`):
   - Builds the sorted array one element at a time, inserting each new element into its correct position among the already-sorted elements. Efficient for small or nearly-sorted lists.

7. **Counting Sort** (`Counting Sort.py`):
   - Non-comparison integer sorting algorithm that counts occurrences of each distinct value. Runs in O(n + k) where k is the range of input values; stable when implemented with prefix sums.

8. **Radix Sort** (`Radix Sort.py`):
   - Non-comparison integer sorting that processes digits (LSD or MSD). When digit size is fixed, it runs in linear time relative to input size.

## Usage

To use any of the sorting algorithms, you can import the respective Python file and call the sorting function with an array of integers. Each file also supports dynamic input when executed directly: run the file and enter space-separated integers on a single line.

Example (run in terminal):

```powershell
python "Bubble Sort.py"
# then type: 5 1 4 2 8
```

## Performance

Below are the typical time and space complexity characteristics and a note about stability for each algorithm included in this folder.

- **Bubble Sort** (`Bubble Sort.py`)
   - Best: O(n)
   - Average: O(n^2)
   - Worst: O(n^2)
   - Space: O(1)
   - Stable: Yes

- **Selection Sort** (`Selection Sort.py`)
   - Best/Average/Worst: O(n^2)
   - Space: O(1)
   - Stable: No (simple implementation)

- **Insertion Sort** (`Insertion Sort.py`)
   - Best: O(n)
   - Average: O(n^2)
   - Worst: O(n^2)
   - Space: O(1)
   - Stable: Yes

- **Merge Sort** (`Merge Sort.py`)
   - Best/Average/Worst: O(n log n)
   - Space: O(n) (additional arrays for merging)
   - Stable: Yes

- **Quick Sort** (`Quick Sort.py`)
   - Best/Average: O(n log n)
   - Worst: O(n^2) (rare, depends on pivot choice)
   - Space: O(log n) average for recursion (in-place variants)
   - Stable: No (standard in-place implementations)

- **Heap Sort** (`Heap Sort.py`)
   - Best/Average/Worst: O(n log n)
   - Space: O(1)
   - Stable: No

- **Counting Sort** (`Counting Sort.py`)
   - Time: O(n + k) where k is the range of input values
   - Space: O(k)
   - Stable: Yes (when implemented with prefix sums)

- **Radix Sort** (`Radix Sort.py`)
   - Time: O(d * (n + b)) where d is number of digits and b is base (often O(n) for fixed d)
   - Space: O(n + b)
   - Stable: Yes (when using a stable internal sort like counting sort per digit)

These are broad, textbook-level characteristics; actual performance can vary based on implementation details and input distribution.
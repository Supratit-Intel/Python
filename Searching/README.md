# Searching Algorithms

This directory contains implementations of various searching algorithms. Below is a brief overview of the algorithms included:

1. **Binary Search**:
   - Implemented in `binary_search.py`.
   - A fast search algorithm that works on sorted arrays by repeatedly dividing the search interval in half.

2. **Linear Search**:
    - Implemented in `linear_search.py`.
   - A simple search algorithm that checks each element in the array sequentially until the desired element is found or the array is exhausted.

3. **Jump Search**:
   - Implemented in `Jump Search.py`.
   - Works on sorted arrays by jumping ahead by fixed steps (usually sqrt(n)) and then doing a linear search within the identified block.

4. **Interpolation Search**:
   - Implemented in `Interpolation Search.py`.
   - An improvement over binary search for uniformly distributed sorted data — estimates the position of the target using linear interpolation.

5. **Exponential Search**:
   - Implemented in `Exponential Search.py`.
   - Useful for unbounded or large arrays; finds a range where the target lies by repeated doubling and then does binary search.

These algorithms are fundamental for searching data efficiently and are widely used in various applications.

## Performance

Below are typical time and space complexities and notes for each search algorithm included in this folder.

- **Linear Search** (`Linear Search.py`)
   - Best: O(1) (target at first position)
   - Average: O(n)
   - Worst: O(n)
   - Space: O(1)
   - Notes: No precondition on data ordering; use when data is small or unsorted.

- **Binary Search** (`Binary Search.py`)
   - Best: O(1)
   - Average/Worst: O(log n)
   - Space: O(1) (iterative) or O(log n) recursion depth
   - Notes: Requires sorted input.

- **Jump Search** (`Jump Search.py`)
   - Best: O(1)
   - Average/Worst: O(√n)
   - Space: O(1)
   - Notes: Works on sorted arrays; choose block size ≈ sqrt(n) for best performance.

- **Interpolation Search** (`Interpolation Search.py`)
   - Best: O(1)
   - Average: O(log log n) for uniformly distributed data
   - Worst: O(n)
   - Space: O(1)
   - Notes: Best for uniformly distributed sorted data; degrades to linear for skewed distributions.

- **Exponential Search** (`Exponential Search.py`)
   - Time: O(log n) to locate range + O(log n) for binary search → O(log n)
   - Space: O(1)
   - Notes: Useful for unbounded or large arrays where you don't know the array size upfront.
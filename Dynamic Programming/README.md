# Dynamic Programming Algorithms

This directory contains implementations of various dynamic programming algorithms. Each algorithm is designed to solve specific problems efficiently by breaking them down into simpler subproblems and storing the results of these subproblems to avoid redundant calculations.

## Algorithms Included

1. **Knapsack Problem (0/1 Knapsack)**:
   - Implemented in `knapsack.py`
   - This algorithm solves the problem of selecting items with given weights and values to maximize the total value without exceeding a specified weight limit.

2. **Longest Common Subsequence (LCS)**:
   - Implemented in `lcs.py`
   - This algorithm finds the longest subsequence present in two sequences, which is a common problem in string comparison.

3. **Fibonacci Sequence**:
   - Implemented in `fibonacci_dp.py`
   - This algorithm computes Fibonacci numbers using dynamic programming to optimize the calculation by storing previously computed values.

4. **Longest Increasing Subsequence (LIS)**:
    - Implemented in `Longest Increasing Subsequence.py`
    - Finds the length (and an example subsequence) of the longest strictly increasing subsequence of an array.

5. **Matrix Chain Multiplication**:
    - Implemented in `Matrix Chain Multiplication.py`
    - Computes the minimal number of scalar multiplications needed to multiply a chain of matrices.

6. **Coin Change Problem**:
    - Implemented in `Coin Change Problem.py`
    - Computes the minimum number of coins needed to make a target amount (or reports impossible).

7. **Minimum Edit Distance (Levenshtein Distance)**:
    - Implemented in `Minimum Edit Distance.py`
    - Computes the minimal number of insertions, deletions, and substitutions to convert one string to another.

8. **Subset Sum Problem**:
    - Implemented in `Subset Sum Problem.py`
    - Determines whether there exists a subset of numbers that sums to a given target.

## Performance (quick reference)

- Fibonacci (DP)
   - Time: O(n)
   - Space: O(n) (or O(1) with rolling variables)

- Knapsack (0/1)
   - Time: O(n * W) where W is capacity
   - Space: O(n * W) (can be reduced to O(W))

- Longest Common Subsequence (LCS)
   - Time: O(n * m) for strings of lengths n and m
   - Space: O(n * m) (can be optimized)

- Longest Increasing Subsequence (LIS)
   - Time: O(n^2) for the DP implementation; O(n log n) is possible with patience sorting.
   - Space: O(n)

- Matrix Chain Multiplication
   - Time: O(n^3)
   - Space: O(n^2)

- Coin Change (min coins)
   - Time: O(amount * number_of_coins)
   - Space: O(amount)

- Minimum Edit Distance
   - Time: O(n * m)
   - Space: O(n * m) (can be optimized to O(min(n, m)))

- Subset Sum
   - Time: O(n * target)
   - Space: O(target)


## Usage

Each algorithm can be imported and used in your Python projects. Refer to the individual algorithm files for specific usage instructions and examples.
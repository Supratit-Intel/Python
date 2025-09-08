# String Algorithms

This directory contains implementations of various string algorithms. Below is a brief overview of the algorithms included:

1. **Knuth-Morris-Pratt (KMP) Algorithm**:
   - File: `kmp.py`
   - Description: An efficient algorithm for substring searching that preprocesses the pattern to allow for faster searching in the text.

2. **Rabin-Karp Algorithm**:
   - File: `rabin_karp.py`
   - Description: A string searching algorithm that uses hashing to find any one of a set of pattern strings in a text. It is particularly useful for multiple pattern searches.

3. **Naive String Matching**:
    - File: `Naive String Matching.py`
    - Description: Simple substring search by checking every possible alignment. Best for short texts or when simplicity matters.

4. **Z Algorithm**:
    - File: `Z Algorithm.py`
    - Description: Computes Z-array for a string; useful for pattern matching and string queries. Runs in linear time.

5. **Manacher's Algorithm**:
    - File: `Manacher's Algorithm.py`
    - Description: Finds the longest palindromic substring in linear time using a center-expansion trick with mirror information.

## Performance (quick reference)

- Naive search
   - Time: O(n * m) worst-case (text length n, pattern length m)
   - Space: O(1)

- KMP
   - Time: O(n + m)
   - Space: O(m) for prefix table

- Rabin-Karp
   - Time: O(n + m) expected with rolling hash; O(n * m) worst-case if hashes collide and verification is needed
   - Space: O(1)

- Z Algorithm
   - Time: O(n)
   - Space: O(n) for Z-array

- Manacher's Algorithm
   - Time: O(n)
   - Space: O(n)

These algorithms are fundamental in string processing and can be utilized in various applications such as text editing, searching, and data compression.
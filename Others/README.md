# Other Popular Algorithms

This directory contains standalone implementations of a set of commonly used algorithms that don't fit neatly into the other folders. Each file is named to match the algorithm it implements; run the script directly for a small example or import the function(s) in your own code.

## Algorithms

- Binary Search Tree — `Binary Search Tree.py`
	- Interface: `BST` class with `insert(key)`, `search(key) -> bool`, `delete(key)`.

- Union-Find / Disjoint Set — `union_find.py`
	- Interface: `UnionFind(size)` class with `find(x)`, `union(x, y)`, `connected(x, y)`.

- Bit Manipulation helpers — `bit_manipulation.py`
	- Small utility functions: `count_set_bits`, `is_power_of_two`, `set_ith_bit`, `clear_ith_bit`, etc.

- Kadane's Algorithm — `Kadane's Algorithm.py`
	- Interface: `max_subarray(arr)` returns maximum subarray sum.

- Fast Exponentiation — `Fast Exponentiation.py`
	- Interface: `pow_fast(x, n)` computes x^n in O(log n) time.

- Sieve of Eratosthenes — `Sieve of Eratosthenes.py`
	- Interface: `sieve(n)` returns primes up to n.

- Flood Fill — `Flood Fill.py`
	- Interface: `flood_fill(grid, x, y, new_color)` modifies the grid in-place.

- N-Queens —  `Backtracking Algorithms/N-Queens Problem.py`
	- Helpers provide `solve_n_queens(n)`; example loader in `N-Queens Problem.py`.

- Rat in a Maze — `Backtracking Algorithms/Rat in a Maze.py`
	- Interface: `rat_in_maze(maze)` returns a solution matrix if a path exists.

- Sudoku Solver — `Backtracking Algorithms/Sudoku Solver.py`
	- Interface: `solve_sudoku(board)` solves 9x9 sudoku in-place.

- Activity Selection — `Greedy Algorithms/Activity Selection.py`
	- `activity_selection(intervals)` selects maximum number of non-overlapping intervals.

- Huffman Coding — `Greedy Algorithms/Huffman Coding.py` 
	- Interface: `huffman_encode(freq)` returns prefix codes.

- Job Sequencing Problem — `Greedy Algorithms/Job Sequencing Problem.py`
	- Interface: `job_sequencing(jobs)` returns scheduled job slots and total profit.

## Performance (organized)

- Binary Search Tree (`Binary Search Tree.py`)
	- Time: Average O(log n); Worst O(n) when unbalanced
	- Space: O(n)

- Union-Find (`union_find.py`)
	- Time: Nearly O(1) amortized per op (path compression + union by rank)
	- Space: O(n)

- Bit Manipulation (`bit_manipulation.py`)
	- Time: O(1) for simple ops; counting bits O(k) where k = bit-width or number of set bits
	- Space: O(1)

- Kadane's Algorithm (`Kadane's Algorithm.py`)
	- Time: O(n)
	- Space: O(1)

- Fast Exponentiation (`Fast Exponentiation.py`)
	- Time: O(log n)
	- Space: O(1)

- Sieve of Eratosthenes (`Sieve of Eratosthenes.py`)
	- Time: O(n log log n)
	- Space: O(n)

- Flood Fill (`Flood Fill.py`)
	- Time: O(rows * cols)
	- Space: O(rows * cols) worst-case recursion/queue

- Backtracking (N-Queens, Sudoku)
	- Time: Exponential in worst case (problem-specific)
	- Space: O(n) recursion depth + problem state

- Rat in a Maze (`Rat in a Maze.py`)
	- Time: Exponential worst-case (search), depends on maze size
	- Space: O(n^2) for n x n maze solution/state

- Greedy / Activity Selection
	- Time: O(n log n) (sorting dominates)
	- Space: O(n)

- Huffman Coding (`Huffman Coding.py`)
	- Time: O(k log k) for k symbols
	- Space: O(k)

- Job Sequencing (`Job Sequencing Problem.py`)
	- Time: O(n^2) naive; DSU-based optimizations exist
	- Space: O(n)

If you want, I can add example calls, small runtime benchmarks for selected inputs, or unit tests for key algorithms.
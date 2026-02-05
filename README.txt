PAY ATTENTION!!!:
I used GitHub Copilot while writing this code. I analyzed the generated code and understood it`s details.
Copilot was used to save time and simplify the task.


PROJECT DESCRIPTION
-------------------
This program finds the shortest superstring that contains all input strings
as substrings. It uses advanced algorithms including exact dynamic programming
(for small datasets) and simulated annealing local search (for larger datasets).


INPUT FILE FORMAT
-----------------
File: numbers.txt

Requirements:
- Plain text file with one string per line
- Each line will be stripped of leading/trailing whitespace
- Empty lines are ignored
- No file size limit, but very large files may be slower

Example numbers.txt:
---
ABCD
BCDE
CDEF
---


HOW TO RUN
----------
python3 calculate.py

or

python calculate.py


PROGRAM WORKFLOW
----------------
1. Reads all strings from numbers.txt
2. Removes duplicate strings
3. Removes strings that are contained within other strings
4. Uses one of two algorithms:
   - Exact algorithm (if ≤20 strings remain) - guaranteed optimal solution
   - Advanced local search with annealing (if >20 strings) - fast heuristic
5. Outputs the shortest superstring and its length


OUTPUT INFORMATION
------------------
The program prints:
- Total strings read from file
- Number of strings removed (duplicates or contained in others)
- Remaining strings after cleanup
- Algorithm used
- Result length (length of the shortest superstring found)
- The resulting superstring
- Order of strings used (if ≤50 remaining strings)

Example output:
---
Total strings read: 100
Skipped strings (duplicates or contained in others): 30
Remaining strings after cleanup: 70
Method used: Advanced local-search (anneal, restarts=50, iterations=10000, seed=0)
Result length: 2450
Resulting superstring: ABCDEFGHIJKLMNOPQRSTUVWXYZ...
---


FILE STRUCTURE
--------------
calculate.py     - Main entry point and program logic
utils.py         - File reading utilities
rmv_dub.py       - Duplicate and substring removal functions
overlap.py       - String overlap detection and matrix building
superstring.py   - Exact shortest superstring algorithm (DP)
search.py        - Advanced local search algorithms
numbers.txt      - Input file (user-provided)


ALGORITHM DETAILS
-----------------

EXACT ALGORITHM (used for ≤20 strings):
- Uses dynamic programming with bitmask approach
- Time complexity: O(2^n * n^2)
- Guarantees the optimal (shortest) result
- Only practical for small datasets (n ≤20)

ADVANCED LOCAL SEARCH (used for >20 strings):
- Uses simulated annealing for optimization
- Randomly explores solution space with decreasing probability of accepting worse solutions
- Parameters:
  * strategy: 'anneal' (simulated annealing)
  * restarts: 50 (number of independent searches)
  * iterations: 10000 (iterations per restart)
  * temp_start: 1.0 (initial temperature)
  * cooling: 0.995 (temperature reduction rate)
- No optimality guarantee but finds good solutions quickly


KEY FUNCTIONS
-------------

read_numbers(path)
- Reads strings from file
- Input: file path (string)
- Output: list of strings

remove_substrings(strings)
- Removes duplicates and contained strings
- Input: list of strings
- Output: tuple (kept_strings, skipped_strings)

overlap(a, b)
- Calculates how much of string 'a' overlaps with start of string 'b'
- Input: two strings
- Output: overlap length (integer)

build_overlap_matrix(strings)
- Pre-computes all pairwise overlaps
- Input: list of strings
- Output: 2D matrix of overlaps

exact_shortest_superstring(strings)
- Finds optimal superstring (for small inputs)
- Input: list of strings
- Output: tuple (superstring, order_of_strings)

advanced_local_search(strings, ...)
- Finds near-optimal superstring (for large inputs)
- Input: list of strings and parameters
- Output: tuple (superstring, order_of_strings)


TIPS & BEST PRACTICES
---------------------
1. Remove obviously redundant strings before running
2. For >100 strings, results may take a few seconds
3. For >1000 strings, consider pre-processing to reduce input
4. All strings should be DNA sequences or similar for best results
5. Avoid very long strings (>10000 characters each)


TROUBLESHOOTING
---------------
Q: Program crashes reading numbers.txt
A: Check file exists in the same directory as calculate.py
   Make sure file is in plain text format (not Word document, etc.)

Q: Getting "No strings to process"
A: All input strings were duplicates or contained in other strings
   Check numbers.txt has valid, unique strings

Q: Program running very slowly
A: You may have >100 strings with local search enabled
   This is normal - algorithm is working hard to find good solutions
   Reduce number of restarts or iterations in search.py if needed

Q: Results look wrong
A: Verify that all strings from numbers.txt are in the result
   They should all appear as substrings in the output


PERFORMANCE EXPECTATIONS
-------------------------
<20 strings:     Instant to <1 second
20-100 strings:  1-30 seconds (uses local search)
100-500 strings: 30 seconds to 5 minutes
>500 strings:    5+ minutes (consider sampling input)


================================================================================
Version: 1.0 | Last Updated: February 2026
================================================================================

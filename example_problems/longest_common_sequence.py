from typing import Any, List
import numpy as np

# Finding the longest common subsequence (LCS) between two arrays is a classical example of using dynamic programming.
# Let the arrays have lengths M and N, and stored as variables a[0:M] and b[0:N].
# Let’s use L[p, q] to mark the length of the LCS for subarrays a[0:p], b[0:q]; that is, L[p, q] == LCS(a[0:p], b[0:q]).
# Let’s also visualize what a matrix L[p, q] would look like for an example pair of “bananas” and “sandal”.
#
# p/q	0	1 B	2 A	3 N	4 A	5 N	6 A	7 S
# 0	0	0	0	0	0	0	0	0
# 1 S	0	0	0	0	0	0	0	1
# 2 A	0	0	1	1	1	1	1	1
# 3 N	0	0	1	2	2	2	2	2
# 4 D	0	0	1	2	2	2	2	2
# 5 A	0	0	1	2	3	3	3	3
# 6 L	0	0	1	2	3	3	3	3
# If p or q is zero, then L[p, q] = 0 since we have one empty subarray.
# All other fields have a simple rule connecting them - L[p, q] equals to the maximum value of the following options:
#
# L[p - 1, q] - the LCS didn’t change, we just added one letter to array a to achieve L[p, q]
# L[p, q - 1] - analogous for array b
# L[p - 1, q - 1]+1 - adding the same letter to both a and b, which of course can’t happen for every field

test_a = list("bananas")
test_b = list("sandal")


def longest_common_sequence(first: List[Any], second: List[Any]) -> np.matrix:
    first_length = len(first)
    second_length = len(second)

    results = np.matrix(first_length + 1, second_length + 1)

    for i in range(0, first_length):
        results[i, 0] = 0

    for i in range(0, second_length):
        results[0, i] = 0

    for i in range(1, first_length):
        for j in range(1, second_length):
            results[i, j] = max(results[i - 1, j], results[i, j - 1])
            if first[i - 1] == second[j - 1]:
                results[i, j] = max(results[i, j], results[i - 1, j - 1] + 1)

    return results
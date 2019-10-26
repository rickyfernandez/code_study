from typing import List

"""
Given a permutation compute the next permutation using dictionary ordering
(e.g. (1, 2, 3) < (1, 3, 2) as string sorting. Solution use the insight that
the last/largets permutation has the order (n, n-1, n-2, ...) and the smallest
has the order (1, 2, 3, ...), thus every larger permutation has a suffix of
decreasing values we need to find the beginning that suffix and swap it with
the next increasing value followed by sorting the suffix.

(1, 2, 4, 3, 0) -> (1, 3, 4, 2, 0) -> (1, 3, 0, 2, 4)
"""

def next_permutation(perm: List[int]) -> List[int]:
    i = len(perm) - 2
    while perm[i] > perm[i+1] and perm[i] >= 0:
        i -= 1
    # last possible permutation
    if i == -1: return perm

    j = len(perm)-1
    while perm[i] > perm[j]:
        j -= 1
    perm[i], perm[j] = perm[j], perm[i]
    perm[i+1:] = reversed(perm[i+1:])

if __name__ == "__main__":
    x = [6, 2, 1, 5, 4, 3, 0]
    print(x)
    next_permutation(x)
    print(x)

from typing import List
"""
Given a sorted array with duplicates remove each element thus keeping
only unique values, return the last index of the new array. Solution,
use a new index that only increments when a new value is found.
"""

def sorted_array_remove_dups(A: List[int]) -> int:
    # all values less than 1 are unique
    # keep this invariant
    j = 1
    for i in range(1,len(A)):
        if A[i] != A[i-1]:
            A[j] = A[i]
            j += 1
    return j


if __name__ == "__main__":
    x = [2, 3, 5, 5, 7, 11, 11, 11, 13]
    print(x)
    v = sorted_array_remove_dups(x)
    print(x[:v])

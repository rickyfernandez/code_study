from typing import List

"""
Given a list A and a permutation reorder A in that permutatin
in constant space. Solution, we use the permutation array for
storage. At each index we swap A and perm untill that slot
is cleared.
"""

def apply_permutation(perm: List[int], A: List[str]) -> None:
    for i in range(len(A)):
        while perm[i] != i:
            A[perm[i]], A[i] = A[i], A[perm[i]]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]

if __name__ == "__main__":
    x = ["a", "b", "c", "d"]
    p = [2, 0, 1, 3]
    print(x, p)
    apply_permutation(p, x)
    print(x)


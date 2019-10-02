from typing import List

"""
move all even elements to the front and all odd to the back. The solution
uses the idea that we have two pointers that track the boundary of un-
processed elements. We process each element so that the array can be
though of consisting of three arrays even - unprocessed - odd
"""

def even_odd(A: List[int]) -> None:
    i, j = 0, len(A)-1
    while i < j:
        if A[i] % 2 == 0: # even
            i += 1
        else: # odd
            A[i], A[j] = A[j], A[i]
            j -= 1

if __name__ == "__main__":
    x = [2, 5, 4, 3]
    print(x)
    even_odd(x)
    print(x)

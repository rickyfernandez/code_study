from typing import List

"""
move all the elements less than A[pivot_index] to the left of the
array followed by values equal to A[pivot_index] then by values
greater than A[pivot_index]. Solution use the following

A[:i] = values less than A[pivot_index]
A[i:j+1] = values equal to A[pivot_index]
A[j+1:] = values greate than A[pivot_index]

hence we keep this statement true as we traverse the array.
with k untill k == j
"""

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    i, k, j = 0, 0, len(A)-1
    pivot = A[pivot_index]
    while k <= j:
        if A[k] < pivot:
            A[k], A[i] = A[i], A[k]
            i += 1; k += 1
        elif A[k] > pivot:
            A[k], A[j] = A[j], A[k]
            j -= 1
        else:
            k += 1

if __name__ == "__main__":
    x = [0, 1, 2, 5, 2, 3, 1, 0, 2]
    print(x)
    dutch_flag_partition(2, x)
    print(x)

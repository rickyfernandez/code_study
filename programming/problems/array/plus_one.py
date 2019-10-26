from typing import List

"""
integer is represented as list add one and return result as list. Here
we take advantage that propagate a 1 only if the last digit becomes
a 10.
"""

def plus_one(A: List[int]) -> List[int]:
    A[-1] += 1
    for i in reversed(range(1,len(A))):
        if A[i] != 10:
            break

        A[i] = 0
        A[i-1] += 1

    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

if __name__ == "__main__":
    x = [9, 9, 9]
    print(x)
    print( plus_one(x))

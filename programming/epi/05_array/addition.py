from typing import List

"""
Given two list that represents an integer (ie. 121 -> [1, 2, 1])
add both and return in a new list. Solution, loop from the back
of both arrays adding each digit, if value is greater than 10
save remainder and add the multiples of 10 to the next digit.
We keep track of indices for each array.
"""

def addition(A: List[int], B: List[int]) -> List[int]:
    n1, n2 = len(A), len(B)

    j = n1-1
    k = n2-1
    result = [0]*(n1 + n2)
    for i in reversed(range(1, len(result))):
        if j >= 0 and k >= 0:
            result[i] += (A[j] + B[k]) % 10
            result[i-1] += (A[j] + B[k])//10
            j -= 1; k -= 1

        elif j >= 0:
            val = result[i] + A[j]
            result[i] = val % 10
            result[i-1] += val//10
            j -= 1

        elif k >= 0:
            val = result[i] + B[k]
            result[i] = val % 10
            result[i-1] += val//10
            k -= 1

    i = 0
    while result[i] == 0: i += 1
    if result[i] == 10:
        result[i] == 0
        result[i-1] == 0
        i -= 1
    return result[i:]


if __name__ == "__main__":
    x1 = [9, 9, 9]
    x2 = [1]
    print(x1, x2, addition(x1, x2))

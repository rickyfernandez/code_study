from typing import List

"""
Create pascals triangle. Solution, we use a list to hold all entries,
we use the observation that for row i>1 0<j<i j is the sum of
j-1 and j elements from i-1.
"""

def pascal_triangle(n: int) -> List[int]:
    res = [[1]*(i+1) for i in range(n)]
    for i in range(1, n):
        for j in range(1, i):
            res[i][j] = res[i-1][j-1] + res[i-1][j]
    return res

if __name__ == "__main__":
    n = 7
    pt = pascal_triangle(n)
    print(n)
    for row in pt:
        print(row)

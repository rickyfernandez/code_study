from typing import List

"""
An array has values for each index the max that can be taken
from that index. Determine if you can hop your way to the end.
Solution, at each step determine the max steps you can take
as long this value is less than index traveled then you can
reach that index otherwise you cannot make it. A drawing gives
a better example:
           -
           |
        -------
        |  |  |
    -----  .  .
    |   |  |  |
    [1, 2, 0, 1]

each index displays furthest can travel where from that position
but the move is only valid if we could get there in the first place.
"""

def can_reach_end(A: List[int]) -> bool:
    max_so_far = 0
    for i in range(len(A)):
        max_so_far = max(max_so_far, i+x[i])
        if max_so_far <= i:
            return False
    return True

if __name__ == "__main__":
    x = [2, 4, 1, 1, 0, 2, 3]
    print(x, can_reach_end(x))

import random
import numpy as np
from typing import List

def offline_sampling(k: int, A: List[int]) -> None:
    for i in range(k):
        j = random.randint(i, len(A)-1)
        A[i], A[j] = A[j], A[i]
    return A[:k]

if __name__ == "__main__":
    k = 4
    x = np.arange(10)
    np.random.seed(0)
    print(offline_sampling(k, x))

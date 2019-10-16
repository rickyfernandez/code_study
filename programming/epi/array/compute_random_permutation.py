from typing import List
from offline_sampling import offline_sampling

def compute_random_permutation(n: int) -> List[int]:
    p = list(range(n))
    return offline_sampling(n, p)

if __name__ == "__main__":
    n = 6
    print(n, compute_random_permutation(n))
